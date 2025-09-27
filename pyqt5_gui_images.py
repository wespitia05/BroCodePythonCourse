# pyqt5 images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # sets window title
        self.setWindowTitle("My cool first GUI")
        # sets size/placement of gui window
        # parameters: (x, y, width, height)
        self.setGeometry(200, 200, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        # get the path to the image
        pixmap = QPixmap("profilepic.jpg")
        # set the image using pixmap
        label.setPixmap(pixmap)

        # scales image to fit within size
        label.setScaledContents(True)

        # .width() and .height() gets inital size set
        label.setGeometry((self.width() - label.width()) // 2, (self.height() - label.height()) // 2, label.width(), label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # shows window briefly
    sys.exit(app.exec_()) # ensures clean exit of program

if __name__ == "__main__":
    main()