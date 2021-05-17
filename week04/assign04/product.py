"""
File: product.py
Author: Alejandro Flores Medina

This file creates a class named Product which is a Product including id, name, price and quantity
"""


class Product:
    # Class definition
    def __init__(self, id, name, price, quantity):
        # Init the class variables
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def display(self):
        # Format the total round up to 2 decimals
        total = format(self.get_total_price(), ".2f")
        print(self.name + ' (' + str(self.quantity) + ') - $' + str(total))
