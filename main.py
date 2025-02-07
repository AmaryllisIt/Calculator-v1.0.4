from styles.mainwindow_ui import Ui_MainWindow
from styles.login_ui import Login_ui
from extentions.sotfunction import Statement_of_the_function
from extentions.tools import subfactorial, double_factorial, tetration, hash_encoder
from extentions.summation import Summation
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow, QWidget
from math import sin, cos, tan, asin, acos, atan
from math import e, pi, radians, factorial, cbrt, degrees
from math import log
import sqlite3
import ctypes
import sys
from datetime import date, datetime


name = None
start_time = datetime.now()


class FactorialError(Exception):
    pass


class RootError(Exception):
    pass


class Login(QWidget, Login_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Авторизация')
        self.setWindowIcon(QIcon('pictures/icon_main.ico'))
        self.messagebox = QMessageBox(self)
        self.btn_reg.clicked.connect(self.reg)
        self.btn_log.clicked.connect(self.log)

    def reg(self):
        with sqlite3.connect('data/BaseUsersData.sqlite3') as BaseUsersData:
            cursor = BaseUsersData.cursor()
            request = cursor.execute(f"SELECT name FROM user WHERE name == '{
                                     self.name.toPlainText()}'")
            user_info = [item for item in request]
            if not user_info and self.name.toPlainText() and self.hash.toPlainText():
                cursor.execute(f"INSERT INTO user(name, hash, birthday, equalcount, CountedTime) VALUES('{
                               self.name.toPlainText()}', '{hash_encoder(self.hash.toPlainText())}', '{date.today()}', 0, 0)")
                self.messagebox.setText(
                    'Вы успешно зарегестрировались! Попробуйте войти под своими данными.')
                self.messagebox.show()
            else:
                self.messagebox.setText(
                    'Такой аккаунт уже был зарегестрирован.')
                self.messagebox.show()

    def log(self):
        global name
        with sqlite3.connect('data/BaseUsersData.sqlite3') as BaseUsersData:
            cursor = BaseUsersData.cursor()
            request = cursor.execute(f"SELECT name, hash FROM user WHERE name = '{
                                     self.name.toPlainText()}'")
            user_info = [item for item in request]
            if user_info:
                if hash_encoder(self.hash.toPlainText()) == user_info[0][-1]:
                    name = user_info[0][0]
                    close_login()
                    open_Calculator()
                else:
                    self.messagebox.setText(
                        'Вы указали неверный логин или пароль. Попробуйте еще раз...')
                    self.messagebox.show()
            else:
                self.messagebox.setText(
                    'Такого аккаутна не существует. Попробуйте зарегистрироваться.')
                self.messagebox.show()


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.config()
        self.configurate_window()
        self.value: str

    def configurate_window(self):
        self.setWindowTitle('Одарённый калькулятор')
        self.setFixedSize(811, 461)
        self.setWindowIcon(QIcon('pictures/icon_main.ico'))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            'mycompany.myproduct.subproduct.version')

    def config(self):
        self.mainfield.setDisabled(True)
        self.fieldinfo.setDisabled(True)

        self.messageinfo = QMessageBox(self)
        self.messageinfo.setWindowTitle('Ошибка!!!')

        self.btn_1.clicked.connect(self.add_value)
        self.btn_2.clicked.connect(self.add_value)
        self.btn_3.clicked.connect(self.add_value)
        self.btn_4.clicked.connect(self.add_value)
        self.btn_5.clicked.connect(self.add_value)
        self.btn_6.clicked.connect(self.add_value)
        self.btn_7.clicked.connect(self.add_value)
        self.btn_8.clicked.connect(self.add_value)
        self.btn_9.clicked.connect(self.add_value)
        self.btn_0.clicked.connect(self.add_value)
        self.btn_point.clicked.connect(self.point)
        self.btn_plus.clicked.connect(self.baseOperations)
        self.btn_minus.clicked.connect(self.baseOperations)
        self.btn_mult.clicked.connect(self.baseOperations)
        self.btn_div.clicked.connect(self.baseOperations)
        self.btn_pow.clicked.connect(self.baseOperations)
        self.about.triggered.connect(self.info)
        self.Sotf.triggered.connect(self._openStatementOfTheFunction)
        self.summator.triggered.connect(self._openSummator)
        self.btn_eq.clicked.connect(self.equal)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_clearinfo.clicked.connect(self.clear_info)
        self.btn_e.clicked.connect(self.values)
        self.btn_pi.clicked.connect(self.values)
        self.btn_sin.clicked.connect(self.trigonometry)
        self.btn_cos.clicked.connect(self.trigonometry)
        self.btn_tg.clicked.connect(self.trigonometry)
        self.btn_arcsin.clicked.connect(self.trigonometry)
        self.btn_arccos.clicked.connect(self.trigonometry)
        self.btn_arctg.clicked.connect(self.trigonometry)
        self.btn_stfact.clicked.connect(self.factorial)
        self.btn_subfact.clicked.connect(self.factorial)
        self.btn_doubfact.clicked.connect(self.factorial)
        self.btn_sqrt.clicked.connect(self.root)
        self.btn_cubert.clicked.connect(self.root)
        self.btn_nroot.clicked.connect(self.root)
        self.btn_loge.clicked.connect(self.logarithm)
        self.btn_logab.clicked.connect(self.logarithm)
        self.btn_logdec.clicked.connect(self.logarithm)
        self.btn_plmin.clicked.connect(self.inversion)
        self.btn_tetra.clicked.connect(self.tetration)
        self.user.triggered.connect(self.about_account)
        
    def about_account(self):
        global name
        self.messageinfo.setWindowTitle('Информация об аккаунте')
        with sqlite3.connect('data/BaseUsersData.sqlite3') as BaseUsersData:
            cursor = BaseUsersData.cursor()
            info = cursor.execute(
                f"SELECT name, equalcount, birthday, CountedTime FROM user WHERE name = '{name}'")
            name, equalcount, birthday, counted_time = [
                item for item in info][0]
            birthday = birthday.split('-')
            birthday = '/'.join([birthday[2], birthday[1], birthday[0]])
        self.messageinfo.setText(f"Имя: {name}\nДата создания: {birthday}\nКоличество нажатий на равно: {
                                 equalcount}\nОбщее время: {round(counted_time, 2)} ч.")
        self.messageinfo.show()

    def point(self):
        if '.' not in self.mainfield.text():
            self.mainfield.setText(self.mainfield.text() + '.')

    def tetration(self):
        self.value = float(self.mainfield.text())
        self.fieldinfo.setText('Введите число: ')
        self.mainfield.setText('0')

    def inversion(self):
        if self.mainfield.text().startswith('-'):
            self.mainfield.setText(self.mainfield.text()[1:])
        else:
            self.mainfield.setText('-' + self.mainfield.text())

    def logarithm(self):
        if self.sender().objectName() == 'btn_loge':
            self.mainfield.setText(str(log(float(self.mainfield.text()), e)))
            self.fieldinfo.setText('')

        elif self.sender().objectName() == 'btn_logab':
            self.value = float(self.mainfield.text())
            self.mainfield.setText('0')
            self.fieldinfo.setText(f'Введите основание для logₓ{self.value}: ')
        elif self.sender().objectName() == 'btn_logdec':
            self.mainfield.setText(str(log(float(self.mainfield.text()), 10)))
            self.fieldinfo.setText('0')

    def root(self):
        if self.sender().objectName() == 'btn_sqrt':
            try:
                if float(self.mainfield.text()) < 0:
                    raise RootError(
                        'Невозможно получить действительное значение из отрицательного числа')
                if float(float(self.mainfield.text()) ** 0.5).is_integer():
                    self.mainfield.setText(
                        str(int(int(self.mainfield.text()) ** 0.5)))
                else:
                    self.mainfield.setText(
                        str(float(self.mainfield.text()) ** 0.5))
            except RootError as error:
                self.messageinfo.setText(error)
                self.messageinfo.show()
        elif self.sender().objectName() == 'btn_cubert':
            if cbrt(float(self.mainfield.text())).is_integer():
                self.mainfield.setText(
                    str(int(cbrt(int(self.mainfield.text())))))
            else:
                self.mainfield.setText(
                    str(cbrt(float(self.mainfield.text()))))
        elif self.sender().objectName() == 'btn_nroot':
            self.value = float(self.mainfield.text())
            self.mainfield.setText('0')
            self.fieldinfo.setText('Введите степень корня: ')

    def _openStatementOfTheFunction(self):
        open_Statement_of_the_function()

    def clear_info(self):
        self.fieldinfo.setText('')

    def factorial(self):
        try:
            if not (float(self.mainfield.text()).is_integer()):
                raise FactorialError('Значение должно быть целочисленным!')
            if self.sender().objectName() == 'btn_stfact':
                self.mainfield.setText(
                    str(factorial(int(self.mainfield.text()))))
            elif self.sender().objectName() == 'btn_doubfact':
                self.mainfield.setText(double_factorial(self.mainfield.text()))
            elif self.sender().objectName() == 'btn_subfact':
                self.mainfield.setText(subfactorial(self.mainfield.text()))
        except FactorialError:
            self.messageinfo.setWindowTitle('Ошибка значения')
            self.messageinfo.setText(f'Вы не можете использовать дробь для нахождения факториала, субфакториала, двойного факториала: {
                                     self.mainfield.text()} <---')
            self.messageinfo.show()

    def _openSummator(self):
        openSummator()

    def trigonometry(self):
        if self.sender().objectName() == 'btn_arccos':
            self.mainfield.setText(
                str(degrees(acos(radians(int(self.mainfield.text()))))))
        elif self.sender().objectName() == 'btn_arctg':
            self.mainfield.setText(
                str(degrees(atan(radians(int(self.mainfield.text()))))))
        else:
            try:
                if self.sender().objectName() == 'btn_sin':
                    self.mainfield.setText(
                        str(round(sin(radians(int(self.mainfield.text()))), 4)))
                elif self.sender().objectName() == 'btn_cos':
                    self.mainfield.setText(
                        str(round(cos(radians(int(self.mainfield.text()))), 4)))
                elif self.sender().objectName() == 'btn_tg':
                    self.mainfield.setText(
                        str(round(tan(degrees(int(self.mainfield.text()))), 4)))
                elif self.sender().objectName() == 'btn_arcsin':
                    self.mainfield.setText(
                        str(degrees(asin(radians(int(self.mainfield.text()))))))

            except ValueError:
                self.messageinfo.setWindowTitle('Ошибка значения')
                self.messageinfo.setText(f'Вы можете получить значение {
                    self.sender().objectName().split('_')[-1]} только из INT')
                self.messageinfo.show()

    def values(self):
        if self.sender().objectName() == 'btn_e':
            if self.mainfield.text() == '0' and str(round(e, 2)) not in self.mainfield.text():
                self.mainfield.setText(str(e))
        elif self.sender().objectName() == 'btn_pi':
            if self.mainfield.text() == '0' and str(round(pi, 4)) not in self.mainfield.text():
                self.mainfield.setText(str(pi))

    def delete(self):
        self.mainfield.setText(self.mainfield.text()[:-1])
        if self.mainfield.text() == '':
            self.mainfield.setText('0')

    def clear(self):
        self.mainfield.setText('0')
        self.fieldinfo.setText('')

    def info(self):
        self.messageinfo.setText(
            'Версия: 1.4.1 \nНазвание продукта: Одарённый калькулятор\nРазработчик: SARUGAKUZA (Фёдоров П. А.)')
        self.messageinfo.setWindowTitle('Version')
        self.messageinfo.show()

    def equal(self):
        try:
            if 'Введите степень корня' in self.fieldinfo.text():
                power = int(self.mainfield.text())
                if self.value < 0 and power % 2 == 0:
                    raise RootError(f'Невозможно извечь корень {
                                    power}-ой степени из отрицательного числа')
                self.mainfield.setText(str(self.value ** (1 / power)))
            elif 'Введите число:' in self.fieldinfo.text():
                count = int(self.mainfield.text())
                self.mainfield.setText(str(tetration(count, self.value)))
            elif 'Введите основание' in self.fieldinfo.text():
                base = float(self.mainfield.text())
                self.mainfield.setText(str(log(self.value, base)))

            elif 'Введите основание' not in self.fieldinfo.text() and 'Введите степень корня' not in self.fieldinfo.text():
                variable = eval(self.fieldinfo.text() + self.mainfield.text())
                if variable == int(variable):
                    self.mainfield.setText(str(int(variable)))
                else:
                    self.mainfield.setText(str(variable))

        except OverflowError as error:
            self.messageinfo.setText(
                'Результат получился большой и не помещается на калькуляторе.')
            self.messageinfo.show()
            self.mainfield.setText('0')

        except RootError as error:
            self.messageinfo.setText(str(error))
            self.messageinfo.show()
            self.mainfield.setText('0')

        except ZeroDivisionError:
            self.messageinfo.setText('Вы не можете делить на ноль!')
            self.messageinfo.show()
        finally:
            self.fieldinfo.setText('')

        with sqlite3.connect('data/BaseUsersData.sqlite3') as BaseUsersData:
            cursor = BaseUsersData.cursor()
            cursor.execute(
                f"UPDATE user SET equalcount = equalcount + 1 WHERE name = '{name}'")
            BaseUsersData.commit()

    def baseOperations(self):
        if self.sender().text() == '+':
            self.fieldinfo.setText(
                self.fieldinfo.text() + self.mainfield.text() + ' + ')
        elif self.sender().text() == '-':
            self.fieldinfo.setText(
                self.fieldinfo.text() + self.mainfield.text() + ' - ')
        elif self.sender().text() == 'x':
            self.fieldinfo.setText(
                self.fieldinfo.text() + self.mainfield.text() + ' * ')
        elif self.sender().text() == '/':
            self.fieldinfo.setText(
                self.fieldinfo.text() + self.mainfield.text() + ' / ')
        elif self.sender().text() == '**':
            self.fieldinfo.setText(
                self.fieldinfo.text() + self.mainfield.text() + ' ** ')
        self.mainfield.setText('0')
        self.fieldinfo.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.mainfield.setAlignment(Qt.AlignmentFlag.AlignRight)

    def add_value(self):
        if self.mainfield.text() == '0':
            self.mainfield.setText(self.sender().text())
        else:
            self.mainfield.setText(
                self.mainfield.text() + self.sender().text())

    def closeEvent(self, event):
        global start_time, name
        confirmation = QMessageBox.question(
            self, "Выход", "Вы точно хотите выйти (прогресс сохранится)?")
        if confirmation == 16384:
            end_time = datetime.now() - start_time
            with sqlite3.connect('data/BaseUsersData.sqlite3') as BaseUsersData:
                cursor = BaseUsersData.cursor()
                end_time = str(end_time).split(':')
                end_time = int(end_time[0]) + int(end_time[1]) / \
                    60 + round(float(end_time[2]) / 3600, 4)
                cursor.execute(
                    f"UPDATE user SET CountedTime = CountedTime + {end_time} WHERE name = '{name}'")

            event.accept()
            exit()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    ex = Calculator()
    summator = Summation()
    sotf = Statement_of_the_function()

    def openSummator():
        summator.show()

    def open_Statement_of_the_function():
        sotf.show()

    def open_Calculator():
        ex.show()

    def close_login():
        login.close()

    login.show()
    app.exec()
    
    
    
    
    
