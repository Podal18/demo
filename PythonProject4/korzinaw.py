from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import  QIcon

class Ui_korzina_f(object):
    def setupUi(self, korzina_f):
        korzina_f.setObjectName("korzina_f")
        korzina_f.resize(432, 265)
        korzina_f.setStyleSheet("background-color: rgb(250, 190, 255);\n"
"font: 8pt \"New York\";")
        self.delButton = QtWidgets.QPushButton(parent=korzina_f)
        self.delButton.setGeometry(QtCore.QRect(280, 100, 121, 31))
        self.delButton.setStyleSheet("background-color: rgb(255, 247, 213);\n"
"border-radius:10px;\n"
"font: 10pt \"MS Sans Serif\";")
        self.delButton.setObjectName("delButton")
        self.backButton = QtWidgets.QPushButton(parent=korzina_f)
        self.backButton.setGeometry(QtCore.QRect(280, 210, 121, 31))
        self.backButton.setStyleSheet("background-color: rgb(255, 247, 213);\n"
"border-radius:10px;\n"
"font: 10pt \"MS Sans Serif\";")
        self.backButton.setObjectName("backButton")
        self.changeButton = QtWidgets.QPushButton(parent=korzina_f)
        self.changeButton.setGeometry(QtCore.QRect(280, 60, 121, 31))
        self.changeButton.setStyleSheet("background-color: rgb(255, 247, 213);\n"
"border-radius:10px;\n"
"font: 10pt \"MS Sans Serif\";")
        self.changeButton.setObjectName("changeButton")
        self.zakazButton = QtWidgets.QPushButton(parent=korzina_f)
        self.zakazButton.setGeometry(QtCore.QRect(280, 20, 121, 31))
        self.zakazButton.setStyleSheet("background-color: rgb(255, 247, 213);\n"
"border-radius:10px;\n"
"font: 10pt \"MS Sans Serif\";")
        self.zakazButton.setObjectName("zakazButton")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=korzina_f)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 251, 241))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)

        self.retranslateUi(korzina_f)
        QtCore.QMetaObject.connectSlotsByName(korzina_f)

    def retranslateUi(self, korzina_f):
        _translate = QtCore.QCoreApplication.translate
        korzina_f.setWindowTitle(_translate("korzina_f", "Корзина"))
        self.delButton.setText(_translate("korzina_f", "Удалить"))
        self.backButton.setText(_translate("korzina_f", "Назад"))
        self.changeButton.setText(_translate("korzina_f", "Изменить"))
        self.zakazButton.setText(_translate("korzina_f", "Заказать"))
        korzina_f.setWindowIcon(QIcon('Icon.png'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    korzina_f = QtWidgets.QWidget()
    ui = Ui_korzina_f()
    ui.setupUi(korzina_f)
    korzina_f.show()
    sys.exit(app.exec())