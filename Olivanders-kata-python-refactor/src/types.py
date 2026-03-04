class itenmsName:
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    DEFAULT = "Default Item"

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        """Método base. Las subclases lo sobrescribirán."""
        pass

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"

class NormalItem(Item):
    def update_quality(self):
        if self.quality > 0:
            self.quality -= 1
        self.sell_in -= 1
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality -= 1
    
class AgedBrieItem(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0:
            if self.quality < 50:
                self.quality += 1
class BackstagePassesItem(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
            if self.sell_in < 11:
                if self.quality < 50:
                    self.quality += 1
            if self.sell_in < 6:
                if self.quality < 50:
                    self.quality += 1
        
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0

class SulfurasItem(Item):
    def update_quality(self):
        pass

class olivanders:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()