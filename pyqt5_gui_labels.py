# pyqt5 labels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

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

        # set what the label will say
        label = QLabel("Hello, world!", self)
        # set the font and font size
        label.setFont(QFont("Eurostile", 40))
        # set where the label will be positioned
        label.setGeometry(0, 0, 500, 100)
        # add some css label properties
        label.setStyleSheet("color: #1fff5a;"
                            "background-color: navy;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        # align vertically top
        # label.setAlignment(Qt.AlignTop)
        # align vertically bottom
        # label.setAlignment(Qt.AlignBottom)
        # align vertically center
        # label.setAlignment(Qt.AlignVCenter)
        
        # align horizontally right
        # label.setAlignment(Qt.AlignRight)
        # align horizontally center
        # label.setAlignment(Qt.AlignHCenter)
        # align horizontally left
        # label.setAlignment(Qt.AlignLeft)

        # align horizontally center and top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        # align horizontally center and bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        # align horizontally center and vertically center
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # shortcut to align center and center
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # shows window briefly
    sys.exit(app.exec_()) # ensures clean exit of program

if __name__ == "__main__":
    main()