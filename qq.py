from PyQt6 import QtCore, QtGui, QtWidgets


class SecondWindow(QtWidgets.QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(400, 300)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Назад")
        self.pushButton_2.clicked.connect(self.gob)

    def gob(self):
        self.mw.show()
        self.close()

