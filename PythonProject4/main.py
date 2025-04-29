from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt
import os
import pymysql
from PyQt6.QtGui import QPixmap
from add_to_t import Ui_add_tovar
from admw import Ui_admin_form
from authw2 import Ui_auth2
from korzinaw import Ui_korzina_f
from productw import Ui_add_f
import sys



class authw(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_auth2()
        self.ui.setupUi(self)
        self.ui.adm_b.clicked.connect(self.admwin)
        self.ui.polz_b.clicked.connect(self.uswind)
        self.admin = admw(self)
        self.user = usw(self)

    def admwin(self):
        self.admin.show()
        self.hide()

    def uswind(self):
        self.user.show()
        self.hide()


class admw(QtWidgets.QWidget):
    def __init__(self, ex):
        super().__init__()
        self.ui = Ui_admin_form()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back)
        self.ui.change_b.clicked.connect(self.change_data)
        self.ex = ex
        self.ui.comboBox.currentTextChanged.connect(self.show_data)
        self.show_data()

    def show_data(self):
        try:
            con = pymysql.connect(host="localhost", user= "root", password="", database="zxc", port=3310)
            sortt = "ASC" if self.ui.comboBox.currentText() == "По возрастанию" else "DESC"
            cur = con.cursor()
            sql = f"select zayavka.id, cover.model, zayavka.l, zayavka.w, zayavka.count_pol, status.name from cover join zayavka on zayavka.id_cover = cover.id join status on status.id = zayavka.id_status order by count_pol {sortt}"
            cur.execute(sql)
            text = cur.fetchall()

            self.ui.tableWidget.setRowCount(len(text))
            self.ui.tableWidget.setColumnCount(6)
            self.ui.tableWidget.setColumnHidden(0, True)


            for i, j in enumerate(text):
                for w, ww in enumerate(j):
                    self.ui.tableWidget.setItem(i, w, QtWidgets.QTableWidgetItem(str(ww)))

            con.close()

        except Exception as e:
            print(e)


    def back(self):
        self.ex.show()
        self.close()

    def change_data(self):
        row = self.ui.tableWidget.currentRow()
        idd = int(self.ui.tableWidget.item(row, 0).text())
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("update zayavka set id_status = 3 where id=%s", (idd,))
            con.commit()
            self.show_data()
            con.close()
        except Exception as e:
            print(e)

class usw(QtWidgets.QWidget):
    def __init__(self, ex):
        super().__init__()
        self.ui = Ui_add_f()
        self.ui.setupUi(self)
        self.ui.backButton.clicked.connect(self.back)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.trashButton.clicked.connect(self.open_trash)
        self.ex = ex
        self.trash = korzw(self)
        self.add = addw(self)
        self.show_data()

    def back(self):
        self.ex.show()
        self.close()

    def add_data(self):
        self.add.show()
        self.close()

    def open_trash(self):
        self.trash.show()
        self.close()

    def show_data(self):
        try:
            con = pymysql.connect(host="localhost", user= "root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("select model, fromm, img, price from cover")
            text = cur.fetchall()

            self.ui.tableWidget.setRowCount(len(text))
            self.ui.tableWidget.setColumnCount(4)

            for i, j in enumerate(text):
                for w, ww in enumerate(j):
                    if w == 2:
                        lab = QtWidgets.QLabel()
                        lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

                        img = os.path.abspath(ww) if ww else ""

                        pix = QPixmap(img)
                        lab.setPixmap(pix)
                        self.ui.tableWidget.setCellWidget(i, w, lab)
                    else:
                        self.ui.tableWidget.setItem(i, w, QtWidgets.QTableWidgetItem(str(ww)))

            con.close()

        except Exception as e:
            print(e)


class addw(QtWidgets.QWidget):
    def __init__(self, ex):
        super().__init__()
        self.ui = Ui_add_tovar()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back)
        self.ui.add_in_trash.clicked.connect(self.add_data)
        self.ex = ex
        self.showcom()
        self.show_data()

    def showcom(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("select id from cover")
            text = cur.fetchall()
            for i in text:
                self.ui.comboBox.addItem(str(i[0]))
            self.show_data()
            con.close()


        except Exception as e:
            print(e)


    def back(self):
        self.ex.show()
        self.close()

    def add_data(self):
        cnt = self.ui.cntEdit.text()
        w = self.ui.weigEdit.text()
        l = self.ui.lengEdit.text()
        num = self.ui.comboBox.currentText()

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3310)
            cur = con.cursor()
            sql = f"insert into zayavka (id_cover, l, w, id_status, count_pol) values (%s, %s, %s, %s, %s)"
            cur.execute(sql, (num, l, w, 1, cnt))
            con.commit()
            con.close()
            QtWidgets.QMessageBox.critical(None, "Uraaaa", "GO fuck")
            self.show_data()

        except Exception as e:
            print(e)

    def show_data(self):
        try:
            con = pymysql.connect(host="localhost", user= "root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("select model, fromm, img, price from cover")
            text = cur.fetchall()

            self.ui.tableWidget.setRowCount(len(text))
            self.ui.tableWidget.setColumnCount(5)

            for i, j in enumerate(text):
                for w, ww in enumerate(j):
                    if w == 2:
                        lab = QtWidgets.QLabel()
                        lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

                        img = os.path.abspath(ww) if ww else ""

                        pix = QPixmap(img)
                        lab.setPixmap(pix)
                        self.ui.tableWidget.setCellWidget(i, w, lab)
                    else:
                        self.ui.tableWidget.setItem(i, w, QtWidgets.QTableWidgetItem(str(ww)))

            con.close()

        except Exception as e:
            print(e)



class korzw(QtWidgets.QWidget):
    def __init__(self, ex):
        super().__init__()
        self.ui = Ui_korzina_f()
        self.ui.setupUi(self)
        self.ui.delButton.clicked.connect(self.del_data)
        self.ui.backButton.clicked.connect(self.back)
        self.ui.zakazButton.clicked.connect(self.zakaz_data)
        self.ui.tableWidget_2.cellClicked.connect(self.show_data)
        self.ex = ex
        self.show_data()

    def show_data(self):
        try:
            con = pymysql.connect(host="localhost", user= "root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("select * from zayavka where id_status = 1")
            text = cur.fetchall()
            self.ui.tableWidget_2.setRowCount(len(text))
            self.ui.tableWidget_2.setColumnCount(6)

            for i, j in enumerate(text):
                for w, ww in enumerate(j):
                    self.ui.tableWidget_2.setItem(i, w, QtWidgets.QTableWidgetItem(str(ww)))

            con.close()

        except Exception as e:
            print(e)

    def del_data(self):
        row = self.ui.tableWidget_2.currentRow()
        idd = int(self.ui.tableWidget_2.item(row, 0).text())
        try:
            con = pymysql.connect(host="localhost", user= "root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("delete from zayavka where id=%s", (idd,))
            con.commit()
            self.show_data()
            con.close()

        except Exception as e:
            print(e)

    def back(self):
        self.ex.show()
        self.close()

    def zakaz_data(self):
        row = self.ui.tableWidget_2.currentRow()
        idd = int(self.ui.tableWidget_2.item(row, 0).text())
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("update zayavka set id_status = 2 where id=%s", (idd,))
            con.commit()
            self.show_data()
            con.close()


        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = authw()
    win.show()
    sys.exit(app.exec())

