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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.time = 60

        self.setWindowTitle("Timey")
        self.setGeometry(700, 300, 500, 500)

        label = QLabel(str(self.time), self)
        label.setGeometry(0, 0, 230, 100)
        label.setFont(QFont("Arial", 40))
        label.setStyleSheet("color: blue;" "background-color: red;")

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_tick)
        self.timer.start(1000)  # Timer will tick every 1000 milliseconds (1 second)

    def timer_tick(self):
        print(self.time)
        self.time -= 1


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
