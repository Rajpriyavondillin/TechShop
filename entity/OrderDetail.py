from entity.Order import Order
from entity.Product import Product

class OrderDetail:
    def __init__(self, order_detail_id, order: Order, product: Product, quantity):
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity=0
        self.set_quantity(quantity)
        self.__discount = 0.0

    def get_order_detail_id(self):
        return self.__order_detail_id

    def get_order(self):
        return self.__order

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, qty):
        if qty <= 0:
            raise ValueError("Quantity must be positive")
        self.__quantity = qty

    def calculate_subtotal(self):
        return self.__quantity * self.__product.get_price() * (1 - self.__discount)

    def add_discount(self, percent):
        if 0 <= percent <= 100:
            self.__discount = percent / 100.0
