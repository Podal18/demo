from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication


from qq import SecondWindow
import pymysql

def show_d():
    try:
        con = pymysql.connect(host='localhost', user='root', password='', database='bb')
        cursor = con.cursor()
        cursor.execute("select name_postav, type_postav, inn FROM pizda")
        data = cursor.fetchall()

        results = []

        for row in data:
            name, typee, inn = row
            text = f"{name}\n{typee}\n{inn}"
            results.append(text)

        return results
    except Exception as e:
        print(f"{str(e)}")
    finally:
        con.close()



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 314)
        Form.setStyleSheet("")

        self.page = 0
        self.item = 3
        self.data = show_d()

        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(QtWidgets.QApplication.quit)

        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.open_second_window)

        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 260, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.n_p)

        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 260, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.b_p)

        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 321, 201))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.up_l()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "exit"))
        self.pushButton_2.setText(_translate("Form", "стр"))
        self.pushButton_3.setText(_translate("Form", "вперед"))
        self.pushButton_4.setText(_translate("Form", "прош"))

    def open_second_window(self):
        self.second_window = SecondWindow(self.Form)  # передаём главное окно
        self.Form.hide()
        self.second_window.show()

    def set_main_widget(self, widget):
        self.Form = widget

    def up_l(self):
        start = self.page * self.item
        end = start + self.item
        current = self.data[start:end]

        self.label.setText(current[0] if len(current) > 0 else "")
        self.label_2.setText(current[1] if len(current) > 1 else "")
        self.label_3.setText(current[2] if len(current) > 2 else "")

    def n_p(self):
        max_page = (len(self.data) - 1) // self.item
        if self.page < max_page:
            self.page += 1
            self.up_l()

    def b_p(self):
        if self.page > 0:
            self.page -= 1
            self.up_l()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.set_main_widget(Form)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
