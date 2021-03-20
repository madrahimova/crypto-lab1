
import sys

from PyQt5 import QtWidgets

import ui.mainscreen

class MainScreen(QtWidgets.QMainWindow, ui.mainscreen.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.GenerateButton.clicked.connect(self.f)
        self.encryptButton.clicked.connect(self.f)
        self.decipherButton.clicked.connect(self.f)
        
    def f(self):
        print("тут")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainScreen()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
