from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Shoe import *

class InputShoeDialog(QWidget):
   def __init__(self, parent = None):
      super(InputShoeDialog, self).__init__(parent)

      layout = QFormLayout()

      self.input_name = QLineEdit()
      self.input_name.setFixedSize(200, 30)
      layout.addRow(self.input_name)
      self.input_image = QLineEdit()
      self.input_image.setFixedSize(200, 30)
      layout.addRow(self.input_image)
      self.input_brand = QLineEdit()
      self.input_brand.setFixedSize(200, 30)
      layout.addRow(self.input_brand)
      self.input_price = QLineEdit()
      self.input_price.setFixedSize(200, 30)
      layout.addRow(self.input_price)
      self.input_desp = QLineEdit()
      self.input_desp.setFixedSize(200, 30)
      layout.addRow(self.input_desp)
      self.input_web = QLineEdit()
      self.input_web.setFixedSize(200, 30)
      layout.addRow(self.input_web)

      self.setLayout(layout)

   def getInfo(self):
      return Shoe(None, self.input_name.text(), self.input_brand.text(), self.input_image.text(),
         self.input_price.text(), self.input_desp.text(), [self.input_web.text()])
