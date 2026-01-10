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
from datetime import datetime
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Nothing", self)
        self.setWindowTitle("Timey")
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150, 100, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.onPress)

        self.label.setGeometry(200, 225, 100, 50)
        self.label.setStyleSheet("background-color: Red;" "font-size: 20px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def onPress(self):
        print("Button pressed!")
        self.label.setText("Pressed!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
