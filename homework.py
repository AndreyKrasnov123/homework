class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

class Payment:
    def process_payment(self, amount):
        return f"Заказ успешно обработан! ${amount}"

class Database:
    def __init__(self):
        self.orders = []

    def save_order(self, order):
        self.orders.append(order)
        return "Заказ успешно обработан!"

pizza1 = Pizza("Pepperoni", 10)
pizza2 = Pizza("Margarita", 8)

order = Order()
order.add_item(pizza1)
order.add_item(pizza2)

total_price = order.calculate_total()

payment = Payment()
payment_result = payment.process_payment(total_price)

database = Database()
database.save_order(order)

print(payment_result)
print("Coxraneno")
