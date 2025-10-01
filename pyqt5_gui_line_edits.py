# pyqt5 line edits

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # sets window title
        self.setWindowTitle("My cool first GUI")
        # sets size/placement of gui window
        # parameters: (x, y, width, height)
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        # sets icon for gui window
        self.setWindowIcon(QIcon("profilepic.jpg"))
        self.initUI()
    
    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial")
        self.button.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial")
        self.button.clicked.connect(self.submit)
        self.line_edit.setPlaceholderText("enter your name")
    
    def submit(self):
        text = self.line_edit.text()
        print(f"hello {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # shows window briefly
    sys.exit(app.exec_()) # ensures clean exit of program

if __name__ == "__main__":
    main()