# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(100, 60, 191, 42))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(70, 150, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(70, 200, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.emailEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.emailEntry.setGeometry(QtCore.QRect(170, 150, 151, 20))
        self.emailEntry.setObjectName("emailEntry")
        self.emailEntry_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.emailEntry_2.setGeometry(QtCore.QRect(170, 200, 151, 20))
        self.emailEntry_2.setObjectName("emailEntry_2")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(144, 270, 101, 23))
        self.loginButton.setObjectName("loginButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WriterEditor"))
        self.title.setText(_translate("MainWindow", "WriterEditor"))
        self.emailLabel.setText(_translate("MainWindow", "email"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.loginButton.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
