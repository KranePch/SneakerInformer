from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QCustomWidget(QWidget):
    def __init__ (self, text, img_path, parent = None):
        super(QCustomWidget, self).__init__(parent)

        # Init attributes
        self.textLabel = QLabel()
        self.imageLabel = QLabel()
        self.QHBoxLayout = QHBoxLayout()

        self.textLabel.setFont(QFont('SansSerif', 10, QFont.Bold))
        self.textLabel.setAlignment(Qt.AlignCenter)

        # Setup QHBoxLayout
        self.QHBoxLayout.addWidget(self.imageLabel, 0)
        self.QHBoxLayout.addWidget(self.textLabel, 1)
        self.setLayout(self.QHBoxLayout)

        self.setText(text)
        self.setImg(img_path)

    def setText(self, text):
        self.textLabel.setText(text)

    def setImg(self, img_path):
        self.imageLabel.setPixmap(QPixmap(img_path))
