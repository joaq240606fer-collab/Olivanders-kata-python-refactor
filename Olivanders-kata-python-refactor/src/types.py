class Oivanders (object):
    def __init__(self, items):
        self.items = items

    def updateQuality (self):
        for item in self.items:
            item.updateQuality()
    def getItems (self):
        return self.items


class Item(Document):

    def __init__(self,name,sell_in,quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __rerp__(self):
        
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


    
