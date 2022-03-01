from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, broken: bool = False):
        super().__init__(name, price, quantity)

        self.broken = broken
