from .verilog2doc import verilog2doc


def generate(project):
    print("generating documentation")
    try:
        verilogs = []
        for verlog in project["verilog_files"]:
            verilogs.append(f"{project['GATEWARE_PATH']}/{verlog}")
        verilogs.append(f"{project['GATEWARE_PATH']}/rio.v")

        verilog2doc(
            verilogs, top="rio", output=f"{project['OUTPUT_PATH']}/Documentation"
        )
    except Exception as error:
        print(f"# can't generate documentation: {error}")
