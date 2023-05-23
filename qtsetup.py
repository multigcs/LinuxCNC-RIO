import importlib
import glob
import time
from struct import *
import json
import sys
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

pinlist = {}

plugins = {}
for path in glob.glob("plugins/*"):
    plugin = path.split("/")[1]
    vplugin = importlib.import_module(".plugin", f"plugins.{plugin}")
    plugins[plugin] = vplugin.Plugin(jdata)


for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for num in range(32):
        pinlist[f"{char}{num}"] = "IO"


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


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("Setup")
        self.layout = QGridLayout()
        self.layout_row = 0
        self.layout_col = 0
        self.setLayout(self.layout)

        for section in [
            "vout",
            "vin",
            "joints",
            "dout",
            "din",
            "interface",
            "expansion",
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
                    etype = entry.get("type", "")
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

                    editbutton.clicked.connect(partial(self.open_edit, section, num))
                    self.layout_row += 1

            self.layout.addWidget(
                QPushButton("add"), self.layout_row, self.layout_col + 1
            )
            self.layout_row += 1
            self.layout_col -= 1

    def open_edit(self, section, num):
        print("open edit", section, num)
        self.edit = EditAdd(section, num)
        self.edit.show()


class EditAdd(QWidget):
    def __init__(self, section, num, parent=None):
        super(EditAdd, self).__init__(parent)

        self.section = section
        self.num = num

        self.setWindowTitle(f"Edit ({section}:{num})")
        self.layout = QGridLayout()
        self.layout_row = 0
        self.layout_col = 0
        self.setLayout(self.layout)

        subtype = jdata[section][num].get("type", "")
        self.gen_setup_options(setup_data[section][subtype], jdata[section][num])

    def gen_setup_options(self, options, data):
        for name, option in options.items():
            if option["type"] == "dict":
                value = data.get(name, {})
                label = QLabel(name)
                label.setStyleSheet("font-weight: bold")
                self.layout.addWidget(label, self.layout_row, self.layout_col)
                self.layout_row += 1
                self.layout_col += 1
                self.gen_setup_options(option["options"], value)
                self.layout_col -= 1

            elif option["type"] == "bool":
                value = data.get(name, False)
                self.layout.addWidget(QLabel(name), self.layout_row, self.layout_col)
                tedit = QCheckBox()
                tedit.setChecked(value)
                self.layout.addWidget(tedit, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "input":
                value = str(data.get(name, ""))
                self.layout.addWidget(QLabel(name), self.layout_row, self.layout_col)
                combo = QComboBox()
                for pin, pdir in pinlist.items():
                    if pdir in ["INPUT", "IO"]:
                        combo.addItem(pin)
                combo.setEditable(True)
                combo.setCurrentText(value)
                self.layout.addWidget(combo, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "output":
                value = str(data.get(name, ""))
                self.layout.addWidget(QLabel(name), self.layout_row, self.layout_col)
                combo = QComboBox()
                for pin, pdir in pinlist.items():
                    if pdir in ["OUTPUT", "IO"]:
                        combo.addItem(pin)
                combo.setEditable(True)
                combo.setCurrentText(value)
                self.layout.addWidget(combo, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "int":
                value = int(data.get(name, 0))
                self.layout.addWidget(QLabel(name), self.layout_row, self.layout_col)
                spinbox = QSpinBox()
                spinbox.setSingleStep(1)
                spinbox.setMinimum(-900000000)
                spinbox.setMaximum(900000000)
                spinbox.setValue(value)
                self.layout.addWidget(spinbox, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            else:
                value = str(data.get(name, ""))
                self.layout.addWidget(QLabel(name), self.layout_row, self.layout_col)
                tedit = QLineEdit()
                tedit.setText(value)
                self.layout.addWidget(tedit, self.layout_row, self.layout_col + 1)
                self.layout_row += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()

    sys.exit(app.exec_())
