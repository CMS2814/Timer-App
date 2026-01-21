import sys
from PyQt5.QtWidgets import *
from functools import partial


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 400, 200)
        self.initUI()
        self.value = 0

    def initUI(self):
        self.button1 = QPushButton(self)
        self.button1.setGeometry(40, 40, 100, 50)
        self.button1.setText("Button 1")

        self.button2 = QPushButton(self)
        self.button2.setGeometry(150, 40, 100, 50)
        self.button2.setText("Button 2")

        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.button1)
        self.btn_grp.addButton(self.button2)

        self.btn_grp.buttonClicked.connect(self.on_click)

        self.show()

    def on_click(self, btn):
        if btn.text() == "Button 1":
            self.value = 1
            print(self.value)
        elif btn.text() == "Button 2":
            self.value = 2
            print(self.value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
