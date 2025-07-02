class Payment:
    def __init__(self, payment_id, order_id, amount, method, status):
        self.__payment_id = payment_id
        self.__order_id = order_id
        self.__amount=0.0
        self.set_amount(amount)
        self.__method = method
        self.__status = status

    # Getters
    def get_payment_id(self): return self.__payment_id
    def get_order_id(self): return self.__order_id
    def get_amount(self): return self.__amount
    def get_method(self): return self.__method
    def get_status(self): return self.__status

    # Setters with validation
    def set_payment_id(self, pid): self.__payment_id = pid
    def set_order_id(self, oid): self.__order_id = oid

    def set_amount(self, amount):
        if amount > 0:
            self.__amount = amount
        else:
            raise ValueError("Amount must be greater than 0")

    def set_method(self, method): self.__method = method
    def set_status(self, status): self.__status = status

    def __str__(self):
        return f"Payment ID: {self.__payment_id}, Order ID: {self.__order_id}, Amount: ₹{self.__amount}, Method: {self.__method}, Status: {self.__status}"
