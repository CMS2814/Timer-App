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
        self.setGeometry(700, 300, 500, 550)
        # self.mainlabel = QLabel(self)
        self.mainlayout = QVBoxLayout(self)
        self.mainWidget = QWidget(self)
        self.currentMode = QLabel("TIMER", self.mainWidget)
        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.mainWidget)
        self.currentMode.setFixedWidth(100)
        self.currentMode.setFixedHeight(50)
        self.currentMode.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.mainlabel.setGeometry(0, 0, self.width(), self.height())
        # self.mainlabel.setStyleSheet("background-color: red;" "font-size: 40px;")
        # self.mainlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.mainlayout.addWidget(self.mainlabel)
        self.mainlayout.addWidget(self.currentMode)
        self.mainWidget.setStyleSheet("background-color: white;")
        self.mainWidget.setLayout(self.mainlayout)

        # self.currentMode.setGeometry(0, 0, 1000, 50)
        self.currentMode.setStyleSheet("background-color: blue;")
        self.currentMode.setAlignment(Qt.AlignmentFlag.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
