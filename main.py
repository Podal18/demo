import sys
import pymysql
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from addW import Ui_AddW
from welcW import Ui_WelcomeW


# Функция для подключения и выполнения запроса
def execute_query(query, params=()):
    try:
        connection = pymysql.connect(host='localhost', user='root', password='', database='your_db', port=3307)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()
    except Exception as e:
        QMessageBox.critical(None, "Ошибка", f"Ошибка базы данных: {str(e)}")


class AddWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_AddW()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.ui.addB.clicked.connect(self.add_data)
        self.ui.last_b.clicked.connect(self.close)

    def add_data(self):
        # Получаем данные из полей
        name, lastname, age = self.ui.name_Edit.text(), self.ui.lastname_Edit.text(), self.ui.age_Edit.text()

        if name and lastname and age:
            if not age.isdigit():  # Проверка на возраст
                QMessageBox.warning(self, "Ошибка", "Возраст должен быть числом!")
                return
            # Добавляем в базу
            execute_query("INSERT INTO people (first_name, last_name, age) VALUES (%s, %s, %s)", (name, lastname, age))
            self.main_window.load_data()
            self.close()
        else:
            QMessageBox.warning(self, "Внимание", "Заполните все поля!")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WelcomeW()
        self.ui.setupUi(self)
        self.add_window = AddWindow(self)
        self.ui.add_Button.clicked.connect(self.show_add_window)
        self.ui.del_Button.clicked.connect(self.delete_row)
        self.ui.change_Button.clicked.connect(self.update_row)
        self.load_data()
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AllEditTriggers)

    def load_data(self):
        try:
            connection = pymysql.connect(host='localhost', user='root', password='', database='your_db', port=3307)
            cursor = connection.cursor()
            cursor.execute("SELECT id, first_name, last_name, age FROM people")
            records = cursor.fetchall()

            self.ui.tableWidget.setRowCount(len(records))
            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setHorizontalHeaderLabels(['Имя', 'Фамилия', 'Возраст'])

            for row_index, (id_val, fname, lname, age) in enumerate(records):
                self.ui.tableWidget.setItem(row_index, 0, QtWidgets.QTableWidgetItem(fname))
                self.ui.tableWidget.setItem(row_index, 1, QtWidgets.QTableWidgetItem(lname))
                self.ui.tableWidget.setItem(row_index, 2, QtWidgets.QTableWidgetItem(str(age)))
                # Храним ID в заголовке строки (невидимо для пользователя)
                self.ui.tableWidget.setVerticalHeaderItem(row_index, QtWidgets.QTableWidgetItem())
                self.ui.tableWidget.verticalHeaderItem(row_index).setData(QtCore.Qt.ItemDataRole.UserRole, id_val)

            connection.close()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки данных: {str(e)}")

    def show_add_window(self):
        self.add_window.show()

    def delete_row(self):
        selected = self.ui.tableWidget.currentRow()
        if selected != -1:
            id_val = self.ui.tableWidget.verticalHeaderItem(selected).data(QtCore.Qt.ItemDataRole.UserRole)
            if id_val:
                execute_query("DELETE FROM people WHERE id=%s", (id_val,))
                self.load_data()
        else:
            QMessageBox.warning(self, "Внимание", "Выберите строку для удаления.")

    def update_row(self):
        selected = self.ui.tableWidget.currentRow()
        if selected != -1:
            id_val = self.ui.tableWidget.verticalHeaderItem(selected).data(QtCore.Qt.ItemDataRole.UserRole)

            new_fname = self.ui.tableWidget.item(selected, 0).text()
            new_lname = self.ui.tableWidget.item(selected, 1).text()
            new_age = self.ui.tableWidget.item(selected, 2).text()

            if not new_age.isdigit():
                QMessageBox.warning(self, "Ошибка", "Возраст должен быть числом.")
                return

            execute_query("UPDATE people SET first_name=%s, last_name=%s, age=%s WHERE id=%s",
                          (new_fname, new_lname, new_age, id_val))
            QMessageBox.information(self, "Успех", "Данные обновлены!")
            self.load_data()
        else:
            QMessageBox.warning(self, "Внимание", "Выберите строку для изменения.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
