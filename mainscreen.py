
import sys
from func.BigInt import BigInt as bg
from func import Random as rd
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
        self.p = rd.rand()
        self.q = rd.rand()
        self.n = self.p.mul(self.q)
        self.pm = self.p.mul(bg(1))
        self.qm = self.q.mul(bg(1))
        self.f = self.pm.mul(self.qm)
        self.e = 199

        self.eEdit.setText(str(self.e))
        self.openEdit.setText("{" + str(self.e) + ", " + self.n.str() + "}")
        self.d = self.generateD(self.e, self.f)
        self.closeEdit.setText("{" + str(self.d) + ", " + self.n.str() + "}")

    def generateD(self, e, f):
        d = 1
        print((bg(d).mul(bg(e))).mod(f).equals(bg(1)))
        while (bg(d).mul(bg(e))).mod(f).equals(bg(1)) == False:
            d += 1

            print(d, " ", (bg(d).mul(bg(e))).mod(f).str())
        return d

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainScreen()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
