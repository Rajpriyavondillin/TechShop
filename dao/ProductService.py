# dao/product_service.py

from entity.Product import Product

class ProductService:
    def __init__(self):
        self.products = {}  # Key: product_id, Value: Product object

    def add_product(self, product):
        self.products[product.get_product_id()] = product

    def get_product_by_id(self, product_id):
        return self.products.get(product_id, None)

    def get_product(self, product_id: int) -> Product:
        return self.products.get(product_id)

    def get_product_details(self, product_id: int) -> str:
        product = self.products.get(product_id)
        return product.get_product_details() if product else "Product not found."

    def update_product_info(self, product_id: int, price: float = None, description: str = None) -> bool:
        product = self.products.get(product_id)
        if product:
            product.update_product_info(price, description)
            return True
        return False

    def is_product_in_stock(self, product_id: int, inventory_service) -> bool:
        return inventory_service.get_quantity_in_stock(product_id) > 0 if inventory_service else False

    # Getters
    def get_name(self, product_id: int) -> str:
        product = self.products.get(product_id)
        return product.product_name if product else None

    def get_description(self, product_id: int) -> str:
        product = self.products.get(product_id)
        return product.description if product else None

    def get_price(self, product_id: int) -> float:
        product = self.products.get(product_id)
        return product.price if product else None

    # Setters
    def set_name(self, product_id: int, name: str):
        product = self.products.get(product_id)
        if product:
            product.product_name = name

    def set_description(self, product_id: int, description: str):
        product = self.products.get(product_id)
        if product:
            product.description = description

    def set_price(self, product_id: int, price: float):
        product = self.products.get(product_id)
        if product:
            product.price = price



