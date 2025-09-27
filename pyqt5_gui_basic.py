# pyqt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # sets window title
        self.setWindowTitle("My cool first GUI")
        # sets size/placement of gui window
        # parameters: (x, y, width, height)
        self.setGeometry(200, 200, 500, 500)
        # sets icon for gui window
        self.setWindowIcon(QIcon("profilepic.jpg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # shows window briefly
    sys.exit(app.exec_()) # ensures clean exit of program

if __name__ == "__main__":
    main()