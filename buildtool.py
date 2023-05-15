import glob
import importlib
import json
import os
import sys

project = {}

data = open(sys.argv[1], "r").read()
project["jdata"] = json.loads(data)


# loading plugins
project["plugins"] = {}
for path in glob.glob("plugins/*"):
    plugin = path.split("/")[1]
    vplugin = importlib.import_module(".plugin", f"plugins.{plugin}")
    project["plugins"][plugin] = vplugin.Plugin(project["jdata"])


generators = {}
for path in glob.glob("generators/*"):
    generator = path.split("/")[1]
    generators[generator] = importlib.import_module(
        f".{generator}", f"generators.{generator}"
    )


project["verilog_files"] = []
project["pinlists"] = {}

project["osc_clock"] = False
if project["jdata"]["toolchain"] == "icestorm":
    project["osc_clock"] = project["jdata"]["clock"].get("osc")
    if project["osc_clock"]:
        project["pinlists"]["main"] = (
            ("sysclk_in", project["jdata"]["clock"]["pin"], "INPUT"),
        )
    else:
        project["pinlists"]["main"] = (
            ("sysclk", project["jdata"]["clock"]["pin"], "INPUT"),
        )

if "blink" in project["jdata"]:
    project["pinlists"]["blink"] = (
        ("BLINK_LED", project["jdata"]["blink"]["pin"], "OUTPUT"),
    )

if "error" in project["jdata"]:
    project["pinlists"]["error"] = (
        ("ERROR_OUT", project["jdata"]["error"]["pin"], "OUTPUT"),
    )

for plugin in project["plugins"]:
    if hasattr(project["plugins"][plugin], "pinlist"):
        project["pinlists"][plugin] = project["plugins"][plugin].pinlist()

project["dins"] = 0
for plugin in project["plugins"]:
    if hasattr(project["plugins"][plugin], "dins"):
        project["dins"] += project["plugins"][plugin].dins()

project["douts"] = 0
for plugin in project["plugins"]:
    if hasattr(project["plugins"][plugin], "douts"):
        project["douts"] += project["plugins"][plugin].douts()

project["vouts"] = 0
for plugin in project["plugins"]:
    if hasattr(project["plugins"][plugin], "vouts"):
        project["vouts"] += project["plugins"][plugin].vouts()

project["vins"] = 0
for plugin in project["plugins"]:
    if hasattr(project["plugins"][plugin], "vins"):
        project["vins"] += project["plugins"][plugin].vins()

project["joints"] = 0
for plugin in project["plugins"]:
    if hasattr(project["plugins"][plugin], "joints"):
        project["joints"] += project["plugins"][plugin].joints()

project["jointcalcs"] = {}
for plugin in project["plugins"]:
    if hasattr(project["plugins"][plugin], "jointcalcs"):
        project["jointcalcs"].update(project["plugins"][plugin].jointcalcs())

project["joints_en_total"] = (project["joints"] + 7) // 8 * 8
project["douts_total"] = (project["douts"] + 7) // 8 * 8
project["dins_total"] = (project["dins"] + 7) // 8 * 8
project["douts_total"] = max(project["douts_total"], 8)
project["dins_total"] = max(project["dins_total"], 8)

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


# file structure
project[
    "OUTPUT_PATH"
] = f"Output/{project['jdata']['name'].replace(' ', '_').replace('/', '_')}"
project["FIRMWARE_PATH"] = f"{project['OUTPUT_PATH']}/Firmware"
project["SOURCE_PATH"] = f"{project['FIRMWARE_PATH']}"
project["PINS_PATH"] = f"{project['FIRMWARE_PATH']}"
project["LINUXCNC_PATH"] = f"{project['OUTPUT_PATH']}/LinuxCNC"
os.system(f"mkdir -p {project['OUTPUT_PATH']}")
os.system(f"mkdir -p {project['SOURCE_PATH']}")
os.system(f"mkdir -p {project['PINS_PATH']}")
os.system(f"mkdir -p {project['LINUXCNC_PATH']}")
os.system(f"mkdir -p {project['LINUXCNC_PATH']}/Components/")
os.system(f"mkdir -p {project['LINUXCNC_PATH']}/ConfigSamples/rio")

if project["jdata"]["toolchain"] == "diamond":
    project["SOURCE_PATH"] = f"{project['FIRMWARE_PATH']}/impl1/source"
    project["PINS_PATH"] = f"{project['FIRMWARE_PATH']}/impl1/source"
    os.system(f"mkdir -p {project['SOURCE_PATH']}")
    os.system(f"mkdir -p {project['PINS_PATH']}")


print(f"generating files in {project['OUTPUT_PATH']}")


for generator in generators.values():
    generator.generate(project)
