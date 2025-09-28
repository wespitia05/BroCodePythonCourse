# pyqt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # sets window title
        self.setWindowTitle("My cool first GUI")
        # sets size/placement of gui window
        # parameters: (x, y, width, height)
        self.setGeometry(200, 200, 500, 500)
        self.button = QPushButton("Click Me", self) # self refers to our window object
        # sets icon for gui window
        self.setWindowIcon(QIcon("profilepic.jpg"))
        self.label = QLabel("Hello", self)
        self.initUT()

    def initUT(self):
        self.button.setGeometry(150, 200, 200, 100) # set size of button/position
        self.button.setStyleSheet("font-size: 30px") # sets font size
        self.button.clicked.connect(self.on_click) # connects the button to the clicked method

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px")
    
    # this function handles when you click the button
    def on_click(self):
        self.label.setText("Goodbye")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # shows window briefly
    sys.exit(app.exec_()) # ensures clean exit of program

if __name__ == "__main__":
    main()