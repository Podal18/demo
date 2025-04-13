from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WelcomeW(object):
    def setupUi(self, WelcomeW):
        WelcomeW.setObjectName("WelcomeW")
        WelcomeW.resize(396, 321)
        WelcomeW.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.tableWidget = QtWidgets.QTableWidget(parent=WelcomeW)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 361, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(parent=WelcomeW)
        self.widget.setGeometry(QtCore.QRect(30, 240, 321, 58))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_Button = QtWidgets.QPushButton(parent=self.widget)
        self.add_Button.setObjectName("add_Button")
        self.horizontalLayout.addWidget(self.add_Button)
        self.change_Button = QtWidgets.QPushButton(parent=self.widget)
        self.change_Button.setObjectName("change_Button")
        self.horizontalLayout.addWidget(self.change_Button)
        self.del_Button = QtWidgets.QPushButton(parent=self.widget)
        self.del_Button.setObjectName("del_Button")
        self.horizontalLayout.addWidget(self.del_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ex_b = QtWidgets.QPushButton(parent=self.widget)
        self.ex_b.setObjectName("ex_b")
        self.ex_b.clicked.connect(QtWidgets.QApplication.quit)
        self.horizontalLayout_2.addWidget(self.ex_b)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(WelcomeW)
        QtCore.QMetaObject.connectSlotsByName(WelcomeW)

    def retranslateUi(self, WelcomeW):
        _translate = QtCore.QCoreApplication.translate
        WelcomeW.setWindowTitle(_translate("WelcomeW", "Hi"))
        self.add_Button.setText(_translate("WelcomeW", "добавить"))
        self.change_Button.setText(_translate("WelcomeW", "изменить"))
        self.del_Button.setText(_translate("WelcomeW", "удалить"))
        self.ex_b.setText(_translate("WelcomeW", "выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeW = QtWidgets.QWidget()
    ui = Ui_WelcomeW()
    ui.setupUi(WelcomeW)
    WelcomeW.show()
    sys.exit(app.exec())