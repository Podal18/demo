from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QWidget, QTableWidget, QApplication, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os
import pymysql
from authw2 import Ui_auth2
from korzinaw import Ui_korzina_f
from productw import Ui_add_f
from add_to_t import Ui_add_tovar
from admw import Ui_admin_form

class add_tovar(QtWidgets.QWidget):
    def __init__(self, ex):
        super().__init__()
        self.ui = Ui_add_tovar()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back)
        self.ex = ex
        self.ui.tableWidget.cellClicked.connect(self.show_data)
        self.show_data()

        self.ui.add_in_trash.clicked.connect(self.add_data)
        self.add_combo()

    def add_combo(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3309)
            cur = con.cursor()
            cur.execute("select id from cover")
            text = cur.fetchall()

            for i in text:
                self.ui.comboBox.addItem(str(i[0]))

        except Exception as e:
            print(e)

    def add_data(self):
        cnt = self.ui.cntEdit.text()
        w = self.ui.weigEdit.text()
        l = self.ui.lengEdit.text()
        num = self.ui.comboBox.currentText()

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3309)
            cur = con.cursor()
            sql = f"insert into zayavka (id_cover, l, w, id_status, count_pol) values (%s, %s, %s, %s, %s)"
            cur.execute(sql, (num, w, l, 1, cnt))
            con.commit()
            QtWidgets.QMessageBox.warning(None, "ПОЗДРАВЛЯЮ!!!!!", "Данные успешно добавлены")
            self.show_data()

        except Exception as e:
            print(str(e))


    def show_data(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3309)
            cur = con.cursor()
            cur.execute("select cover.id, cover.img, cover.model, material.name, cover.from, cover.price from cover join material on cover.material_id = material.id")
            text = cur.fetchall()
            self.ui.tableWidget.setRowCount(len(text))
            self.ui.tableWidget.setColumnCount(6)
            self.ui.tableWidget.setHorizontalHeaderLabels(['Номер слота', 'image', 'model', 'material', 'from', 'price'])

            for i, j in enumerate(text):
                for w, ww in enumerate(j):
                    if w == 1:
                        label = QtWidgets.QLabel()
                        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

                        img = os.path.abspath(ww) if ww else ""
                        pix = QPixmap(img)
                        label.setPixmap(pix)
                        self.ui.tableWidget.setCellWidget(i, w, label)
                    else:
                        self.ui.tableWidget.setItem(i, w, QtWidgets.QTableWidgetItem(str(ww)))

        except Exception as e:
            print(str(e))

    def back(self):
        self.ex.show()
        self.hide()

class admw(QtWidgets.QWidget):
    def __init__(self, ex):
        super().__init__()
        self.ui = Ui_admin_form()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back)
        self.ex = ex
        self.ui.change_b.clicked.connect(self.change_data)
        self.ui.comboBox.currentTextChanged.connect(self.show_data)
        self.show_data()
        self.ui.tableWidget.cellClicked.connect(self.show_data)
        self.show_data()



    def change_data(self):
        pass

    def back(self):
        self.ex.show()
        self.hide()

    def show_data(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3309)
            cur = con.cursor()
            sortt = "ASC" if self.ui.comboBox.currentText() == "По возрастанию" else "DESC"
            sql = f"select cover.model, users.login, cover.img, cover.cnt, status.name from cover join zayavka on cover.id = zayavka.id_cover join status on status.id = zayavka.id_status join users on cover.id_client = users.id order by cover.cnt {sortt}"
            cur.execute(sql)
            text = cur.fetchall()
            self.ui.tableWidget.setRowCount(len(text))
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(['model', 'user', 'image', 'count', 'status'])
            

            for i, j in enumerate(text):
                for w, ww in enumerate(j):
                    if w == 2:
                        lab = QtWidgets.QLabel()
                        lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

                        img = os.path.abspath(ww) if ww else ""
                        pixmap = QPixmap(img)
                        lab.setPixmap(pixmap)

                        self.ui.tableWidget.setCellWidget(i, w, lab)
                    else:
                        self.ui.tableWidget.setItem(i, w, QtWidgets.QTableWidgetItem(str(ww)))


        except Exception as e:
            print(e)
        finally:
            con.close()


class auth_w(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_auth2()
        self.ui.setupUi(self)
        self.ui.polz_b.clicked.connect(self.pol_w)
        self.ui.adm_b.clicked.connect(self.vhod)
        self.vhoduser = prod_w(self)
        self.vhodadm = admw(self)

    def vhod(self):
        self.vhodadm.show()
        self.hide()

    def pol_w(self):
        self.vhoduser.show()
        self.hide()

class korz_w(QtWidgets.QWidget):
    def __init__(self, ex):
        super().__init__()
        self.ui = Ui_korzina_f()
        self.ui.setupUi(self)
        self.ui.delButton.clicked.connect(self.del_data)
        self.ui.backButton.clicked.connect(self.back)
        self.ui.changeButton.clicked.connect(self.change_data)
        self.ui.zakazButton.clicked.connect(self.add_data)
        self.ex = ex
        self.ui.tableWidget_2.cellClicked.connect(self.show_data)
        self.show_data()

    def show_data(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', database='zxc', port=3309)
            cursor = con.cursor()
            cursor.execute("select * from zayavka where id_status = 1")
            text = cursor.fetchall()
            self.ui.tableWidget_2.setRowCount(len(text))
            self.ui.tableWidget_2.setColumnCount(6)

            for i, j in enumerate(text):
                for w, ww in enumerate(j):
                    self.ui.tableWidget_2.setItem(i, w, QtWidgets.QTableWidgetItem(str(ww)))

            con.close()

        except Exception as e:
            print(e)

    def del_data(self):
        selected_row = self.ui.tableWidget_2.currentRow()
        id_vak = int(self.ui.tableWidget_2.item(selected_row, 0).text())
        try:
            con = pymysql.connect(host='localhost', user='root', password='', database='zxc', port=3309)
            cursor = con.cursor()
            cursor.execute("DELETE FROM zayavka WHERE id=%s", (id_vak,))
            con.commit()
            self.show_data()
        except Exception as e:
            print(e)

    def back(self):
        self.ex.show()
        self.hide()

    def change_data(self):
        pass

    def add_data(self):
        selected_row = self.ui.tableWidget_2.currentRow()
        id_vak = int(self.ui.tableWidget_2.item(selected_row, 0).text())
        try:
            con = pymysql.connect(host='localhost', user='root', password='', database='zxc', port=3309)
            cursor = con.cursor()
            cursor.execute("Update zayavka set id_status = 2 WHERE id=%s", (id_vak,))
            con.commit()
            print("сучка")
            self.show_data()
        except Exception as e:
            print(e)



class prod_w(QtWidgets.QWidget):
    def __init__(self, ex):
        super().__init__()
        self.ui = Ui_add_f()
        self.ui.setupUi(self)
        self.ui.backButton.clicked.connect(self.back)
        self.ui.addButton.clicked.connect(self.add_data)
        self.ui.trashButton.clicked.connect(self.show_trash)
        self.ex = ex
        self.tr = korz_w(self)
        self.add_d = add_tovar(self)
        self.show_data()

    def show_data(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', database='zxc', port=3309)
            cursor = con.cursor()
            cursor.execute("SELECT cover.model, material.name, cover.from, cover.img from cover join material on cover.material_id = material.id")
            text = cursor.fetchall()
            self.ui.tableWidget.setRowCount(len(text))
            self.ui.tableWidget.setColumnCount(4)
            self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'Имя', 'Фамилия', 'Возраст'])

            for i, j in enumerate(text):
                for w, ww in enumerate(j):
                    if w == 3:
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

    def back(self):
        self.ex.show()
        self.hide()

    def add_data(self):
        self.add_d.show()
        self.hide()

    def show_trash(self):
        self.tr.show()
        self.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = auth_w()
    win.show()
    sys.exit(app.exec())