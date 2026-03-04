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


    
