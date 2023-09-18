
import os
from buildtool import main


def test_generator():
    name = "tangnano9k_1"

    configfile = f"tests/data/{name}/config.json"
    #testfiles = ("Firmware/rio.v", "LinuxCNC/Components/rio.h", "LinuxCNC/ConfigSamples/rio/rio.hal", "LinuxCNC/ConfigSamples/rio/rio.ini")
    testfiles = ("LinuxCNC/Components/rio.h", "LinuxCNC/ConfigSamples/rio/rio.hal", "LinuxCNC/ConfigSamples/rio/rio.ini")
    outputdir = f"tests/Output/{name}"
    osscadsuitePath = "/opt/oss-cad-suite/bin"

    os.system(f"rm -rf {outputdir}")
    main(configfile, outputdir)

    for testfile in testfiles:
        generated = f"tests/Output/{name}/{testfile}"
        expected = f"tests/data/{name}/{testfile.split('/')[-1]}"
        print(f"# diff {expected} {generated}") 
        assert os.system(f"diff {expected} {generated}") == 0

    #assert os.system(f"cd {outputdir}/Firmware ; PATH=$PATH:{osscadsuitePath} make all") == 0
