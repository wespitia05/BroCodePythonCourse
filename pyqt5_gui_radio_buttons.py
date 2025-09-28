# pyqt5 radio buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # sets window title
        self.setWindowTitle("My cool first GUI")
        # sets size/placement of gui window
        # parameters: (x, y, width, height)
        self.setGeometry(200, 200, 500, 500)
        self.radio1 = QRadioButton("visa", self)
        self.radio2 = QRadioButton("mastercard", self)
        self.radio3 = QRadioButton("giftcard", self)
        self.radio4 = QRadioButton("in-store", self)
        self.radio5 = QRadioButton("online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()
        # sets icon for gui window
        self.setWindowIcon(QIcon("profilepic.jpg"))

    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 40px;"
                           "font-family: Eurostile;"
                           "padding-left: 10px;"
                           "}")
        
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender() # sender method will return widget that sent the signal
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # shows window briefly
    sys.exit(app.exec_()) # ensures clean exit of program

if __name__ == "__main__":
    main()