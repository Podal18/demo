import sys
import pymysql
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from addW import Ui_AddW
from welcW import Ui_WelcomeW


# Функция для подключения и выполнения запроса
def execute_query(query, params=()):
    try:
        connection = pymysql.connect(host='localhost', user='root', password='', database='your_db')
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

    def load_data(self):
        try:
            connection = pymysql.connect(host='localhost', user='root', password='', database='your_db')
            cursor = connection.cursor()
            cursor.execute("SELECT id, first_name, last_name, age FROM people")
            records = cursor.fetchall()
            self.ui.tableWidget.setRowCount(len(records))
            self.ui.tableWidget.setColumnCount(4)
            self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'Имя', 'Фамилия', 'Возраст'])

            for i, row in enumerate(records):
                for j, val in enumerate(row):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))

            connection.close()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки данных: {str(e)}")

    def show_add_window(self):
        self.add_window.show()

    def delete_row(self):
        selected = self.ui.tableWidget.currentRow()
        if selected != -1:
            id_item = self.ui.tableWidget.item(selected, 0)
            if id_item:
                id_val = id_item.text()
                # Удаляем запись по id
                execute_query("DELETE FROM people WHERE id=%s", (id_val,))
                self.load_data()
        else:
            QMessageBox.warning(self, "Внимание", "Выберите строку для удаления.")

    def update_row(self):
        selected = self.ui.tableWidget.currentRow()
        if selected != -1:
            id_val = self.ui.tableWidget.item(selected, 0).text()
            fname = self.ui.tableWidget.item(selected, 1).text()
            lname = self.ui.tableWidget.item(selected, 2).text()
            age = self.ui.tableWidget.item(selected, 3).text()

            new_fname, ok1 = QtWidgets.QInputDialog.getText(self, "Изменить имя", "Имя:", text=fname)
            new_lname, ok2 = QtWidgets.QInputDialog.getText(self, "Изменить фамилию", "Фамилия:", text=lname)
            new_age, ok3 = QtWidgets.QInputDialog.getText(self, "Изменить возраст", "Возраст:", text=age)

            if ok1 and ok2 and ok3:
                # Обновляем запись
                execute_query("UPDATE people SET first_name=%s, last_name=%s, age=%s WHERE id=%s",
                              (new_fname, new_lname, new_age, id_val))
                self.load_data()
        else:
            QMessageBox.warning(self, "Внимание", "Выберите строку для изменения.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
