# dao/inventory_service.py

from entity.Inventory import Inventory
from entity.Product import Product
from datetime import datetime

class InventoryService:
    def __init__(self):
        self.inventory_items = {}  # Correct usage

    def add_inventory(self, inventory):
        self.inventory_items[inventory.get_inventory_id()] = inventory

    def add_inventory_item(self, inventory_id: int, product: Product, quantity: int, last_update: datetime = None):
        if not last_update:
            last_update = datetime.now()
        inventory = Inventory(inventory_id, product, quantity, last_update)
        self.inventory_items[inventory_id] = inventory
        return inventory

    def get_inventory_item(self, inventory_id: int):
        return self.inventory_items.get(inventory_id)

    def list_all_products(self):
        return [str(inv) for inv in self.inventory_items.values()]

    def list_low_stock_products(self, threshold: int):
        return [inv for inv in self.inventory_items.values() if inv.quantity_in_stock < threshold]

    def list_out_of_stock_products(self):
        return [inv for inv in self.inventory_items.values() if inv.quantity_in_stock == 0]

    def is_product_available(self, inventory_id: int, quantity_to_check: int):
        inv = self.inventory_items.get(inventory_id)
        return inv.is_product_available(quantity_to_check) if inv else False

    def add_to_inventory(self, inventory_id: int, quantity: int):
        inv = self.inventory_items.get(inventory_id)
        if inv:
            inv.add_to_inventory(quantity)

    def remove_from_inventory(self, inventory_id: int, quantity: int):
        inv = self.inventory_items.get(inventory_id)
        if inv:
            inv.remove_from_inventory(quantity)

    def update_stock_quantity(self, inventory_id: int, new_quantity: int):
        inv = self.inventory_items.get(inventory_id)
        if inv:
            inv.update_stock_quantity(new_quantity)

    def get_inventory_value(self, inventory_id: int):
        inv = self.inventory_items.get(inventory_id)
        return inv.get_inventory_value() if inv else 0.0

    def get_total_inventory_value(self):
        return sum(inv.get_inventory_value() for inv in self.inventory_items.values())
