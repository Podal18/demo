from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Ui_auth_u(object):
    def setupUi(self, auth_u):
        auth_u.setObjectName("auth_u")
        auth_u.resize(276, 230)
        auth_u.setStyleSheet("background-color: rgb(225, 176, 255);\n"
"font: 11pt \"MV Boli\";")
        self.widget = QtWidgets.QWidget(parent=auth_u)
        self.widget.setGeometry(QtCore.QRect(60, 160, 158, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.widget1 = QtWidgets.QWidget(parent=auth_u)
        self.widget1.setGeometry(QtCore.QRect(60, 30, 154, 88))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_edit = QtWidgets.QLineEdit(parent=self.widget1)
        self.login_edit.setObjectName("login_edit")
        self.verticalLayout.addWidget(self.login_edit)
        self.login_edit_3 = QtWidgets.QLineEdit(parent=self.widget1)
        self.login_edit_3.setObjectName("login_edit_3")
        self.verticalLayout.addWidget(self.login_edit_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(auth_u)
        QtCore.QMetaObject.connectSlotsByName(auth_u)

    def retranslateUi(self, auth_u):
        _translate = QtCore.QCoreApplication.translate
        auth_u.setWindowTitle(_translate("auth_u", "Авторизация"))
        self.pushButton.setText(_translate("auth_u", "вход"))
        self.pushButton_2.setText(_translate("auth_u", "рег"))
        self.label.setText(_translate("auth_u", "Добро пожаловать!"))
        self.login_edit.setPlaceholderText(_translate("auth_u", "Логин"))
        self.login_edit_3.setPlaceholderText(_translate("auth_u", "Пароль"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    auth_u = QtWidgets.QWidget()
    ui = Ui_auth_u()
    ui.setupUi(auth_u)
    auth_u.show()
    sys.exit(app.exec())
