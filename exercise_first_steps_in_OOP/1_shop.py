from typing import Union, Optional


class Shop:
    def __init__(self, name: str, items: Optional[list] = None):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)

