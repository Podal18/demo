from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import pymysql
from one import Ui_onef
from two import Ui_twof
from izm import Ui_Changef
from info import  Ui_infof

class One(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_onef()
        self.ui.setupUi(self)
        self.ui.delButton.clicked.connect(self.dell)
        self.ui.changeButton.clicked.connect(self.changee)
        self.ui.addButton.clicked.connect(self.openadd)
        self.ui.closeButton.clicked.connect(self.close)
        self.showdata()

    def dell(self):
        r = self.ui.tableWidget.currentRow()
        idd = int(self.ui.tableWidget.item(r, 0).text())
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("delete from zayavka where id = %s", (idd,))
            con.commit()
            self.showdata()
            con.close()

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ура", f"ошибка:{e}")

    def showdata(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("select zayavka.id, cover.model, zayavka.l, zayavka.w, zayavka.count_pol * cover.price, status.name from cover join zayavka on zayavka.id_cover = cover.id join status on status.id = zayavka.id_status")
            text = cur.fetchall()

            self.ui.tableWidget.setRowCount(len(text))
            self.ui.tableWidget.setColumnCount(6)
            self.ui.tableWidget.setColumnHidden(0, True)
            self.ui.tableWidget.setHorizontalHeaderLabels(["Айди", "Модель", "Длинна", "Ширина", "Сумма", "Статус"])

            for i, j in enumerate(text):
                for w, ww in enumerate(j):
                    self.ui.tableWidget.setItem(i, w, QtWidgets.QTableWidgetItem(str(ww)))
            con.close()

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ура", f"ошибка: {e}")

    def changee(self):
        r = self.ui.tableWidget.currentRow()
        idd = int(self.ui.tableWidget.item(r, 0).text())
        self.uii = Change(idd, self)
        self.uii.show()
        self.close()

    def openadd(self):
        self.twof = Two(self)
        self.twof.show()
        self.close()

class Change(QtWidgets.QWidget):
    def __init__(self, q, ex):
        super().__init__()
        self.ui = Ui_Changef()
        self.ui.setupUi(self)
        self.q = q
        self.ex = ex

        self.ui.chButton.clicked.connect(self.changedata)
        self.ui.backButton.clicked.connect(self.back)

        self.load_data()

    def load_data(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("""
                SELECT zayavka.l, zayavka.w, zayavka.count_pol, cover.model, cover.id 
                FROM zayavka 
                JOIN cover ON zayavka.id_cover = cover.id 
                WHERE zayavka.id = %s
            """, (self.q,))
            text = cur.fetchone()
            con.close()

            l, w, cnt, mn, mi = text
            self.ui.dlinaEdit.setText(str(l))
            self.ui.shirinaEdit.setText(str(w))
            self.ui.cntEdit.setText(str(cnt))
            self.showcombo(s=mi)
            print(mi)

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Ошибка при загрузке: {e}")

    def showcombo(self, s=None):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("SELECT id, model FROM cover")
            text = cur.fetchall()
            con.close()

            for i, (w, ww) in enumerate(text):
                self.ui.comboBox.addItem(ww, w)
                if w == s:
                    self.ui.comboBox.setCurrentIndex(i)

        except Exception as e:
            print("Ошибка при загрузке моделей:", e)

    def changedata(self):
        l = self.ui.dlinaEdit.text()
        w = self.ui.shirinaEdit.text()
        count = self.ui.cntEdit.text()
        cover_id = self.ui.comboBox.currentData()

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("""
                UPDATE zayavka 
                SET l = %s, w = %s, count_pol = %s, id_cover = %s 
                WHERE id = %s
            """, (l, w, count, cover_id, self.q))
            con.commit()
            con.close()

            QtWidgets.QMessageBox.information(self, "Успех", "Запись успешно обновлена")
            self.back()

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Ошибка при сохранении: {e}")

    def back(self):
        self.ex.showdata()
        self.ex.show()
        self.close()



class Two(QtWidgets.QWidget):
    def __init__(self, ex):
        super().__init__()
        self.ui = Ui_twof()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.adddata)
        self.ui.backButton.clicked.connect(self.back)
        self.ex = ex
        self.showcombo()

    def showcombo(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3310)
            cur = con.cursor()
            cur.execute("select id, model from cover")
            text = cur.fetchall()
            for i, j in text:
                self.ui.comboBox.addItem(str(j), i)

        except Exception as e:
            print(e)

    def back(self):
        self.ex.showdata()
        self.ex.show()
        self.close()

    def adddata(self):
        l = self.ui.dlinaEdit.text()
        o = self.ui.shirinaEdit.text()
        cnt = self.ui.cntEdit.text()
        combo = self.ui.comboBox.currentData()
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="zxc", port=3310)
            cur = con.cursor()
            sql = f"insert into zayavka (id_cover, l, w, id_status, count_pol) values (%s, %s, %s, %s, %s)"
            cur.execute(sql, (combo, l, o, 1, cnt))
            con.commit()
            QtWidgets.QMessageBox.critical(self, "Ура","Данные успешно добавлены")
            con.close()

        except Exception as e:
            print(e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = One()
    w.show()
    sys.exit(app.exec())
