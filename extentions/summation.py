from PyQt6.QtWidgets import QWidget
from styles.summator_ui import Ui_Form
from PyQt6.QtGui import QIcon


class Summation(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(613, 430)
        self.setWindowIcon(QIcon('pictures/icon_summation.ico'))
        self.setWindowTitle('Суммирование')
        self.start.setText("0")
        self.stop.setText("10")
        self.btn_startSum.clicked.connect(self.evaluate)

    def evaluate(self):
        result = 0.0
        start, stop = int(self.start.toPlainText()), int(self.stop.toPlainText())
        for x in range(start, stop + 1):
            result += eval(str(self.value.toPlainText().replace('x', str(x))))
        self.result.setText(str(result if not result.is_integer() else int(result)))
            
        