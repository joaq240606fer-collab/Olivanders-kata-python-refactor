from src.types import (
    Item,
    ItemFactory,
    ItemNames,
    NormalItem,
    AgedBrieItem,
    BackstagePassesItem,
    Olivanders,
    SulfurasItem
)
items = [
    ItemFactory.create_item("Aged Brie", 2, 0),
    ItemFactory.create_item("Backstage passes to a TAFKAL80ETC concert", 20, 40),
    ItemFactory.create_item("Sulfuras, Hand of Ragnaros", 0, 80),
    ItemFactory.create_item("Conjured Mana Cake", 3, 6), # Usará NormalItem por defecto
]


gilded_rose = Olivanders(items)

gilded_rose.update_quality()

for item in items:
    print(item)