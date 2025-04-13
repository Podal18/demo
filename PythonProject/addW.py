from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddW(object):
    def setupUi(self, AddW):
        AddW.setObjectName("AddW")
        AddW.resize(317, 250)
        AddW.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.last_b = QtWidgets.QPushButton(parent=AddW)
        self.last_b.setGeometry(QtCore.QRect(180, 160, 75, 23))
        self.last_b.setObjectName("last_b")
        self.addB = QtWidgets.QPushButton(parent=AddW)
        self.addB.setGeometry(QtCore.QRect(50, 160, 75, 23))
        self.addB.setObjectName("addB")
        self.widget = QtWidgets.QWidget(parent=AddW)
        self.widget.setGeometry(QtCore.QRect(80, 60, 135, 74))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_Edit = QtWidgets.QLineEdit(parent=self.widget)
        self.name_Edit.setObjectName("name_Edit")
        self.verticalLayout.addWidget(self.name_Edit)
        self.lastname_Edit = QtWidgets.QLineEdit(parent=self.widget)
        self.lastname_Edit.setObjectName("lastname_Edit")
        self.verticalLayout.addWidget(self.lastname_Edit)
        self.age_Edit = QtWidgets.QLineEdit(parent=self.widget)
        self.age_Edit.setObjectName("age_Edit")
        self.verticalLayout.addWidget(self.age_Edit)

        self.retranslateUi(AddW)
        QtCore.QMetaObject.connectSlotsByName(AddW)


    def retranslateUi(self, AddW):
        _translate = QtCore.QCoreApplication.translate
        AddW.setWindowTitle(_translate("AddW", "Добавление"))
        self.last_b.setText(_translate("AddW", "назад"))
        self.addB.setText(_translate("AddW", "Добавить"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddW = QtWidgets.QWidget()
    ui = Ui_AddW()
    ui.setupUi(AddW)
    AddW.show()
    sys.exit(app.exec())