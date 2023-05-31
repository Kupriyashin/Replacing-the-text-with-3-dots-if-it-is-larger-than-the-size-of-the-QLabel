import sys

from PyQt5.QtGui import QFontMetrics
from loguru import logger

from exp import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # текст для вставки
        self.text = "0123456789_"

        # немного меняем окно, ничего важного
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_2.clear()
        self.ui.pushButton.clicked.connect(lambda: self.upgrade_text())

        logger.info(f"Длина текстовой строки в символах: {len(self.text)}")

        # узнаю количество символов, которое влезет в поле
        self.width = QFontMetrics(self.ui.label_2.font()).maxWidth()
        logger.info(f"Ширина текстового поля в символах: {self.width}")

    def upgrade_text(self):
        """
        Срабатывает при нажатии кнопки;
        Обрабатывает текст;
        Добавляет текст в label
        :return:
        """
        self.ui.label_2.setText(self.text[:int(self.width) - 3] + "..." if len(self.text) >= self.width else self.text)


if __name__ == '__main__':
    logger.info("Программа запускается")

    _app = QApplication(sys.argv)
    _app.setStyle("Fusion")
    _window = MainWindow()
    _window.show()

    logger.info("Программа запущена")

    sys.exit(_app.exec_())
