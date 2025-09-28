# pyqt5 checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # sets window title
        self.setWindowTitle("My cool first GUI")
        # sets size/placement of gui window
        # parameters: (x, y, width, height)
        self.setGeometry(200, 200, 500, 500)
        # sets checkbox, first parameter is the text
        self.checkbox = QCheckBox("do you like food?", self)
        # sets icon for gui window
        self.setWindowIcon(QIcon("profilepic.jpg"))
        self.initUI()
        
    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Eurostile")
        self.checkbox.setChecked(False) # checkbox will not be filled
        self.checkbox.stateChanged.connect(self.checkbox_change)

    def checkbox_change(self, state):
        # when we check it, state has a value of 2, when we uncheck, state has a value of 0
        # print(state) 
        if state == Qt.Checked:
            print("you like food")
        else:
            print("you do not like food")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # shows window briefly
    sys.exit(app.exec_()) # ensures clean exit of program

if __name__ == "__main__":
    main()