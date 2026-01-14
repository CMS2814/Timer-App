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
        # Top Widget
        self.currentModeTitle = QLabel("TIMER", self.topWidget)
        self.modeButton = QPushButton("Timer", self.topWidget)
        self.timeLabel = QLineEdit("00:00", self.topWidget)
        # Mid Widget
        self.pickTime1 = QPushButton("10m", self.midWidget)
        self.pickTime2 = QPushButton("15m", self.midWidget)
        self.pickTime3 = QPushButton("30m", self.midWidget)
        # Bottom Widget
        self.startButton = QPushButton("Start", self.bottomWidget)

        # Layouts
        self.mainlayout = QVBoxLayout(self.mainWidget)
        self.topLayout = QVBoxLayout(self.topWidget)
        self.midLayout = QHBoxLayout(self.midWidget)
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
        self.topLayout.addWidget(
            self.modeButton,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
        )
        self.topLayout.addWidget(
            self.currentModeTitle,
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

    def checkButtonConnections(self):
        self.pickTime1.clicked.connect(self.onButtonClick)
        self.pickTime2.clicked.connect(self.onButtonClick)
        self.pickTime3.clicked.connect(self.onButtonClick)
        self.startButton.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        print("Button clicked!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
