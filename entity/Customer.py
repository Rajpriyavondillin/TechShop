class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, name):
        self.__first_name = name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, name):
        self.__last_name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return f"Customer ID: {self.__customer_id}, Name: {self.__first_name} {self.__last_name}, Email: {self.__email}, Phone: {self.__phone}, Address: {self.__address}"



