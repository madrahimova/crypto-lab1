# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 305)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GenerateButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateButton.setGeometry(QtCore.QRect(13, 35, 145, 25))
        self.GenerateButton.setStyleSheet("background: #C4C4C4;")
        self.GenerateButton.setObjectName("GenerateButton")
        self.encryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.encryptButton.setGeometry(QtCore.QRect(13, 186, 145, 25))
        self.encryptButton.setStyleSheet("background: #C4C4C4;")
        self.encryptButton.setObjectName("encryptButton")
        self.decipherButton = QtWidgets.QPushButton(self.centralwidget)
        self.decipherButton.setGeometry(QtCore.QRect(13, 228, 145, 25))
        self.decipherButton.setStyleSheet("background: #C4C4C4;")
        self.decipherButton.setObjectName("decipherButton")
        self.eEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.eEdit.setGeometry(QtCore.QRect(196, 35, 422, 25))
        self.eEdit.setObjectName("eEdit")
        self.openEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.openEdit.setGeometry(QtCore.QRect(48, 77, 570, 25))
        self.openEdit.setObjectName("openEdit")
        self.closeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.closeEdit.setGeometry(QtCore.QRect(48, 119, 570, 25))
        self.closeEdit.setObjectName("closeEdit")
        self.encryptEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.encryptEdit.setGeometry(QtCore.QRect(196, 186, 422, 25))
        self.encryptEdit.setObjectName("encryptEdit")
        self.decipherEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.decipherEdit.setGeometry(QtCore.QRect(196, 228, 422, 25))
        self.decipherEdit.setObjectName("decipherEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(179, 40, 7, 14))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 122, 60, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GenerateButton.setText(_translate("MainWindow", "Сгенерировать ключи"))
        self.encryptButton.setText(_translate("MainWindow", "Шифровать"))
        self.decipherButton.setText(_translate("MainWindow", "Расшифровать"))
        self.label.setText(_translate("MainWindow", "e"))
        self.label_2.setText(_translate("MainWindow", "{e, n}"))
        self.label_3.setText(_translate("MainWindow", "{d, n}"))