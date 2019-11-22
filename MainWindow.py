from PyQt5 import QtWidgets, uic, QtCore ,QtGui

from QCustomWidget import *
from Shoe import *
from InputShoeDialog import *

import sys

PATH = 'pics\\'

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        # Init attributes
        QMainWindow.__init__(self, None)
        self.count_id = 0
        self.shoe_list = []
        self.current_brand = None
        

        # Load UI
        form = uic.loadUi('bey.ui', self)

        # Init shoes
        self.initShoes()

        # Init Text edit
        self.textEdit = form.findChild(QTextEdit, "textEdit")
        self.textEdit.setReadOnly(True)

        # Init list widget
        self.myQListWidget = form.findChild(QListWidget, "listWidget")
        self.myQListWidget.itemClicked.connect(self.clicked)
        self.addShoeWidget(self.shoe_list)

        # Init Buttons
        self.myAllButton = form.findChild(QPushButton, "allButton")
        self.myAllButton.clicked.connect(self.handleAllButton)
        self.myNikeButton = form.findChild(QPushButton, "nikeButton")
        self.myNikeButton.clicked.connect(self.handleNikeButton)
        self.myAdidasButton = form.findChild(QPushButton, "adidasButton")
        self.myAdidasButton.clicked.connect(self.handleAdidasButton)
        self.myVansButton = form.findChild(QPushButton, "vansButton")
        self.myVansButton.clicked.connect(self.handleVansButton)
        self.myBalenButton = form.findChild(QPushButton, "balenButton")
        self.myBalenButton.clicked.connect(self.handleBalenButton)
        self.myAddButton = form.findChild(QPushButton, "addButton")
        self.myAddButton.clicked.connect(self.handleAddButton)

        self.myQWidget = form.findChild(QWidget, "inputWidget")
        self.myInputWidget = InputShoeDialog(self.myQWidget)

        self.show()

    def initShoes(self):
        # Read data file
        file = open("shoe_db.txt", "r")
        shoe_data = file.readlines()

        for shoe in shoe_data:
            # Extract data from a line of file
            data = shoe.split('/ ')
            id = self.count_id
            name = data[0]
            brand = data[1]
            img = data[2]
            price = data[3]
            desp = data[4]
            websites = []
            for i in range(5, len(data)):
                websites.append(data[i])

            # Init a shoe
            myShoe = Shoe(id, name, brand, img, price, desp, websites)
            self.shoe_list.append(myShoe)
            self.count_id += 1
        file.close()

    def addShoeWidget(self, shoe_list):
        for shoe in shoe_list:
            self.addShoe(shoe)

    def addShoe(self, shoe):
        cw = QCustomWidget(shoe.name, PATH+shoe.img)

        ql = QListWidgetItem(self.myQListWidget)
        ql.setSizeHint(cw.sizeHint())

        self.myQListWidget.setItemWidget(ql, cw)

    def findShoe(self, row, brand):
        if brand == None:
            return self.shoe_list[row]
        shoes = self.getShoesByBrand(brand)
        return shoes[row]

    def clicked(self, item):
        row = item.listWidget().row(item)
        shoe = self.findShoe(row, self.current_brand)
        self.updateTextEdit(shoe)

    def getShoesByBrand(self, brand):
        shoes = []
        for shoe in self.shoe_list:
            if shoe.getBrand() == brand:
                shoes.append(shoe)
        return shoes

    def handleAllButton(self):
        self.current_brand = None
        self.myQListWidget.clear()
        self.addShoeWidget(self.shoe_list)

    def handleNikeButton(self):
        self.current_brand = 'nike'
        self.myQListWidget.clear()
        shoes = self.getShoesByBrand('nike')
        self.addShoeWidget(shoes)

    def handleAdidasButton(self):
        self.current_brand = 'adidas'
        self.myQListWidget.clear()
        shoes = self.getShoesByBrand('adidas')
        self.addShoeWidget(shoes)

    def handleVansButton(self):
        self.current_brand = 'vans'
        self.myQListWidget.clear()
        shoes = self.getShoesByBrand('vans')
        self.addShoeWidget(shoes)

    def handleBalenButton(self):
        self.current_brand = 'balenciaga'
        self.myQListWidget.clear()
        shoes = self.getShoesByBrand('balenciaga')
        self.addShoeWidget(shoes)

    def handleAddButton(self):
        shoe = self.myInputWidget.getInfo()
        shoe.setID(self.count_id)
        self.count_id += 1
        self.shoe_list.append(shoe)
        self.handleAllButton()
        self.addShoeToFile(shoe)

    def addShoeToFile(self, shoe):
        file = open("shoe_db.txt", "a+")
        file.write(str(shoe))
        file.close()

    def updateTextEdit(self, shoe):
        text = ""
        text += "<b>Name:</b><br/><br/>" + shoe.getName()
        text += "<br/><br/><b>Price:</b><br/><br/>" + shoe.getPrice()
        text += "<br/><br/><b>Description:</b><br/><br/>" + shoe.getDesp()
        text += "<br/><br/><b>Websites:</b>"
        for website in shoe.websites:
            text += "<br/><br/>" + website

        self.textEdit.setText(text)
        
def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
