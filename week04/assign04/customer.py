"""
File: customer.py
Author: Alejandro Flores Medina

This file creates a class named Customer which holds customer name, id and the list of orders
"""

from order import Order


class Customer:
    # Class definition
    def __init__(self):
        # Init the class variables
        self.id = ""
        self.name = ""
        self.orders = []

    def get_order_count(self):
        # Return the orders list length
        return len(self.orders)

    def get_total(self):
        total = 0
        # Iterate over the orders list and sum up the total
        for order in self.orders:
            total += order.get_total()

        return total

    def add_order(self, order):
        # Append a new order to the orders list
        self.orders.append(order)

    def display_summary(self):
        print("Summary for customer '" + str(self.id + "':"))
        print('Name: ' + self.name)
        print('Orders: ' + str(self.get_order_count()) )
        print('Total: $' + str(format(self.get_total(), ".2f")))

    def display_receipts(self):
        print("Detailed receipts for customer '" + str(self.id + "':"))
        print('Name: ' + self.name + '\n')
        order_proccessed = 0
        
        # Iterate over each order from orders list
        for order in self.orders:
            order.display_receipt()
            order_proccessed += 1
            # if the order is not the last print a new line
            if order_proccessed < self.get_order_count():
                print()
            
        