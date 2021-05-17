"""
File: order.py
Author: Alejandro Flores Medina

This file creates a class named Order which creates a new Order and holds an id and the list of products
"""

from product import Product


class Order:
    # Class definition
    def __init__(self):
        # Init the class variables
        self.id = ""
        self.products = []

    def get_subtotal(self):
        subtotal = 0
        # Iterate over all list elements and sum up the total price
        for product in self.products:
            subtotal += product.get_total_price()

        return subtotal

    def get_tax(self):
        # Calculate the tax of 6.5% from the subtotal
        tax = self.get_subtotal() * 0.065
        return tax

    def get_total(self):
        # Sum the subtotal plus the tax
        total = self.get_subtotal() + self.get_tax()
        return total

    def add_product(self, product):
        # Append a new product to the Products list
        self.products.append(product)

    def display_receipt(self):
        print('Order: ' + str(self.id))
        for product in self.products:
            product.display()
        print('Subtotal: $' + str(format(self.get_subtotal(), ".2f")))
        print('Tax: $' + str(format(self.get_tax(), ".2f")))
        print('Total: $' + str(format(self.get_total(), ".2f")))
