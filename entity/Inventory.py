from datetime import datetime
from entity.Product import Product

class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock=0):
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock if quantity_in_stock >= 0 else 0
        self.__last_stock_update = datetime.now()

    def set_quantity_in_stock(self, qty):
        if qty < 0:
            raise ValueError("Quantity can't be negative")
        self.__quantity_in_stock = qty
        self.__last_stock_update = datetime.now()

    def get_product(self):
        return self.__product

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    def add_to_inventory(self, qty):
        if qty > 0:
            self.__quantity_in_stock += qty

    def remove_from_inventory(self, qty):
        if 0 < qty <= self.__quantity_in_stock:
            self.__quantity_in_stock -= qty
            self.__last_stock_update = datetime.now()
        else:
            raise ValueError("Invalid quantity to remove from inventory")

    def update_stock_quantity(self, new_qty):
        self.set_quantity_in_stock(new_qty)

    def is_product_available(self, qty):
        return self.__quantity_in_stock >= qty

    def get_inventory_value(self):
        return self.__quantity_in_stock * self.__product.get_price()

    def __str__(self):
        return f"Product: {self.__product.get_product_name()}, Stock: {self.__quantity_in_stock}"

