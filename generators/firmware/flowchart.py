try:
    import graphviz
    do_graphviz = True
except Exception:
    do_graphviz = False


def flowchart(project):
    if not do_graphviz:
        return

    g = graphviz.Digraph('G', filename=f"{project['SOURCE_PATH']}/flowchart.gv")
    g.attr(rankdir='LR')

    label = f"<<table BORDER='0' CELLBORDER='1' CELLSPACING='0'>"
    label += f"<tr><td>name</td><td>pin</td><td>dir</td></tr>"

    pindirs = {}
    for pname in sorted(list(project["pinlists"])):
        pins = project["pinlists"][pname]
        for pin in pins:
            label += f"<tr><td>{pin[0]}</td><td>{pin[1]}</td><td PORT=\"{pin[1]}\">{pin[2]}</td></tr>"
            pindirs[pin[1]] = pin[2]

    label += f"</table>>"
    g.node(f"pins", shape='plaintext', label=label)

    uniqParts = {}
    for ptype in {"jointnames", "voutnames", "vinnames", "doutnames", "dinnames"}:
        if project[ptype]:
            for data in project[ptype]:
                pid = data.get('pid') or data.get('_name')
                if pid not in uniqParts:
                    uniqParts[pid] = []
                uniqParts[pid].append(data)


    label = f"<<table BORDER='0' CELLBORDER='1' CELLSPACING='0'>"
    label += f"<tr><td>name</td><td>hal</td></tr>"
    for pid, datalist in uniqParts.items():
        data = datalist[0]
        for ndata in datalist:
            if net := ndata.get("net"):
                label += f"<tr><td PORT=\"{net}\">net</td><td>{net}</td></tr>"
            else:
                label += f"<tr><td PORT=\"rio.{ndata['_name']}\">signal</td><td>rio.{ndata['_name']}</td></tr>"
    label += f"</table>>"
    g.node("hal", shape='plaintext', label=label)


    for pid, datalist in uniqParts.items():
        data = datalist[0]
        label = f"<<table BORDER='0' CELLBORDER='1' CELLSPACING='0'>"


        label += f"<tr><td>plugin</td><td>{data['type']}</td></tr>"
        for ndata in datalist:
            label += f"<tr><td>name</td><td PORT=\"{ndata['_name']}\">{ndata['_name']}</td></tr>"
            if net := ndata.get("net"):
                g.edge(f"{pid}:{ndata['_name']}", f"hal:{net}")
            else:
                g.edge(f"{pid}:{ndata['_name']}", f"hal:rio.{ndata['_name']}")

        if "pin" in data:
            pin = data["pin"]
            label += f"<tr><td PORT=\"{pin}\">pin</td><td>{pin}</td></tr>"

            pindir = pindirs.get(pin)
            if pindir == "OUTPUT":
                g.edge(f"pins:{pin}", f"{pid}:{pin}", dir="back")
            elif pindir == "INOUT":
                g.edge(f"pins:{pin}", f"{pid}:{pin}", dir="both")
            else:
                g.edge(f"pins:{pin}", f"{pid}:{pin}", dir="forward")


        elif "pins" in data:
            for pname, pin in data["pins"].items():
                label += f"<tr><td PORT=\"{pin}\">pin-{pname}</td><td>{pin}</td></tr>"
                pindir = pindirs.get(pin)
                if pindir == "OUTPUT":
                    g.edge(f"pins:{pin}", f"{pid}:{pin}", dir="back")
                elif pindir == "INOUT":
                    g.edge(f"pins:{pin}", f"{pid}:{pin}", dir="both")
                else:
                    g.edge(f"pins:{pin}", f"{pid}:{pin}", dir="forward")
        label += f"</table>>"
        g.node(pid, shape='plaintext', label=label, href=f"https://github.com/multigcs/LinuxCNC-RIO/tree/main/plugins/{data['type']}")

    g.view()
