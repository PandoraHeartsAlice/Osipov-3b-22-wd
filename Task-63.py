class ProductCard:
    def __init__(self, name, cost, quantity):
        self.name = name
        self._cost = cost
        self._quantity = quantity

    def decrease_quantity(self, amount):
        if amount <= self._quantity:
            self._quantity -= amount
            print(
                f"The quantity of {self.name} has been decreased by {amount}.")
        else:
            print(f"Not enough {self.name} in stock.")

    def change_cost(self, new_cost):
        if new_cost >= 0:
            self._cost = new_cost
            print(f"The cost of {self.name} has been changed to {new_cost}.")
        else:
            print("Invalid cost value.")

    def get_cost(self):
        return self._cost

    def get_quantity(self):
        return self._quantity


product = ProductCard("Product 1", 10, 100)
# The quantity of Product 1 has been decreased by 50.
product.decrease_quantity(50)
product.decrease_quantity(70)  # Not enough Product 1 in stock.

product.change_cost(20)  # The cost of Product 1 has been changed to 20.
product.change_cost(-5)  # Invalid cost value.

cost = product.get_cost()
quantity = product.get_quantity()
print(cost)  # 20
print(quantity)  # 80
