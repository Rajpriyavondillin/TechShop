from Exceptions.exceptions import *
from entity.Product import Product
from entity.Order import Order
from entity.Inventory import Inventory
from entity.OrderDetail import OrderDetail
from datetime import datetime

class CollectionManager:
    def __init__(self):
        self.products_list = []          # List[Products]
        self.orders_list = []            # List[Orders]
        self.inventory_dict = {}         # Dict[int, Inventory], keyed by ProductID
        self.payment_records = {}        # Dict[int, str], keyed by OrderID, status: "Paid", "Failed"

    # ---------------------------- Product Management ----------------------------
    def add_product(self, product):
        for p in self.products_list:
            if p.get_product_name().lower() == product.get_product_name().lower():
                raise InvalidDataException("Product with the same name already exists.")
        self.products_list.append(product)

    def update_product(self, product_id, new_price=None, new_description=None):
        for p in self.products_list:
            if p.get_product_id() == product_id:
                if new_price is not None:
                    p.set_price(new_price)
                if new_description is not None:
                    p.set_description(new_description)
                return
        raise InvalidDataException("Product not found.")

    def remove_product(self, product_id):
        for p in self.products_list:
            if p.get_product_id() == product_id:
                # Check if product is part of any order
                for order in self.orders_list:
                    for detail in order.get_order_details():
                        if detail.get_product().get_product_id() == product_id:
                            raise InvalidDataException("Product part of existing order. Cannot remove.")
                self.products_list.remove(p)
                return
        raise InvalidDataException("Product not found.")

    # ---------------------------- Order Management ----------------------------
    def add_order(self, order):
        # Validate stock before adding
        for detail in order.get_order_details():
            prod_id = detail.get_product().get_product_id()
            if prod_id not in self.inventory_dict:
                raise IncompleteOrderException("Product not in inventory.")
            if not self.inventory_dict[prod_id].is_product_available(detail.get_quantity()):
                raise InsufficientStockException("Not enough stock for product: " + detail.get_product().get_product_name())
        # Deduct stock
        for detail in order.get_order_details():
            prod_id = detail.get_product().get_product_id()
            self.inventory_dict[prod_id].remove_from_inventory(detail.get_quantity())
        self.orders_list.append(order)

    def update_order_status(self, order_id, new_status):
        for o in self.orders_list:
            if o.get_order_id() == order_id:
                o.set_status(new_status)
                return
        raise InvalidDataException("Order ID not found.")

    def remove_cancelled_orders(self):
        self.orders_list = [o for o in self.orders_list if o.get_status().lower() != 'cancelled']

    # ---------------------------- Sorting Orders ----------------------------
    def get_orders_sorted_by_date(self, descending=False):
        return sorted(self.orders_list, key=lambda o: o.get_order_date(), reverse=descending)

    # ---------------------------- Inventory Management ----------------------------
    def add_inventory(self, inventory):
        pid = inventory.get_product().get_product_id()
        self.inventory_dict[pid] = inventory

    def update_inventory_quantity(self, product_id, quantity):
        if product_id in self.inventory_dict:
            self.inventory_dict[product_id].update_stock_quantity(quantity)
        else:
            raise InvalidDataException("Product not found in inventory.")

    def get_inventory(self):
        return self.inventory_dict.values()

    # ---------------------------- Payment Handling ----------------------------
    def record_payment(self, order_id, status):
        if status not in ["Paid", "Failed"]:
            raise PaymentFailedException("Invalid payment status.")
        self.payment_records[order_id] = status

    def get_payment_status(self, order_id):
        return self.payment_records.get(order_id, "Unknown")

    # ---------------------------- Product Search ----------------------------
    def search_products_by_name(self, name):
        results = [p for p in self.products_list if name.lower() in p.get_product_name().lower()]
        if not results:
            raise InvalidDataException("No products found matching search.")
        return results

    def get_all_products(self):
        return self.products_list