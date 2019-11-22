class Shoe:
    def __init__(self, id, name, brand, img, price, desp, websites):
        self.id = id
        self.name = name
        self.brand = brand
        self.img = img
        self.price = price
        self.desp = desp
        self.websites = websites

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getBrand(self):
        return self.brand

    def getDesp(self):
        return self.desp

    def getPrice(self):
        return self.price

    def getImg(self, img):
        return self.img

    def getWebsites(self, websites):
        return self.websites

    def setID(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setBrand(self, brand):
        self.brand = brand

    def setDesp(self, desp):
        self.desp = desp

    def setPrice(self, price):
        self.price = price

    def setImg(self, img):
        self.img = img

    def setWebsites(self, websites):
        self.websites = websites

    def __str__(self):
        text = '\n'
        text += self.name + '/ ' + self.brand + '/ ' + self.img + '/ ' + self.price + '/ ' + self.desp
        for website in self.websites:
            text += '/ ' + website
        return text
