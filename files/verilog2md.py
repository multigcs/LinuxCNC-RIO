
import pprint
import re


patternModule = re.compile(r"module\s+(?P<name>\w+)(?P<params>\s*#\([^\)]*\))?\s\((?P<args>[^\)]*)\)\s*")
patternParam = re.compile(r"parameter(?P<size>\s*\[.*\])?\s+(?P<name>\w+)\s+(?P<default>=.*)")
patternArg = re.compile(r"(?P<dir>output|input|inout)?(?P<type>\s+reg|wire)?(?P<size>\s\[[^\]]*\])?(?P<name>\s\w+)")


verilogData = open("picorv32.v", "r").read()

verilogData = re.sub(
   r"//.*",
   "",
   verilogData
)

verilogData = re.sub(
   r"`(if|else|end|def).*",
   "",
   verilogData
)

verilogData = re.sub(
   r"/\*.*\*/",
   "",
   verilogData
)

modules = {}

for result in patternModule.finditer(verilogData):
    moduleName = result.group("name")
    modules[moduleName] = {"args": {}, "params": {}}
    
    moduleArgs = []
    for arg in result.group("args").split(","):
        moduleArg = {}
        if not arg:
            continue

        arg = re.sub(
           r"\s+",
           " ",
           arg
        )


        argm = patternArg.search(arg.strip())
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

    if result.group("params"):
        for arg in result.group("params").strip().lstrip("#").lstrip("(").rstrip(")").split(","):
            moduleParam = {}
            param = patternParam.search(arg)
            moduleParam["name"] = param["name"].strip()
            if param["size"]:
                moduleParam["size"] = param["size"].strip().replace(" ", "")
            if param["default"]:
                moduleParam["default"] = param["default"].strip().lstrip("=").strip().replace(" ", "").replace("_", "")

            modules[moduleName]["params"][moduleParam["name"]] = moduleParam


#exit(0)

for moduleName, module in modules.items():
    print(f"# {moduleName}")
    print("")

    print("## arguments")
    print("")
    print("| direction | type | size | name |")
    print("| --- | --- | --- | --- |")
    for argName, arg in module["args"].items():
        print(f"| {arg.get('direction', '')} | {arg.get('type', '')} | {arg.get('size', '')} | {argName} |")
    print("")


    print("## parameter")
    print("")
    print("| size | name | default |")
    print("| --- | --- | --- |")
    for argName, arg in module["params"].items():
        print(f"| {arg.get('size', '')} | {arg.get('name', '')} | {arg.get('default', '')} |")
    print("")













