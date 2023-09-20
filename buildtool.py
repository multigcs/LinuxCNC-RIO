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

    for plugin in project["plugins"]:
        if hasattr(project["plugins"][plugin], "ips"):
            for ipv in project["plugins"][plugin].ips():
                project["verilog_files"].append(ipv)
                ipv_path = f"plugins/{plugin}/{ipv}"
                if not os.path.isfile(ipv_path):
                    ipv_path = f"generators/firmware/{ipv}"
                os.system(
                    f"cp -a {ipv_path} {project['SOURCE_PATH']}/{ipv}"
                )
                os.system(
                    f"which verilator >/dev/null && cd {project['SOURCE_PATH']} && verilator --lint-only {ipv}"
                )

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
