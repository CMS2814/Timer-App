import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer
from datetime import datetime
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.time = 5
        self.goal = 60
        self.watch = 0

        self.setWindowTitle("Timey")
        self.setGeometry(700, 300, 500, 500)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 230, 100)
        self.label.setFont(QFont("Arial", 40))
        self.label.setStyleSheet("color: blue;" "background-color: red;")

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_tick)
        self.timer.start(1000)  # Timer will tick every 1000 milliseconds (1 second)

    def timer_tick(self):
        timer_text = time.strftime("%H:%M:%S", time.gmtime(self.time))

        self.time -= 1
        self.label.setText(timer_text)

    def stopwatch(self):
        timer_text = time.strftime("%H:%M:%S", time.gmtime(self.watch))

        self.watch += 1
        self.label.setText(timer_text)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
