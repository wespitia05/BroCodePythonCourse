# pyqt5 setStyleSheet()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget) # centers widgets

        hbox = QHBoxLayout() # creates horizontal box layout

        # adds the buttons into the horizontal box layout
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("b1")
        self.button2.setObjectName("b2")
        self.button3.setObjectName("b3")

        # padding: top side
        # margin: space between widgets
        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#b1 {
                background: hsl(0, 100%, 64%);
            }
            QPushButton#b1:hover {
                background: hsl(0, 100%, 84%);
            }
            QPushButton#b2 {
                background: hsl(122, 100%, 64%);
            }
            QPushButton#b2:hover {
                background: hsl(122, 100%, 84%);
            }
            QPushButton#b3 {
                background: hsl(204, 100%, 64%);
            }
            QPushButton#b3:hover {
                background: hsl(204, 100%, 84%);
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # shows window briefly
    sys.exit(app.exec_()) # ensures clean exit of program

if __name__ == "__main__":
    main()