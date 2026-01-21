# UI_Handler.py
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import QTimer, Qt
from Logic import Timer as coreTimerLogic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timey")
        self.setGeometry(700, 300, 500, 550)
        self.setFixedSize(500, 550)
        self.timerLogic = coreTimerLogic.Timer()  # Always set to zero
        self.stopwatchLogic = coreTimerLogic.Stopwatch()
        self.currentMode = "Timer"  # Timer or Stopwatch

        # Main Properties
        self.mainWidget = QWidget(self)

        self.mainlayout = QVBoxLayout(self.mainWidget)

        # Top Section Properties
        # /---Widgets
        self.topWidget = QWidget(self.mainWidget)
        self.topBarWidget = QWidget(self.topWidget)
        # /---Buttons/Labels/Etc.
        self.currentModeTitle = QLabel("TIMER", self.topWidget)
        self.modeButton = QPushButton("Stopwatch", self.topWidget)
        self.timeLabel = QLineEdit("Enter Time(s)", self.topWidget)
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

        self.pickTimeButtonGroup = QButtonGroup()
        self.pickTimeButtonGroup.setExclusive(True)

        self.pickTimeButtonGroup.addButton(self.pickTime1)
        self.pickTimeButtonGroup.addButton(self.pickTime2)
        self.pickTimeButtonGroup.addButton(self.pickTime3)
        # /---Layouts
        self.midLayout = QHBoxLayout(self.midWidget)

        # Bottom Section Properties
        # /---Widgets
        self.bottomWidget = QWidget(self.mainWidget)
        # /---Buttons/Labels/Etc.
        self.primaryButton = QPushButton("Start", self.bottomWidget)
        self.secondaryButton = QPushButton("Reset", self.bottomWidget)

        # /---Layouts
        self.bottomLayout = QHBoxLayout(self.bottomWidget)

        self.setCentralWidget(self.mainWidget)

        self.loadLayouts()
        self.loadStyles()
        self.checkButtonConnections()

    def loadStyles(self):
        # -------States---------------------
        self.secondaryButton.setHidden(True)
        # -------Sizes-----------------------
        # Top Widget
        self.timeLabel.setFixedSize(425, 100)
        self.currentModeTitle.setFixedSize(150, 50)
        self.modeButton.setFixedSize(115, 50)
        # Mid Widget
        self.pickTime1.setFixedSize(70, 70)
        self.pickTime2.setFixedSize(70, 70)
        self.pickTime3.setFixedSize(70, 70)
        # Bottom Widget
        self.primaryButton.setFixedSize(150, 75)
        self.secondaryButton.setFixedSize(150, 75)
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

        self.primaryButton.setStyleSheet(
            "background-color: green; color: white;" "font-size: 25px;"
        )
        self.secondaryButton.setStyleSheet(
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
        self.upperTopLayout.setSpacing(35)  # default 35

        # Mid Layout
        self.midLayout.addWidget(self.pickTime1)
        self.midLayout.addWidget(self.pickTime2)
        self.midLayout.addWidget(self.pickTime3)
        # Bottom Layout
        self.bottomLayout.addWidget(self.secondaryButton)
        self.bottomLayout.addWidget(self.primaryButton)

    def checkButtonConnections(self):
        self.modeButton.clicked.connect(self.onModeButtonClick)
        self.pickTimeButtonGroup.buttonClicked.connect(self.onPickTimeClicked)
        self.primaryButton.clicked.connect(self.onPrimaryButtonClicked)
        self.secondaryButton.clicked.connect(self.onSecondaryButtonClicked)

    def onPrimaryButtonClicked(self):  # Orignilly start button
        if self.currentMode == "Timer":
            if not self.timerLogic.isStarted:
                try:
                    timerDuration = int(self.timeLabel.text())
                    self.timerLogic = coreTimerLogic.Timer(timerDuration)
                    self.timeLabel.setText(str(self.timerLogic.duration))
                except ValueError:
                    self.timeLabel.setText("Enter Time(s)")

                self.timerLogic.start()
                if self.timerLogic.isStarted:
                    self.ticker()
                    self.primaryButton.setText("Pause")
                    self.secondaryButton.setHidden(False)
            elif not self.timerLogic.isPaused and self.timerLogic.isStarted:
                self.timerLogic.pause()
                self.primaryButton.setText("Resume")

            elif self.timerLogic.isPaused and self.timerLogic.isStarted:
                self.timerLogic.resume()
                self.primaryButton.setText("Pause")
        elif self.currentMode == "Stopwatch":
            if not self.stopwatchLogic.isStarted:
                self.stopwatchLogic.start()
                self.ticker()
                self.primaryButton.setText("Pause")
                self.secondaryButton.setHidden(False)
            elif not self.stopwatchLogic.isPaused and self.stopwatchLogic.isStarted:
                self.stopwatchLogic.pause()
                self.primaryButton.setText("Resume")
            elif self.stopwatchLogic.isPaused and self.stopwatchLogic.isStarted:
                self.stopwatchLogic.resume()
                self.primaryButton.setText("Pause")

    def onSecondaryButtonClicked(self):  # Originally reset Button
        if self.currentMode == "Timer":
            if self.timerLogic.isStarted:
                self.timerLogic.reset()
                self.primaryButton.setText("Start")
                self.secondaryButton.setHidden(True)
                self.timeLabel.setText("Enter Time(s)")
        elif self.currentMode == "Stopwatch":
            if self.stopwatchLogic.isStarted and self.stopwatchLogic.isPaused:
                self.stopwatchLogic.reset()
                self.primaryButton.setText("Start")
                self.secondaryButton.setHidden(True)
                self.timeLabel.setText("0")

    def onPickTimeClicked(self, button: QPushButton):
        if button.text() == "10m":
            self.timeLabel.setText(str(10 * 60))
        elif button.text() == "15m":
            self.timeLabel.setText(str(15 * 60))
        elif button.text() == "30m":
            self.timeLabel.setText(str(30 * 60))

    def ticker(self):
        self.qTimer = QTimer()
        self.qTimer.start(1)
        self.qTimer.timeout.connect(self.updateUI)

    def updateUI(self):
        if self.currentMode == "Timer":
            if self.timerLogic.isPaused:
                return
            print(self.timerLogic.isPaused)
            remainingTime = self.timerLogic.updateTime()
            self.timeLabel.setText(remainingTime)
            if (
                not self.timerLogic.isStarted
            ):  # Hides secondaryButton when timer finished
                self.qTimer.stop()
                self.secondaryButton.setHidden(True)
                self.primaryButton.setText("Start")
            print("UI updated")
        elif self.currentMode == "Stopwatch":
            if self.stopwatchLogic.isPaused:
                return
            print(self.stopwatchLogic.isPaused)
            elapsedTime = self.stopwatchLogic.updateTime()
            self.timeLabel.setText(elapsedTime)
            print("UI updated")

    def onModeButtonClick(self):
        print(self.currentMode)
        if self.currentMode == "Timer":
            self.currentMode = "Stopwatch"
            self.currentModeTitle.setText("STOPWATCH")
            self.modeButton.setText("Timer")

            self.pickTime1.setHidden(True)
            self.pickTime2.setHidden(True)
            self.pickTime3.setHidden(True)
        elif self.currentMode == "Stopwatch":
            self.currentMode = "Timer"
            self.currentModeTitle.setText("TIMER")
            self.modeButton.setText("Stopwatch")
            self.pickTime1.setHidden(False)
            self.pickTime2.setHidden(False)
            self.pickTime3.setHidden(False)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
