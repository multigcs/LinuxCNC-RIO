#!/usr/bin/env python3
#
#

import argparse
import os
import projectLoader

parser = argparse.ArgumentParser()
parser.add_argument(
    "configfile", help="json config file", type=str, nargs="?", default=None
)
parser.add_argument(
    "outputdir", help="output directory", type=str, nargs="?", default=None
)
args = parser.parse_args()


project = projectLoader.load(args.configfile)


# file structure
if args.outputdir:
    project["OUTPUT_PATH"] = args.outputdir
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


for plugin in project["plugins"]:
    if hasattr(project["plugins"][plugin], "ips"):
        for ipv in project["plugins"][plugin].ips():
            project["verilog_files"].append(ipv)
            # os.system(f"verilator --lint-only -Wall plugins/{plugin}/{ipv}")
            os.system(
                f"which verilator >/dev/null && verilator --lint-only plugins/{plugin}/{ipv}"
            )
            os.system(f"cp -a plugins/{plugin}/{ipv} {project['SOURCE_PATH']}/{ipv}")

print(f"generating files in {project['OUTPUT_PATH']}")


for generator in project["generators"].values():
    generator.generate(project)
