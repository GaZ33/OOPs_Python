import csv
class item(object):
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, quantity: float, price=0):
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Price {quantity} is not greater or equal to zero"
        self.name = name
        self.quantity = quantity
        self.price = price

        item.all.append(self.name)

    def __repr__(self):
        return f"item('{self.name}, {self.price}, {self.quantity}')"
    
    @classmethod
    def instancied_from_csv(cls):
        with open('item.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
            for Item in items:
                item(
                    name=Item.get("name"),
                    quantity=int(Item.get('quantity')),
                    price=float(Item.get('price')),
                )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def apply_discount(self):
        self.price =  self.price * self.pay_rate
        
    def calculate_total_price(self):
        return self.quantity * self.price
    

item.instancied_from_csv()
print(item.all)