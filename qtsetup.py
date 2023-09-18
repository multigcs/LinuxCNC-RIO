#!/usr/bin/env python3
#
#

import argparse
import glob
import importlib
import json
import os
import signal
import sys
import time
from copy import deepcopy
from functools import partial
from struct import *

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (
    QPlainTextEdit,
    QApplication,
    QTabWidget,
    QCheckBox,
    QComboBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QSlider,
    QSpinBox,
    QWidget,
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "configfile", help="json config file", type=str, default=None
)

args = parser.parse_args()

config_dir = "/".join(args.configfile.split("/")[:-1])
print(f"loading json config: {args.configfile}")
jdata = json.loads(open(args.configfile, "r").read())
if "plugins" not in jdata:
    print("ERROR: old json config format, please run 'python3 convert-configs.py'")
    sys.exit(1)


print("family:", jdata["family"])
print("type:", jdata["type"])
print("package", jdata["package"])

pinlist = {"": "IO"}
dsourcelist = [
    "spindle.0.on",
    "spindle.1.on",
]
dtargetlist = [
    "joint.0.home-sw-in",
    "joint.1.home-sw-in",
    "joint.2.home-sw-in",
    "joint.3.home-sw-in",
    "joint.4.home-sw-in",
    "joint.5.home-sw-in",
    "motion.probe-input",
]
vsourcelist = [
    "spindle.0.speed-out",
    "spindle.1.speed-out",
]
vtargetlist = [
    "halui.feed-override",
    "halui.rapid-override",
    "halui.spindle.0.override",
    "halui.spindle.1.override",
]

outputfiles = {
    "qtsetup-temp.json": "/tmp/qtsetup-temp.json",
    "rio.ini": "/tmp/qtsetup-temp/LinuxCNC/ConfigSamples/rio/rio.ini",
    "rio.hal": "/tmp/qtsetup-temp/LinuxCNC/ConfigSamples/rio/rio.hal",
    "custom_postgui.hal": "/tmp/qtsetup-temp/LinuxCNC/ConfigSamples/rio/custom_postgui.hal",
    "rio-gui.xml": "/tmp/qtsetup-temp/LinuxCNC/ConfigSamples/rio/rio-gui.xml",
    "rio.h": "/tmp/qtsetup-temp/LinuxCNC/Components/rio.h",
}

if os.path.isfile(f"chipdata/{jdata['family']}.json"):
    chiptype_mapping = {
        "25k": "LFE5U-25F",
        "up5k": "5k",
        "hx1k": "1k",
        "hx4k": "4k",
        "hx8k": "8k",
    }
    print("try to load chipdata")
    chipdata = json.loads(open(f"chipdata/{jdata['family']}.json").read())
    ctype = chiptype_mapping.get(jdata["type"], jdata["type"])
    package = jdata["package"]
    if ctype in chipdata:
        print(" type found:", ctype)
        if package in chipdata[ctype]:
            print(" package found:", package)
            for pin in chipdata[ctype][package]:
                pinlist[pin] = "IO"
        else:
            print(" package not found:", package)
    else:
        print(" type not found:", ctype)


plugins = {}
for path in glob.glob("plugins/*"):
    plugin = path.split("/")[1]
    if os.path.isfile(f"plugins/{plugin}/plugin.py"):
        vplugin = importlib.import_module(".plugin", f"plugins.{plugin}")
        plugins[plugin] = vplugin.Plugin(jdata)


setup_data = {}
for plugin in plugins:
    if hasattr(plugins[plugin], "pinlist"):
        for pins in plugins[plugin].pinlist():
            if not pins[1].startswith("EXPANSION"):
                pinlist[pins[1]] = "IO"

    if hasattr(plugins[plugin], "setup"):
        setups = plugins[plugin].setup()
        for setup in setups:
            subtype = setup["subtype"]
            basetype = setup["basetype"]
            if basetype not in {"interface", "expansion"}:
                basetype = "plugins"
            if basetype not in setup_data:
                setup_data[basetype] = {}
            setup_data[basetype][subtype] = setup["options"]

    if hasattr(plugins[plugin], "expansions"):
        expansions = plugins[plugin].expansions()
        for name, bits in expansions.items():
            if name.endswith("OUTPUT"):
                for bit in range(bits):
                    pinlist[f"{name}[{bit}]"] = "OUTPUT"
            else:
                for bit in range(bits):
                    pinlist[f"{name}[{bit}]"] = "INPUT"


setup_data["clock"] = {
    "speed": {
        "type": "int",
        "name": "clock speed",
    },
    "pin": {
        "type": "input",
        "name": "clock pin",
    },
}


os.system("rm -rf /tmp/qtsetup-temp.json /tmp/qtsetup-temp")
open("/tmp/qtsetup-temp.json", "w").write(json.dumps(jdata, indent=4))
os.system("python3 buildtool.py /tmp/qtsetup-temp.json /tmp/qtsetup-temp")


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("RIO-Setup")
        self.layoutMain = QGridLayout()
        self.setLayout(self.layoutMain)
        self.resize(1600, 600)
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.load()

    def load(self):
        for i in reversed(range(self.layoutMain.count())):
            self.layoutMain.itemAt(i).widget().setParent(None)

        label = QLabel("!!! work in progress !!!")
        label.setStyleSheet("border: 1px solid red;")
        self.layoutMain.addWidget(label, 0, 0)
        label = QLabel("!!! please edit your config by hand !!!")
        label.setStyleSheet("border: 1px solid red;")
        self.layoutMain.addWidget(label, 1, 0)


        tabwidgetR = QTabWidget()
        self.layoutMain.addWidget(tabwidgetR, 2, 1)

        if "images" in jdata:
            for name, image in jdata["images"].items():
                ifile = f"{config_dir}/{image}"
                img = QLabel()
                pixmap = QPixmap(ifile)
                pixmapResized = pixmap.scaledToHeight(600)
                img.setPixmap(pixmapResized)
                tabwidgetR.addTab(img, name)

        else:
            for ifile in glob.glob(f"{config_dir}/*.png") + glob.glob(f"{config_dir}/*.jpg"):
                img = QLabel()
                pixmap = QPixmap(ifile)
                pixmapResized = pixmap.scaledToHeight(600)
                img.setPixmap(pixmapResized)
                tabwidgetR.addTab(img, ifile.split("/")[-1].split(".")[0])


        self.preview = {}
        for filename, filepath in outputfiles.items():
            self.preview[filename] = QPlainTextEdit(self)
            self.preview[filename].setReadOnly(True)
            tabwidgetR.addTab(self.preview[filename], filename)
            fdata = open(filepath, "r").read()
            self.preview[filename].setPlainText(fdata)


        tabwidget = QTabWidget()
        self.layoutMain.addWidget(tabwidget, 2, 0)

        for section in [
            "plugins",
            "expansion",
            "interface",
        ]:

            sectionWidgets = QWidget()
            tabwidget.addTab(sectionWidgets, section.title())

            self.layout = QGridLayout()
            sectionWidgets.setLayout(self.layout)

            self.layout_row = 0
            self.layout_col = 0

            if section in jdata:
                for num, entry in enumerate(jdata[section]):
                    plugin_name = "???"
                    etype = entry.get("type", "???")
                    description = ""
                    pinlist = []

                    name = entry.get("name", "-")

                    pin = entry.get("pin")
                    if pin:
                        pinlist.append(pin)
                    else:
                        pins = entry.get("pins", {})
                        if isinstance(pins, dict):
                            for pname, pin in pins.items():
                                pinlist.append(f"{pname}:{pin}")

                    for plugin in plugins:
                        if hasattr(plugins[plugin], "types"):
                            if etype in plugins[plugin].types():
                                plugin_name = plugin
                                if hasattr(plugins[plugin], "entry_info"):
                                    description = plugins[plugin].entry_info(entry)

                    self.layout.addWidget(
                        QLabel(name), self.layout_row, self.layout_col
                    )
                    self.layout.addWidget(
                        QLabel(etype), self.layout_row, self.layout_col + 1
                    )
                    self.layout.addWidget(
                        QLabel(','.join(pinlist)), self.layout_row, self.layout_col + 2
                    )

                    editbutton = QPushButton("edit")
                    self.layout.addWidget(
                        editbutton, self.layout_row, self.layout_col + 3
                    )
                    editbutton.clicked.connect(
                        partial(self.edit_callback, section, num)
                    )

                    delbutton = QPushButton("del")
                    self.layout.addWidget(
                        delbutton, self.layout_row, self.layout_col + 4
                    )
                    delbutton.clicked.connect(partial(self.del_callback, section, num))

                    self.layout_row += 1

            combo = QComboBox()
            for subtype in setup_data[section]:
                combo.addItem(subtype)
            addbutton = QPushButton("add")
            addbutton.clicked.connect(partial(self.add_callback, section, combo))

            self.layout.addWidget(combo, self.layout_row, self.layout_col + 1)
            self.layout.addWidget(addbutton, self.layout_row, self.layout_col + 2)
            self.layout_row += 1
            self.layout_col -= 1

        exitbutton = QPushButton("Exit")
        exitbutton.clicked.connect(self.exit_callback)
        self.layoutMain.addWidget(exitbutton, 3, 0)

        savebutton = QPushButton("Save")
        savebutton.clicked.connect(self.save_callback)
        self.layoutMain.addWidget(savebutton, 3, 1)

    def exit_callback(self):
        exit(0)

    def save_callback(self):
        print("############################################################")
        print(json.dumps(jdata, indent=4))
        print("############################################################")
        open(args.configfile, "w").write(json.dumps(jdata, indent=4))

    def add_setup_options(self, options, data, dpath=""):
        for name, option in options.items():
            if option["type"] == "dict":
                data[name] = {}
                value = data[name]
                self.add_setup_options(option["options"], value, f"{dpath}/{name}")
            elif option["type"] == "bool":
                default = option.get("default", False)
                data[name] = default
            elif option["type"] == "input":
                default = option.get("default", "")
                data[name] = default
            elif option["type"] == "output":
                default = option.get("default", "")
                data[name] = default
            elif option["type"] == "inout":
                default = option.get("default", "")
                data[name] = default
            elif option["type"] == "int":
                default = int(option.get("default", 0))
                data[name] = default
            elif option["type"] == "dtarget":
                default = option.get("default", "")
                data[name] = default
            elif option["type"] == "dsource":
                default = option.get("default", "")
                data[name] = default
            elif option["type"] == "vtarget":
                default = option.get("default", "")
                data[name] = default
            elif option["type"] == "vsource":
                default = option.get("default", "")
                data[name] = default
            else:
                default = option.get("default", "")
                data[name] = default

    def add_callback(self, section, combo):
        num = 0

        if section in jdata:
            num = len(jdata[section])
        else:
            jdata[section] = []

        subtype = combo.currentText()

        jdata[section].append({"type": subtype})
        self.add_setup_options(setup_data[section][subtype], jdata[section][num])

        self.edit = EditAdd(section, num, self)
        self.edit.added = True
        self.edit.show()

    def edit_callback(self, section, num):
        self.edit = EditAdd(section, num, self)
        self.edit.show()

    def del_callback(self, section, num):
        del jdata[section][num]
        self.load()


class EditAdd(QWidget):
    added = False

    def __init__(self, section, num, gui, parent=None):
        super(EditAdd, self).__init__(parent)

        self.setFixedWidth(600)

        self.gui = gui
        self.section = section
        self.num = num
        self.widgets = {}

        self.setWindowTitle(f"Edit ({section}:{num})")
        self.layout = QGridLayout()
        self.layout_row = 0
        self.layout_col = 0
        self.setLayout(self.layout)

        self.subtype = jdata[section][num].get("type", "")
        self.layout.addWidget(QLabel(f"Type: {self.subtype}"), self.layout_row, 0)
        self.layout_row += 1
        self.gen_setup_options(setup_data[section][self.subtype], jdata[section][num])

        button = QPushButton("Save")
        button.clicked.connect(self.save_callback)
        self.layout.addWidget(button, self.layout_row, self.layout_col + 2)

        button = QPushButton("Cancel")
        button.clicked.connect(self.cancel_callback)
        self.layout.addWidget(button, self.layout_row, self.layout_col)

        self.layout_row += 1

    def save_setup_options(self, options, data, dpath=""):
        for name, option in options.items():
            if option["type"] == "dict":
                value = data.get(name)
                self.save_setup_options(option["options"], value, f"{dpath}/{name}")
            elif option["type"] == "bool":
                data[name] = self.widgets[f"{dpath}/{name}"].isChecked()
            elif option["type"] == "input":
                value = self.widgets[f"{dpath}/{name}"].currentText()
                if value:
                    data[name] = value
                elif name in data:
                    del data[name]
            elif option["type"] == "output":
                value = self.widgets[f"{dpath}/{name}"].currentText()
                if value:
                    data[name] = value
                elif name in data:
                    del data[name]
            elif option["type"] == "inout":
                value = self.widgets[f"{dpath}/{name}"].currentText()
                if value:
                    data[name] = value
                elif name in data:
                    del data[name]
            elif option["type"] == "int":
                data[name] = self.widgets[f"{dpath}/{name}"].value()
            elif option["type"] == "dtarget":
                value = self.widgets[f"{dpath}/{name}"].currentText()
                if value:
                    data[name] = value
                elif name in data:
                    del data[name]
            elif option["type"] == "dsource":
                value = self.widgets[f"{dpath}/{name}"].currentText()
                if value:
                    data[name] = value
                elif name in data:
                    del data[name]
            elif option["type"] == "vtarget":
                value = self.widgets[f"{dpath}/{name}"].currentText()
                if value:
                    data[name] = value
                elif name in data:
                    del data[name]
            elif option["type"] == "vsource":
                value = self.widgets[f"{dpath}/{name}"].currentText()
                if value:
                    data[name] = value
                elif name in data:
                    del data[name]
            else:
                value = self.widgets[f"{dpath}/{name}"].text()
                if value:
                    data[name] = value
                elif name in data:
                    del data[name]

    def cancel_callback(self):
        if self.added:
            jdata[self.section].pop()
        self.close()
        self.gui.load()

    def save_callback(self):
        self.save_setup_options(
            setup_data[self.section][self.subtype], jdata[self.section][self.num]
        )
        print("############################################################")
        print(json.dumps(jdata, indent=4))
        print("############################################################")

        # update prefiew files
        os.system("rm -rf /tmp/qtsetup-temp.json /tmp/qtsetup-temp")
        open("/tmp/qtsetup-temp.json", "w").write(json.dumps(jdata, indent=4))
        os.system("python3 buildtool.py /tmp/qtsetup-temp.json /tmp/qtsetup-temp")

        self.close()
        self.gui.load()


    def gen_setup_options(self, options, data, dpath=""):
        for name, option in options.items():
            label = option.get("name", name)
            if name != label:
                label = f"{label} ({name})"
            tooltip = option.get("comment", label)
            if option["type"] == "dict":
                value = data.get(name, {})
                label = QLabel(label)
                label.setStyleSheet("font-weight: bold")
                self.layout.addWidget(label, self.layout_row, self.layout_col)
                self.layout_row += 1
                self.layout_col += 1
                self.gen_setup_options(option["options"], value, f"{dpath}/{name}")
                self.layout_col -= 1

            elif option["type"] == "bool":
                value = data.get(name, False)
                self.layout.addWidget(QLabel(label), self.layout_row, self.layout_col)
                tedit = QCheckBox()
                tedit.setChecked(value)
                self.widgets[f"{dpath}/{name}"] = tedit
                self.widgets[f"{dpath}/{name}"].setToolTip(tooltip)
                self.layout.addWidget(tedit, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "input":
                value = str(data.get(name, ""))
                self.layout.addWidget(QLabel(label), self.layout_row, self.layout_col)
                combo = QComboBox()
                for pin, pdir in pinlist.items():
                    if pdir in ["INPUT", "IO"]:
                        combo.addItem(pin)
                combo.setEditable(True)
                combo.setCurrentText(value)
                self.widgets[f"{dpath}/{name}"] = combo
                self.widgets[f"{dpath}/{name}"].setToolTip(tooltip)
                self.layout.addWidget(combo, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "output":
                value = str(data.get(name, ""))
                self.layout.addWidget(QLabel(label), self.layout_row, self.layout_col)
                combo = QComboBox()
                for pin, pdir in pinlist.items():
                    if pdir in ["OUTPUT", "IO"]:
                        combo.addItem(pin)
                combo.setEditable(True)
                combo.setCurrentText(value)
                self.widgets[f"{dpath}/{name}"] = combo
                self.widgets[f"{dpath}/{name}"].setToolTip(tooltip)
                self.layout.addWidget(combo, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "inout":
                value = str(data.get(name, ""))
                self.layout.addWidget(QLabel(label), self.layout_row, self.layout_col)
                combo = QComboBox()
                for pin, pdir in pinlist.items():
                    if pdir in ["IO"]:
                        combo.addItem(pin)
                combo.setEditable(True)
                combo.setCurrentText(value)
                self.widgets[f"{dpath}/{name}"] = combo
                self.widgets[f"{dpath}/{name}"].setToolTip(tooltip)
                self.layout.addWidget(combo, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "int":
                value = int(data.get(name, 0))
                self.layout.addWidget(QLabel(label), self.layout_row, self.layout_col)
                spinbox = QSpinBox()
                spinbox.setSingleStep(1)
                spinbox.setMinimum(-900000000)
                spinbox.setMaximum(900000000)
                spinbox.setValue(value)
                self.widgets[f"{dpath}/{name}"] = spinbox
                self.widgets[f"{dpath}/{name}"].setToolTip(tooltip)
                self.layout.addWidget(spinbox, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "dtarget":
                value = str(data.get(name, ""))
                self.layout.addWidget(QLabel(label), self.layout_row, self.layout_col)
                combo = QComboBox()
                for option in dtargetlist:
                    combo.addItem(option)
                combo.setEditable(True)
                combo.setCurrentText(value)
                self.widgets[f"{dpath}/{name}"] = combo
                self.widgets[f"{dpath}/{name}"].setToolTip(tooltip)
                self.layout.addWidget(combo, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "dsource":
                value = str(data.get(name, ""))
                self.layout.addWidget(QLabel(label), self.layout_row, self.layout_col)
                combo = QComboBox()
                for option in dsourcelist:
                    combo.addItem(option)
                combo.setEditable(True)
                combo.setCurrentText(value)
                self.widgets[f"{dpath}/{name}"] = combo
                self.widgets[f"{dpath}/{name}"].setToolTip(tooltip)
                self.layout.addWidget(combo, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "vtarget":
                value = str(data.get(name, ""))
                self.layout.addWidget(QLabel(label), self.layout_row, self.layout_col)
                combo = QComboBox()
                for option in vtargetlist:
                    combo.addItem(option)
                combo.setEditable(True)
                combo.setCurrentText(value)
                self.widgets[f"{dpath}/{name}"] = combo
                self.widgets[f"{dpath}/{name}"].setToolTip(tooltip)
                self.layout.addWidget(combo, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "vsource":
                value = str(data.get(name, ""))
                self.layout.addWidget(QLabel(label), self.layout_row, self.layout_col)
                combo = QComboBox()
                for option in vsourcelist:
                    combo.addItem(option)
                combo.setEditable(True)
                combo.setCurrentText(value)
                self.widgets[f"{dpath}/{name}"] = combo
                self.widgets[f"{dpath}/{name}"].setToolTip(tooltip)
                self.layout.addWidget(combo, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            else:
                value = str(data.get(name, ""))
                self.layout.addWidget(QLabel(label), self.layout_row, self.layout_col)
                tedit = QLineEdit()
                tedit.setText(value)
                self.widgets[f"{dpath}/{name}"] = tedit
                self.widgets[f"{dpath}/{name}"].setToolTip(tooltip)
                self.layout.addWidget(tedit, self.layout_row, self.layout_col + 1)
                self.layout_row += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()

    sys.exit(app.exec_())
