import importlib
import glob
import os
import time
from struct import *
import json
import sys
from copy import deepcopy
from functools import partial
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QApplication,
    QListWidget,
    QGridLayout,
    QLabel,
    QSlider,
    QCheckBox,
    QComboBox,
    QLineEdit,
    QSpinBox,
)
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtGui import QFont

jdata = json.loads(open(sys.argv[1], "r").read())


print("family:", jdata["family"])
print("type:",   jdata["type"])
print("package", jdata["package"])

pinlist = {"": "IO"}

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



class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("RIO-Setup")
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.load()

    def load(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)

        self.layout_row = 0
        self.layout_col = 0

        for section in [
            "interface",
            "expansion",
            "joints",
            "vout",
            "vin",
            "dout",
            "din",
        ]:
            # print(section)
            label = QLabel(section.title())
            # label.setStyleSheet("border: 1px solid black;")
            label.setStyleSheet("font-weight: bold")

            self.layout.addWidget(label, self.layout_row, self.layout_col)
            self.layout_row += 1
            self.layout_col += 1

            if section in jdata:
                for num, entry in enumerate(jdata[section]):
                    plugin_name = "???"
                    etype = entry.get("type", "base")
                    description = f"Type: {etype}"
                    pin = entry.get("pin")
                    if pin:
                        description += f" (pin:{pin})"
                    else:
                        pins = entry.get("pins", {})
                        if isinstance(pins, dict):
                            pin = pins.get("step")
                            if pin:
                                description += f" (step:{pin})"
                            pin = pins.get("pwm")
                            if pin:
                                description += f" (pwm:{pin})"

                    for plugin in plugins:
                        if hasattr(plugins[plugin], "types"):
                            if etype in plugins[plugin].types():
                                plugin_name = plugin
                                if hasattr(plugins[plugin], "entry_info"):
                                    description = plugins[plugin].entry_info(entry)

                    # self.layout.addWidget(QLabel(plugin_name), self.layout_row, self.layout_col)
                    self.layout.addWidget(
                        QLabel(description), self.layout_row, self.layout_col
                    )

                    editbutton = QPushButton("edit")
                    self.layout.addWidget(
                        editbutton, self.layout_row, self.layout_col + 1
                    )
                    editbutton.clicked.connect(partial(self.edit_callback, section, num))


                    delbutton = QPushButton("del")
                    self.layout.addWidget(
                        delbutton, self.layout_row, self.layout_col + 2
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
        self.layout.addWidget(exitbutton, self.layout_row, self.layout_col)

        savebutton = QPushButton("Save")
        savebutton.clicked.connect(self.save_callback)
        self.layout.addWidget(savebutton, self.layout_row, self.layout_col + 3)


    def exit_callback(self):
        exit(0)

    def save_callback(self):
        print("############################################################")
        print(json.dumps(jdata, indent=4))
        print("############################################################")


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
            elif option["type"] == "int":
                default = int(option.get("default", 0))
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
        self.edit.show()

    def edit_callback(self, section, num):
        self.edit = EditAdd(section, num, self)
        self.edit.show()

    def del_callback(self, section, num):
        del jdata[section][num]
        self.load()




class EditAdd(QWidget):
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
                data[name] = self.widgets[f"{dpath}/{name}"].currentText()
            elif option["type"] == "output":
                data[name] = self.widgets[f"{dpath}/{name}"].currentText()
            elif option["type"] == "int":
                data[name] = self.widgets[f"{dpath}/{name}"].value()
            else:
                data[name] = self.widgets[f"{dpath}/{name}"].getText()


    def cancel_callback(self):
        self.close()
        self.gui.load()


    def save_callback(self):
        self.save_setup_options(setup_data[self.section][self.subtype], jdata[self.section][self.num])
        print("############################################################")
        #print(jdata[self.section][self.num])
        print(json.dumps(jdata, indent=4))
        print("############################################################")
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
