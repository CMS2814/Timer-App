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
from Logic import Timer as coreTimerLogic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timey")
        self.setGeometry(700, 300, 500, 550)
        self.timerLogic = coreTimerLogic.Timer(10)
        self.currentMode = "Timer"

        # Main Properties
        self.mainWidget = QWidget(self)

        self.mainlayout = QVBoxLayout(self.mainWidget)

        # Top Section Properties
        # /---Widgets
        self.topWidget = QWidget(self.mainWidget)
        self.topBarWidget = QWidget(self.topWidget)
        # /---Buttons/Labels/Etc.
        self.currentModeTitle = QLabel("TIMER", self.topWidget)
        self.modeButton = QPushButton("Timer", self.topWidget)
        self.timeLabel = QLineEdit("00:00", self.topWidget)
        # /---Layouts
        self.topLayout = QVBoxLayout(self.topWidget)
        self.upperTopLayout = QHBoxLayout(self.topBarWidget)

        # Mid Section Properties
        # /---Widgets
        self.midWidget = QWidget(self.mainWidget)
        # /---Buttons/Labels/Etc.
        self.pickTime1 = QPushButton("10m", self.midWidget)
        self.pickTime2 = QPushButton("15m", self.midWidget)
        self.pickTime3 = QPushButton("30m", self.midWidget)
        # /---Layouts
        self.midLayout = QHBoxLayout(self.midWidget)

        # Bottom Section Properties
        # /---Widgets
        self.bottomWidget = QWidget(self.mainWidget)
        # /---Buttons/Labels/Etc.
        self.startButton = QPushButton("Start", self.bottomWidget)

        # /---Layouts
        self.bottomLayout = QHBoxLayout(self.bottomWidget)

        self.setCentralWidget(self.mainWidget)

        self.loadLayouts()
        self.loadStyles()
        self.checkButtonConnections()

    def loadStyles(self):
        # -------Sizes-----------------------
        # Top Widget
        self.currentModeTitle.setFixedSize(100, 50)
        self.timeLabel.setFixedSize(350, 100)
        self.modeButton.setFixedSize(75, 50)
        # Mid Widget
        self.pickTime1.setFixedSize(70, 70)
        self.pickTime2.setFixedSize(70, 70)
        self.pickTime3.setFixedSize(70, 70)
        # Bottom Widget
        self.startButton.setFixedSize(150, 75)
        # -------Alignments------------------
        # Top Widget
        self.currentModeTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Mid Widget
        # Bottom Top Widget

        # -------Styles----------------------
        self.mainWidget.setStyleSheet("background-color: white;")
        # Top Widget
        self.topWidget.setStyleSheet("background-color: red;")

        self.currentModeTitle.setStyleSheet(
            "background-color: lightgray; "
            "padding: 5px;"
            "border-radius: 5px;"
            "font-size: 20px;"
        )
        self.timeLabel.setStyleSheet(
            "background-color: gray;"
            "color: black;"
            "font-size: 65px;"
            "padding: 10px;"
        )

        self.modeButton.setStyleSheet("background-color: blue; font-size: 20px;")
        self.currentModeTitle.setFont(QFont("Arial"))
        # Mid Widget
        self.midWidget.setStyleSheet("background-color: green;")

        # Pick Time Labels-------
        pickTimeLabelStyle = (
            "background-color: yellow;"
            "color: black;"
            "font-size: 20px;"
            "border-radius: 35px;"
        )
        self.pickTime1.setStyleSheet(pickTimeLabelStyle)
        self.pickTime2.setStyleSheet(pickTimeLabelStyle)
        self.pickTime3.setStyleSheet(pickTimeLabelStyle)
        # Bottom Widget
        self.bottomWidget.setStyleSheet("background-color: blue;")

        self.startButton.setStyleSheet(
            "background-color: green; color: white;" "font-size: 25px;"
        )

    def loadLayouts(self):
        # Main Layout
        self.mainlayout.addWidget(self.topWidget)
        self.mainlayout.addWidget(self.midWidget)
        self.mainlayout.addWidget(self.bottomWidget)
        # Top Layout
        self.topLayout.addWidget(self.topBarWidget)

        self.topLayout.addWidget(
            self.timeLabel,
            alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom,
        )

        self.upperTopLayout.addWidget(self.modeButton)
        self.upperTopLayout.addWidget(
            self.currentModeTitle, alignment=Qt.AlignmentFlag.AlignLeft
        )
        self.upperTopLayout.setSpacing(95)  # default 95

        # Mid Layout
        self.midLayout.addWidget(self.pickTime1)
        self.midLayout.addWidget(self.pickTime2)
        self.midLayout.addWidget(self.pickTime3)
        # Bottom Layout
        self.bottomLayout.addWidget(self.startButton)

    def checkButtonConnections(self):
        self.modeButton.clicked.connect(self.onButtonClick)
        self.pickTime1.clicked.connect(self.onButtonClick)
        self.pickTime2.clicked.connect(self.onButtonClick)
        self.pickTime3.clicked.connect(self.onButtonClick)
        self.startButton.clicked.connect(self.onStartButtonClicked)

    def onStartButtonClicked(self):
        self.timeLabel.setText(str(self.timerLogic.duration))
        self.timerLogic.start()
        self.ticker()
        print("Start Button Clicked!")

    def ticker(self):
        self.qTimer = QTimer()
        self.qTimer.timeout.connect(self.updateUI)
        self.qTimer.start(10)

    def updateUI(self):
        remainingTime = self.timerLogic.updateTime()
        self.timeLabel.setText(str(round(remainingTime, 2)))

    def onButtonClick(self):
        print("Button clicked!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
