import csv


class Item:
    pay_rate = 0.8
    all = []

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def increment(self, value):
        self.__price += self.__price * value

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Name is too long!")
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __init__(self, name: str, price: float, quantity: int = 1):
        # Validate paramater
        assert price > 0, f"Price {price} cannot be empty!"
        assert quantity > 0, f"Quantity {quantity} cannot be empy!"

        self.__name = name
        self.__price = price
        self.__quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

    def calculate_total(self):
        return str(self.__price * self.__quantity)
