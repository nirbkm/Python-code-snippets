import time
import sys
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import QProcess


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("pyqt6_example.ui", self)
        self.show()

        self.txt1 = self.findChild(QtWidgets.QLineEdit, "txt_1")

        self.btn_task = self.findChild(QtWidgets.QPushButton, "btn_big_task")
        self.btn_task.pressed.connect(lambda: print(self.txt1.text()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    app.exec()
