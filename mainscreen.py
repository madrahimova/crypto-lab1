
import sys
from func.BigInt import BigInt as bg
from func import Random as rd
from PyQt5 import QtWidgets

import ui.mainscreen

class MainScreen(QtWidgets.QMainWindow, ui.mainscreen.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.GenerateButton.clicked.connect(self.generate)
        self.encryptButton.clicked.connect(self.encrypt)
        self.decipherButton.clicked.connect(self.encrypt)

        self.p = None
        self.q = None
        self.n = None
        self.pm = None
        self.qm = None
        self.f = None
        self.e = None
        self.d = None

    def generate(self):
        self.p = rd.rand()
        self.q = rd.rand()
        self.n = self.p.mul(self.q)
        self.pm = self.p.mul(bg(1))
        self.qm = self.q.mul(bg(1))
        self.f = self.pm.mul(self.qm)
        self.e = 199
        self.d = bg(5)
        #self.d = self.generateD(self.e, self.f)

        self.eEdit.setText(str(self.e))
        self.openEdit.setText("{" + str(self.e) + ", " + self.n.str() + "}")
        self.closeEdit.setText("{" + self.d.str() + ", " + self.n.str() + "}")

    def encrypt(self):
        pass



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainScreen()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
