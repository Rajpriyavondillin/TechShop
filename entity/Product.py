class Product:
    def __init__(self, product_id, product_name, description, price):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price=0
        self.set_price(price)

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def set_product_name(self, name):
        self.__product_name = name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = price

    def __str__(self):
        return f"ProductID: {self.__product_id}, Name: {self.__product_name}, Price: ₹{self.__price}"

