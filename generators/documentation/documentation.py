
from .verilog2doc import verilog2doc

def generate(project):
    print("generating documentation")
    
    verilogs = []
    for verlog in project["verilog_files"]:
        verilogs.append(f"{project['FIRMWARE_PATH']}/{verlog}")
    verilogs.append(f"{project['FIRMWARE_PATH']}/rio.v")
    
    verilog2doc(verilogs, top="rio", output=f"{project['OUTPUT_PATH']}/Documentation")

