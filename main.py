import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.rgbR.setValue(255)
        self.ui.rgbG.setValue(255)
        self.ui.rgbB.setValue(255)
        self.ui.rgbR.valueChanged.connect(self.slider_change)
        self.ui.rgbG.valueChanged.connect(self.slider_change)
        self.ui.rgbB.valueChanged.connect(self.slider_change)
        self.ui.take.clicked.connect(self.little_rectangle)
        self.show()

    def slider_change(self):
        r = self.ui.rgbR.value()
        g = self.ui.rgbG.value()
        b = self.ui.rgbB.value()

        self.ui.rgbRNum.setText(str(r))
        self.ui.rgbGNum.setText(str(g))
        self.ui.rgbBNum.setText(str(b))

        self.ui.rgbRectangle.setStyleSheet("background-color: rgb({}, {}, {});".format(r, g, b))

    def little_rectangle(self):
        r = self.ui.rgbR.value()
        g = self.ui.rgbG.value()
        b = self.ui.rgbB.value()

        self.ui.rgbTake.setStyleSheet("background-color: rgb({}, {}, {});".format(r, g, b))
        self.ui.rgbTake.setText(f"{r}, {g}, {b}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())

