
import argparse

import pprint
import re


patternModule = re.compile(r"module\s+(?P<name>\w+)(?P<params>\s*#\([^\)]*\))?\s\((?P<args>[^\)]*)\)\s*;(?P<data>[\s\S]*?(?=endmodule))endmodule")
patternParam = re.compile(r"parameter(?P<type>\s+[a-zA-Z]+)?(?P<size>\s*\[.*\])?(?P<name>\s+\w+)\s+(?P<default>=.*)")
patternArg = re.compile(r"(?P<dir>output|input|inout)?(?P<type>\s+reg|wire)?(?P<size>\s\[[^\]]*\])?(?P<name>\s\w+)")


parser = argparse.ArgumentParser()
parser.add_argument(
    "verilog", help="verilog file", type=str, default=None
)
args = parser.parse_args()

verilogData = open(args.verilog, "r").read()

verilogData = re.sub(r"//.*", "", verilogData)
#verilogData = re.sub(r"`(if|else|end|def).*", "", verilogData)
verilogData = re.sub(r"/\*.*\*/", "", verilogData)

modules = {}

for result in patternModule.finditer(verilogData):
    moduleName = result.group("name")
    moduleData = result.group("data")
    modules[moduleName] = {
        "args": {},
        "params": {},
        "data": moduleData,
    }
    
    defines = []
    
    moduleArgs = []
    moduleArgLast = {}
    
    args = []
    for arg in result.group("args").split("\n"):
        #print(arg)
        if arg.startswith("`"):
            args.append(f"{arg},")
        else:
            args.append(arg)

    for arg in ' '.join(args).split(","):
        moduleArg = {}
        if not arg:
            continue

        arg = re.sub(r"\s+", " ", arg.strip())
        
        if arg.startswith("`"):
            if arg.startswith("`ifndef"):
                defines.append(arg)
            elif arg.startswith("`ifdef"):
                defines.append(arg)
            elif arg.startswith("`endif"):
                defines.pop()
        else:

            moduleArg["defines"] = defines.copy()

            argm = patternArg.search(arg)
            if argm:
                if argm["dir"]:
                    moduleArg["direction"] = argm["dir"]
                if argm["type"]:
                    moduleArg["type"] = argm["type"]
                if argm["size"]:
                    moduleArg["size"] = argm["size"]
                if argm["name"]:
                    moduleArg["name"] = argm["name"]
                modules[moduleName]["args"][moduleArg["name"]] = moduleArg
                moduleArgLast = moduleArg
            elif len(arg.strip().split()) == 1:
                moduleArg = moduleArgLast.copy()
                moduleArg["name"] = arg.strip()
                modules[moduleName]["args"][moduleArg["name"]] = moduleArg
            else:
                print(f"UNKNOWN ARG ({moduleName}): {arg.strip()}")

    if result.group("params"):
        for arg in result.group("params").strip().lstrip("#").lstrip("(").rstrip(")").split(","):
            param = patternParam.search(arg.strip())
            if param:
                moduleParam = {}
                moduleParam["name"] = param["name"].strip()
                if param["type"]:
                    moduleParam["size"] = param["type"].strip().replace(" ", "")
                if param["size"]:
                    moduleParam["size"] = param["size"].strip().replace(" ", "")
                if param["default"]:
                    moduleParam["default"] = param["default"].strip().lstrip("=").strip().replace(" ", "").replace("_", "")

                modules[moduleName]["params"][moduleParam["name"]] = moduleParam
            else:
                print(f"UNKNOWN PARAMETER ({moduleName}): {arg.strip()}")



    for arg in result.group("data").split(";"):
        param = patternParam.search(arg.strip())
        if param:
            moduleParam = {}
            moduleParam["name"] = param["name"].strip()
            if param["type"]:
                moduleParam["size"] = param["type"].strip().replace(" ", "")
            if param["size"]:
                moduleParam["size"] = param["size"].strip().replace(" ", "")
            if param["default"]:
                moduleParam["default"] = param["default"].strip().lstrip("=").strip().replace(" ", "").replace("_", "")

            modules[moduleName]["params"][moduleParam["name"]] = moduleParam



#exit(0)

output = "html"

if output == "markdown":
    for moduleName, module in modules.items():
        print(f"# {moduleName}")
        print("")

        print("## arguments")
        print("")
        print("| direction | type | size | name |")
        print("| --- | --- | --- | --- |")
        for argName, arg in module["args"].items():
            print(f"| {arg.get('direction', '')} | {arg.get('type', '')} | {arg.get('size', '')} | {argName} | {arg.get('defines') or ''} |")
        print("")

        if module["params"]:
            print("## parameter")
            print("")
            print("| size | name | default |")
            print("| --- | --- | --- |")
            for argName, arg in module["params"].items():
                print(f"| {arg.get('size', '')} | {arg.get('name', '')} | {arg.get('default', '')} |")
            print("")

else:

    print("""
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>

    """)

    for moduleName, module in modules.items():
        print(f"<h2>{moduleName}</h2>")
        print(f"<hr/>")

        print("<h3>arguments</h3>")
        print("<table>")
        print("<tr><th>direction</th><th>type</th><th>size</th><th>name</th></tr>")
        for argName, arg in module["args"].items():
            print(f"<tr><td>{arg.get('direction', '')}</td><td>{arg.get('type', '')}</td><td>{arg.get('size', '')}</td><td>{argName}</td><td>{arg.get('defines') or ''}</td></tr>")
        print("</table>")

        print("<br>")

        if module["params"]:
            print("<table>")
            print("<h3>parameter</h3>")
            print("<tr><th>size</th><th>name</th><th>default</th></tr>")
            for argName, arg in module["params"].items():
                print(f"<tr><td>{arg.get('size', '')}</td><td>{arg.get('name', '')}</td><td>{arg.get('default', '')}</td></tr>")
            print("</table>")
            print("<br>")

        print("<pre>")
        print(module["data"])
        print("</pre>")











