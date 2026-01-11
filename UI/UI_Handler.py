# UI_Handler.py
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget,
    QLabel,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timey")
        self.setGeometry(700, 300, 500, 500)
        self.mainlabel = QLabel(self)
        self.mainlayout = QVBoxLayout()
        self.mainWidget = QWidget()
        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.mainWidget)
        # self.mainlabel.setGeometry(0, 0, self.width(), self.height())
        self.mainlabel.setStyleSheet("background-color: red;")
        self.mainlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainlayout.addWidget(self.mainlabel)
        self.mainWidget.setLayout(self.mainlayout)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
