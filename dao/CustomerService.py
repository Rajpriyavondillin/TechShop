# dao/customer_service.py

from entity.Customer import Customer

class CustomerService:
    def __init__(self):
        self.customers = {}  # Simulated in-memory database

    def add_customer(self, customer):
        self.customers[customer.get_customer_id()] = customer

    def get_customer_by_id(self, customer_id):
        return self.customers.get(customer_id, None)

    def calculate_total_orders(self, customer_id: int) -> int:
        customer = self.customers.get(customer_id)
        return customer.calculate_total_orders() if customer else 0

    def get_customer_details(self, customer_id: int) -> str:
        customer = self.customers.get(customer_id)
        return customer.get_customer_details() if customer else "Customer not found."

    def update_customer_info(self, customer_id: int, email: str = None, phone: str = None, address: str = None) -> bool:
        customer = self.customers.get(customer_id)
        if customer:
            customer.update_customer_info(email=email, phone=phone, address=address)
            return True
        return False


    def get_first_name(self, customer_id: int) -> str:
        customer = self.customers.get(customer_id)
        return customer.first_name if customer else None

    def get_last_name(self, customer_id: int) -> str:
        customer = self.customers.get(customer_id)
        return customer.last_name if customer else None

    def get_email(self, customer_id: int) -> str:
        customer = self.customers.get(customer_id)
        return customer.email if customer else None

    def get_phone(self, customer_id: int) -> str:
        customer = self.customers.get(customer_id)
        return customer.phone if customer else None

    def get_address(self, customer_id: int) -> str:
        customer = self.customers.get(customer_id)
        return customer.address if customer else None

    def get_order_count(self, customer_id: int) -> int:
        customer = self.customers.get(customer_id)
        return customer.order_count if customer else 0



    def set_first_name(self, customer_id: int, first_name: str):
        customer = self.customers.get(customer_id)
        if customer:
            customer.first_name = first_name

    def set_last_name(self, customer_id: int, last_name: str):
        customer = self.customers.get(customer_id)
        if customer:
            customer.last_name = last_name

    def set_email(self, customer_id: int, email: str):
        customer = self.customers.get(customer_id)
        if customer:
            customer.email = email

    def set_phone(self, customer_id: int, phone: str):
        customer = self.customers.get(customer_id)
        if customer:
            customer.phone = phone

    def set_address(self, customer_id: int, address: str):
        customer = self.customers.get(customer_id)
        if customer:
            customer.address = address

    def set_order_count(self, customer_id: int, order_count: int):
        customer = self.customers.get(customer_id)
        if customer:
            customer.order_count = order_count

