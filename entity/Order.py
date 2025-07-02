from datetime import datetime
from entity.Customer import Customer

class Order:
    def __init__(self, order_id, customer: Customer, order_date: datetime, total_amount=0.0, status='Pending'):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = order_date
        self.__total_amount=0.0
        self.set_total_amount(total_amount)
        self.__status = status
        self.details = []


    def get_order_id(self):
        return self.__order_id

    def get_customer(self):
        return self.__customer

    def get_order_date(self):
        return self.__order_date

    def get_total_amount(self):
        return self.__total_amount

    def set_total_amount(self, amount):
        if amount < 0:
            raise ValueError("Total amount cannot be negative.")
        self.__total_amount = amount

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
