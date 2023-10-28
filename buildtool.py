#!/usr/bin/env python3
#
#

import argparse
import os

import projectLoader


def main(configfile, outputdir=None):

    project = projectLoader.load(configfile)

    # file structure
    if outputdir:
        project["OUTPUT_PATH"] = outputdir
    else:
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
    os.system(f"mkdir -p {project['LINUXCNC_PATH']}/ConfigSamples/rio/subroutines")
    os.system(f"mkdir -p {project['LINUXCNC_PATH']}/ConfigSamples/rio/m_codes")
    os.system(
        f"cp -a files/subroutines/* {project['LINUXCNC_PATH']}/ConfigSamples/rio/subroutines"
    )

    if project["jdata"].get("toolchain") == "diamond":
        project["SOURCE_PATH"] = f"{project['FIRMWARE_PATH']}/impl1/source"
        project["PINS_PATH"] = f"{project['FIRMWARE_PATH']}/impl1/source"
        os.system(f"mkdir -p {project['SOURCE_PATH']}")
        os.system(f"mkdir -p {project['PINS_PATH']}")


    if project["verilog_defines"]:
        verilog_defines = []
        for key, value in project["verilog_defines"].items():
            verilog_defines.append(f"`define {key} {value}")
        verilog_defines.append(f"")
        open(f"{project['SOURCE_PATH']}/defines.v", "w").write("\n".join(verilog_defines))
        project["verilog_files"].append("defines.v")

    if project["firmware_extrafiles"]:
        for filename, content in project["firmware_extrafiles"].items():
            open(f"{project['SOURCE_PATH']}/{filename}", "w").write(content)


    for plugin in project["plugins"]:
        if hasattr(project["plugins"][plugin], "ips"):
            for ipv in project["plugins"][plugin].ips():
                ipv_name = ipv.split("/")[-1]
                if ipv.endswith((".v", ".sv")):
                    project["verilog_files"].append(ipv_name)
                ipv_path = f"plugins/{plugin}/{ipv}"
                if not os.path.isfile(ipv_path):
                    ipv_path = f"generators/firmware/{ipv}"
                os.system(
                    f"cp -a {ipv_path} {project['SOURCE_PATH']}/{ipv_name}"
                )
                """
                if ipv.endswith(".v") and not ipv.startswith("PLL_"):
                    os.system(
                        f"which verilator >/dev/null && cd {project['SOURCE_PATH']} && verilator --lint-only {ipv}"
                    )
                """

    print(f"generating files in {project['OUTPUT_PATH']}")

    for generator in project["generators"].values():
        generator.generate(project)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "configfile", help="json config file", type=str, nargs="?", default=None
    )
    parser.add_argument(
        "outputdir", help="output directory", type=str, nargs="?", default=None
    )
    args = parser.parse_args()

    main(args.configfile, args.outputdir)
