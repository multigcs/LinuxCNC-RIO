
def testbench(project):
    # experimental/uncompleted testbench generator
    top_arguments = []

    for pname in sorted(list(project["pinlists"])):
        pins = project["pinlists"][pname]
        for pin in pins:
            if pin[1].startswith("EXPANSION"):
                continue
            top_arguments.append(f"{pin[2].lower()} {pin[0]}")

    testb_data = []
    testb_data.append("`timescale 1ns/100ps")
    testb_data.append("")
    testb_data.append("module testb;")
    testb_data.append("")

    for arg in top_arguments:
        arg_dir = arg.split()[0]
        arg_name = arg.split()[1]
        if arg_dir == "input":
            testb_data.append(f"    reg {arg_name} = 0;")

    testb_data.append("")
    for arg in top_arguments:
        arg_dir = arg.split()[0]
        arg_name = arg.split()[1]
        if arg_dir == "output":
            testb_data.append(f"    wire {arg_name};")

    testb_data.append("")
    testb_data.append("    always #2 sysclk = !sysclk;")
    testb_data.append("")
    testb_data.append("    initial begin")
    testb_data.append('        $dumpfile("testb.vcd");')

    for anum, arg in enumerate(top_arguments):
        arg_dir = arg.split()[0]
        arg_name = arg.split()[1]

        testb_data.append(f"        $dumpvars({anum}, {arg_name});")

    testb_data.append("")
    testb_data.append("        # 100000 $finish;")
    testb_data.append("    end")
    testb_data.append("")
    testb_data.append("    rio rio1 (")

    alen = len(top_arguments)
    for anum, arg in enumerate(top_arguments):
        arg_dir = arg.split()[0]
        arg_name = arg.split()[1]
        if anum == alen - 1:
            testb_data.append(f"        .{arg_name} ({arg_name})")
        else:
            testb_data.append(f"        .{arg_name} ({arg_name}),")
    testb_data.append("    );")
    testb_data.append("")
    testb_data.append("endmodule")
    testb_data.append("")

    open(f"{project['SOURCE_PATH']}/testb.v", "w").write("\n".join(testb_data))
