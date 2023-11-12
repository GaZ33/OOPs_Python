class item(object):
    def __init__(self, name: str, quantity: float, price=0):
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Price {quantity} is not greater or equal to zero"
        self.name = name
        self.quantity = quantity
        self.price = price
    def calculate_total_price(self):
        return self.quantity * self.price






item1 = item("phone", 3, 1000)
