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
        # Labels/LineEdits/Buttons
        self.currentMode = QLabel("TIMER", self.topWidget)

        self.timeLabel = QLineEdit("00:00", self.midWidget)

        self.pickTime1 = QPushButton("10m", self.midWidget)
        self.pickTime2 = QPushButton("15m", self.midWidget)
        self.pickTime3 = QPushButton("30m", self.midWidget)

        self.startButton = QPushButton("Start", self.bottomWidget)
        # Layouts
        self.mainlayout = QVBoxLayout(self.mainWidget)
        self.topLayout = QVBoxLayout(self.topWidget)
        self.midLayout = QHBoxLayout(self.midWidget)
        self.bottomLayout = QHBoxLayout(self.bottomWidget)

        self.setCentralWidget(self.mainWidget)

        self.loadLayouts()
        self.loadStyles()

    def loadStyles(self):
        # -------Sizes-----------------------
        self.currentMode.setFixedSize(100, 50)
        self.timeLabel.setFixedSize(350, 100)
        self.pickTime1.setFixedSize(70, 70)
        self.pickTime2.setFixedSize(70, 70)
        self.pickTime3.setFixedSize(70, 70)
        # -------Alignments------------------
        self.currentMode.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # -------Styles----------------------
        # Current Mode Label--------
        self.currentMode.setStyleSheet(
            "background-color: lightgray; "
            "padding: 5px;"
            "border-radius: 5px;"
            "font-size: 20px;"
        )
        self.currentMode.setFont(QFont("Arial"))

        # Widget Labels---------
        self.mainWidget.setStyleSheet("background-color: white;")
        self.topWidget.setStyleSheet("background-color: red;")
        self.midWidget.setStyleSheet("background-color: green;")
        self.bottomWidget.setStyleSheet("background-color: blue;")

        # Time Label------------
        self.timeLabel.setStyleSheet(
            "background-color: gray;"
            "color: black;"
            "font-size: 65px;"
            "padding: 10px;"
        )
        # Pick Time Labels-------
        timeLabelStyle = (
            "background-color: yellow;"
            "color: black;"
            "font-size: 20px;"
            "border-radius: 35px;"
        )
        # Time Pick 1
        self.pickTime1.setStyleSheet(timeLabelStyle)
        # self.pickTime1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pickTime1.clicked.connect(self.onButtonClick)
        # Time Pick 2
        self.pickTime2.setStyleSheet(timeLabelStyle)
        # self.pickTime2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pickTime2.clicked.connect(self.onButtonClick)
        # Time Pick 3
        self.pickTime3.setStyleSheet(timeLabelStyle)
        # self.pickTime3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pickTime3.clicked.connect(self.onButtonClick)
        # self.mainlayout.addWidget(self.currentMode)

        # Start Button-----------------------
        self.startButton.setStyleSheet(
            "background-color: green; color: white;" "font-size: 25px;"
        )
        self.startButton.setFixedSize(150, 75)

    def loadLayouts(self):
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
        self.midLayout.addWidget(self.pickTime1)
        self.midLayout.addWidget(self.pickTime2)
        self.midLayout.addWidget(self.pickTime3)
        # Bottom Layout
        self.bottomLayout.addWidget(self.startButton)

    def onButtonClick(self):
        print("Button clicked!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
