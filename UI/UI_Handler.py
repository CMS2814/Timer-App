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
    QLineEdit,
)
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import QTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timey")
        self.setGeometry(700, 300, 500, 550)
        # self.mainlabel = QLabel(self)
        self.mainWidget = QWidget(self)
        self.topWidget = QWidget(self.mainWidget)
        self.midWidget = QWidget(self.mainWidget)
        self.bottomWidget = QWidget(self.mainWidget)
        # Labels
        self.currentMode = QLabel("TIMER", self.topWidget)
        self.timeLabel = QLabel("00:00", self.midWidget)
        # Layouts
        self.mainlayout = QVBoxLayout(self.mainWidget)
        self.topLayout = QVBoxLayout(self.topWidget)
        self.midLayout = QVBoxLayout(self.midWidget)
        self.bottomLayout = QHBoxLayout(self.bottomWidget)

        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.mainWidget)
        # Styles
        # Current Mode Label
        self.currentMode.setFixedWidth(100)
        self.currentMode.setFixedHeight(50)
        self.currentMode.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currentMode.setStyleSheet(
            "background-color: lightgray; padding: 5px; border-radius: 5px;"
            "font-size: 20px;"
        )
        self.currentMode.setFont(QFont("Arial"))
        # Widget Labels
        self.mainWidget.setStyleSheet("background-color: white;")
        self.topWidget.setStyleSheet("background-color: red;")
        self.midWidget.setStyleSheet("background-color: green;")
        self.bottomWidget.setStyleSheet("background-color: blue;")
        # Time Label
        self.timeLabel.setStyleSheet(
            "background-color: gray;"
            "color: black;"
            "font-size: 65px;"
            "padding: 10px;"
        )
        self.timeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeLabel.setFixedSize(350, 100)
        # self.mainlayout.addWidget(self.currentMode)
        # Layout properties
        # Main Layout
        self.mainlayout.addWidget(self.topWidget)
        self.mainlayout.addWidget(self.midWidget)
        self.mainlayout.addWidget(self.bottomWidget)
        # Top Layout
        self.topLayout.addWidget(
            self.currentMode,
            alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop,
        )
        self.topLayout.addWidget(
            self.timeLabel,
            alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom,
        )
        # Mid Layout

        # Bottom Layout


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
