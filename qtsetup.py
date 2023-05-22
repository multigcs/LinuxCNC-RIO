
import importlib
import glob
import time
from struct import *
import json
import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel,QSlider,QCheckBox,QComboBox,QLineEdit
from PyQt5.QtCore import QTimer,QDateTime, Qt
from PyQt5.QtGui import QFont


plugins = {}
for path in glob.glob("plugins/*"):
    plugin = path.split("/")[1]
    vplugin = importlib.import_module(".plugin", f"plugins.{plugin}")
    plugins[plugin] = vplugin.Plugin({})


for plugin in plugins:
    print(plugin)
    #if hasattr(plugins[plugin], "pinlist"):
    #    plugins[plugin].info()


jdata = json.loads(open("configs/TinyFPGA-BX_BOB/config.json", "r").read())
#print(jdata)



data = {
    "basetype": "joint",
    "options": {
        "cl": {
            "type": "bool",
            "name": "closed loop",
        },
        "pins": {
            "type": "dict",
            "name": "pin config",
            "options": {
                "step": {
                    "type": "output",
                    "name": "stepper pin",
                },
                "dir": {
                    "type": "output",
                    "name": "dir pin",
                },
                "en": {
                    "type": "output",
                    "name": "enable pin",
                },
                "enc_a": {
                    "type": "input",
                    "name": "encoder A pin",
                },
                "enc_b": {
                    "type": "input",
                    "name": "encoder B pin",
                },
            },
        },

    },
}



class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('Setup')
        self.listFile=QListWidget()
        self.layout = QGridLayout()
        self.layout_row = 0
        self.layout_col = 0
        self.setLayout(self.layout)


        #combo = QComboBox()
        #combo.addItem("Apple")
        #combo.addItem("Pear")
        #combo.addItem("Lemon")
        #self.layout.addWidget(combo, 2, 0)
        #self.gen_setup_options(data["options"])
        

        for section in ["vout", "vin", "joints", "dout", "din"]:
            print(section)
            label = QLabel(section.title())
            #label.setStyleSheet("border: 1px solid black;")
            label.setStyleSheet("font-weight: bold")
            
            self.layout.addWidget(label, self.layout_row, self.layout_col)
            self.layout_row += 1
            self.layout_col += 1
            
            if section in jdata:
                for entry in jdata[section]:
                    print("##", entry)
                    
                    plugin_name = "???"
                    etype = entry.get("type", "---")
                    description = f"Type: {etype}"

                    for plugin in plugins:
                        if hasattr(plugins[plugin], "types"):
                            if etype in plugins[plugin].types():
                                plugin_name = plugin
                                if hasattr(plugins[plugin], "entry_info"):
                                    description = plugins[plugin].entry_info(entry)


                    #self.layout.addWidget(QLabel(plugin_name), self.layout_row, self.layout_col)
                    self.layout.addWidget(QLabel(description), self.layout_row, self.layout_col)
                    self.layout.addWidget(QPushButton("edit"), self.layout_row, self.layout_col + 1)
                    self.layout_row += 1



            self.layout.addWidget(QPushButton("add"), self.layout_row, self.layout_col + 1)
            self.layout_row += 1
            self.layout_col -= 1

                


    def gen_setup_options(self, options):
        for name, option in options.items():
            print(name, option)

            if option["type"] == "dict":
                self.layout.addWidget(QLabel(name), self.layout_row, self.layout_col)
                self.layout_row += 1
                self.layout_col += 1
                self.gen_setup_options(option["options"])
                self.layout_col -= 1

            elif option["type"] == "bool":
                self.layout.addWidget(QLabel(name), self.layout_row, self.layout_col)
                tedit = QCheckBox()
                tedit.setChecked(True)
                self.layout.addWidget(tedit, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "input":
                self.layout.addWidget(QLabel(name), self.layout_row, self.layout_col)
                tedit = QLineEdit()
                tedit.setText(name)
                self.layout.addWidget(tedit, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            elif option["type"] == "output":
                self.layout.addWidget(QLabel(name), self.layout_row, self.layout_col)
                tedit = QLineEdit()
                tedit.setText(name)
                self.layout.addWidget(tedit, self.layout_row, self.layout_col + 1)
                self.layout_row += 1

            else:
                self.layout.addWidget(QLabel(name), self.layout_row, self.layout_col)
                tedit = QLineEdit()
                tedit.setText(name)
                self.layout.addWidget(tedit, self.layout_row, self.layout_col + 1)
                self.layout_row += 1




if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())

