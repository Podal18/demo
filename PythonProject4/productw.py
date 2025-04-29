from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import  QIcon

class Ui_add_f(object):
    def setupUi(self, add_f):
        add_f.setObjectName("add_f")
        add_f.resize(413, 349)
        add_f.setStyleSheet("background-color: rgb(250, 190, 255);\n"
"font: 8pt \"New York\";")
        self.tableWidget = QtWidgets.QTableWidget(parent=add_f)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 371, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.addButton = QtWidgets.QPushButton(parent=add_f)
        self.addButton.setGeometry(QtCore.QRect(20, 300, 121, 31))
        self.addButton.setStyleSheet("background-color: rgb(255, 247, 213);\n"
"border-radius:10px;\n"
"font: 10pt \"MS Sans Serif\";")
        self.addButton.setObjectName("vhodButton_2")
        self.backButton = QtWidgets.QPushButton(parent=add_f)
        self.backButton.setGeometry(QtCore.QRect(280, 300, 121, 31))
        self.backButton.setStyleSheet("background-color: rgb(255, 247, 213);\n"
"border-radius:10px;\n"
"font: 10pt \"MS Sans Serif\";")
        self.backButton.setObjectName("vhodButton_5")
        self.trashButton = QtWidgets.QPushButton(parent=add_f)
        self.trashButton.setGeometry(QtCore.QRect(150, 300, 121, 31))
        self.trashButton.setStyleSheet("background-color: rgb(255, 247, 213);\n"
"border-radius:10px;\n"
"font: 10pt \"MS Sans Serif\";")
        self.trashButton.setObjectName("vhodButton_3")

        self.retranslateUi(add_f)
        QtCore.QMetaObject.connectSlotsByName(add_f)

    def retranslateUi(self, add_f):
        _translate = QtCore.QCoreApplication.translate
        add_f.setWindowTitle(_translate("add_f", "К товарам"))
        self.addButton.setText(_translate("add_f", "Добавить "))
        self.backButton.setText(_translate("add_f", "Назад"))
        self.trashButton.setText(_translate("add_f", "Корзина"))
        add_f.setWindowIcon(QIcon('icon.png'))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_f = QtWidgets.QWidget()
    ui = Ui_add_f()
    ui.setupUi(add_f)
    add_f.show()
    sys.exit(app.exec())