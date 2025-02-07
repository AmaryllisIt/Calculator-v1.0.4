from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication
import sys
from pyqtgraph import PlotWidget
from PyQt6 import QtCore, QtGui, QtWidgets
from math import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.graphicsView = PlotWidget(parent=Form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 1261, 551))
        self.graphicsView.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.graphicsView.setToolTipDuration(-1)
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(150, 600, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("255, 255, 255")
        self.label.setObjectName("label")
        self.function = QtWidgets.QTextEdit(parent=Form)
        self.function.setGeometry(QtCore.QRect(140, 650, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.function.setFont(font)
        self.function.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.CursorShape.SplitHCursor))
        self.function.setObjectName("function")
        self.btn_build = QtWidgets.QPushButton(parent=Form)
        self.btn_build.setGeometry(QtCore.QRect(420, 590, 121, 51))
        self.btn_build.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_build.setObjectName("btn_build")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(-10, -10, 1291, 731))
        self.label_2.setStyleSheet("white")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pictures/background.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(80, 650, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("255, 255, 255")
        self.label_3.setObjectName("label_3")
        self.info = QtWidgets.QLabel(parent=Form)
        self.info.setGeometry(QtCore.QRect(580, 650, 671, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.info.setFont(font)
        self.info.setStyleSheet("255, 255, 255")
        self.info.setObjectName("info")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(850, 600, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("255, 255, 255")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(630, 600, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("255, 255, 255")
        self.label_5.setObjectName("label_5")
        self.start = QtWidgets.QTextEdit(parent=Form)
        self.start.setGeometry(QtCore.QRect(630, 640, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start.setFont(font)
        self.start.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.CursorShape.SplitHCursor))
        self.start.setObjectName("start")
        self.stop = QtWidgets.QTextEdit(parent=Form)
        self.stop.setGeometry(QtCore.QRect(850, 640, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.stop.setFont(font)
        self.stop.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.CursorShape.SplitHCursor))
        self.stop.setObjectName("stop")
        self.label_2.raise_()
        self.graphicsView.raise_()
        self.label.raise_()
        self.function.raise_()
        self.btn_build.raise_()
        self.label_3.raise_()
        self.info.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.start.raise_()
        self.stop.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate(
            "Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Введите функцию f(x):</span></p></body></html>"))
        self.btn_build.setText(_translate("Form", "Построить"))
        self.label_3.setText(_translate(
            "Form", "<html><head/><body><p><span style=\" color:#ffffff;\">f(x) = </span></p></body></html>"))
        self.info.setText(_translate(
            "Form", "<html><head/><body><p/></body></html>"))
        self.label_4.setText(_translate(
            "Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Максимальный X</span></p></body></html>"))
        self.label_5.setText(_translate(
            "Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Минимальный X</span></p></body></html>"))
        self.start.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-100</p></body></html>"))
        self.stop.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>"))


class Statement_of_the_function(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1280, 720)
        self.setWindowTitle('График функции')
        self.btn_build.clicked.connect(self.build_function)
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle('Ошибка!')

    def build_function(self):
        self.graphicsView.clear()
        try:
            function = self.function.toPlainText()
            start, stop = int(self.start.toPlainText()), int(self.stop.toPlainText()) + 1
            self.graphicsView.plot([x for x in range(start, stop)], [eval(
                function.replace('x', f'(x)')) for x in range(start, stop)], pen='r')
        except:
            self.messagebox.setText(f'Не удалось построить функцию "{self.function.toPlainText()}". Попробуйте изменить функцию или диапазон.')
            self.messagebox.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Statement_of_the_function()
    ex.show()
    exit(app.exec())
    
