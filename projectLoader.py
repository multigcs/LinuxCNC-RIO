import glob
import importlib
import json
import os
import sys


def load(configfile):
    project = {}
    project["config"] = configfile
    if not os.path.isfile(project["config"]):
        print("")
        print(f"this is not a file: {project['config']}")
        print("")
        exit(1)

    try:
        with open(project["config"], "r") as f:
            data = f.read()
    except IOError as err:
        print("")
        print(err)
        print("")
        exit(1)

    try:
        project["jdata"] = json.loads(data)
    except ValueError as err:
        print("")
        print(f"JSON error: {err}")
        print("please check your json syntax")
        print("")
        exit(1)

    if "plugins" not in project["jdata"]:
        print("ERROR: old json config format, please run 'python3 convert-configs.py'")
        sys.exit(1)

    # loading plugins
    project["plugins"] = {}
    for path in glob.glob("plugins/*"):
        plugin = path.split("/")[1]
        if os.path.isfile(f"plugins/{plugin}/plugin.py"):
            vplugin = importlib.import_module(".plugin", f"plugins.{plugin}")
            project["plugins"][plugin] = vplugin.Plugin(project["jdata"])

    project["generators"] = {}
    for path in glob.glob("generators/*"):
        generator = path.split("/")[1]
        if os.path.isfile(f"generators/{generator}/{generator}.py"):
            project["generators"][generator] = importlib.import_module(
                f".{generator}", f"generators.{generator}"
            )

    project["verilog_files"] = []
    project["pinlists"] = {}
    project["expansions"] = {}
    project["internal_clock"] = None

    project["osc_clock"] = False
    if project["jdata"].get("toolchain") == "icestorm":
        project["osc_clock"] = project["jdata"]["clock"].get("osc")
        project["internal_clock"] = project["jdata"]["clock"].get("internal")
        if project["internal_clock"]:
            pass
        elif project["osc_clock"]:
            project["pinlists"]["main"] = (
                ("sysclk_in", project["jdata"]["clock"]["pin"], "INPUT", True),
            )
        else:
            project["pinlists"]["main"] = (
                ("sysclk", project["jdata"]["clock"]["pin"], "INPUT", True),
            )
    else:
        project["pinlists"]["main"] = (
            ("sysclk", project["jdata"]["clock"]["pin"], "INPUT", True),
        )

    if "blink" in project["jdata"]:
        project["pinlists"]["blink"] = (
            ("BLINK_LED", project["jdata"]["blink"]["pin"], "OUTPUT"),
        )

    if "error" in project["jdata"]:
        project["pinlists"]["error"] = (
            ("ERROR_OUT", project["jdata"]["error"]["pin"], "OUTPUT"),
        )

    if "enable" in project["jdata"]:
        project["pinlists"]["enable"] = (
            ("ENA", project["jdata"]["enable"]["pin"], "OUTPUT"),
        )

    for plugin in project["plugins"]:
        if hasattr(project["plugins"][plugin], "pinlist"):
            project["pinlists"][plugin] = project["plugins"][plugin].pinlist()
        if hasattr(project["plugins"][plugin], "expansions"):
            project["expansions"][plugin] = project["plugins"][plugin].expansions()

    # check for double assigned pins
    double_pins = False
    uniq_pins = {}
    for pinlist in project["pinlists"].values():
        for pinsetup in pinlist:
            pin_name = pinsetup[0]
            pin_id = pinsetup[1]
            if pin_id in uniq_pins:
                print()
                print(f"ERROR: pin {pin_id} allready in use")
                print(f"  old: {uniq_pins[pin_id]}")
                print(f"  new: {pinsetup}")
                double_pins = True
            else:
                uniq_pins[pin_id] = pinsetup
    if double_pins:
        print("")
        exit(1)

    for dtype in ("vin", "vout", "din", "dout", "joint"):
        tname = f"{dtype}names"
        if tname not in project:
            project[tname] = []
        for plugin in project["plugins"]:
            if hasattr(project["plugins"][plugin], tname):
                func = getattr(project["plugins"][plugin], tname)
                project[tname] += func()

        project[f"{dtype}s"] = len(project[tname])
        project[f"{dtype}s_total"] = max((len(project[tname]) + 7) // 8 * 8, 8)

    project["jointtypes"] = []
    for joint in project["jointnames"]:
        project["jointtypes"].append(joint["type"])

    project["joints_en_total"] = (project["joints"] + 7) // 8 * 8

    project["tx_data_size"] = 32
    project["tx_data_size"] += project["joints"] * 32
    project["tx_data_size"] += project["vins"] * 32
    project["tx_data_size"] += project["dins_total"]
    project["rx_data_size"] = 32
    project["rx_data_size"] += project["joints"] * 32
    project["rx_data_size"] += project["vouts"] * 32
    project["rx_data_size"] += project["joints_en_total"]
    project["rx_data_size"] += project["douts_total"]
    project["data_size"] = max(project["tx_data_size"], project["rx_data_size"])

    return project
