# TechShop – Electronic Gadget Store Management System

## 📌 Introduction

TechShop is a Python-based Object-Oriented application designed to manage the day-to-day operations of an electronic gadgets shop. The project covers core concepts of OOP such as encapsulation, composition, custom exceptions, and also includes database integration using MySQL.

It simulates real-world business operations such as product management, customer management, order placement, inventory tracking, and order detail management.

---

## 📁 Project Structure
```text
TechShop/
├── entity/ # Model classes (POJOs) without business logic
│ ├── customer.py
│ ├── product.py
│ ├── order.py
│ ├── order_detail.py
│ └── inventory.py
├── dao/ # Service layer with DB logic
│ ├── customer_service.py
│ ├── product_service.py
│ ├── order_service.py
│ ├── order_detail_service.py
│ └── inventory_service.py
├── exception/ # Custom user-defined exceptions
│ └── custom_exceptions.py
├── util/ # DB utilities
│ ├── db_conn_util.py
│ └── db_property_util.py
├── main/
│ └── main_module.py # Menu-driven interface
├── README.md # Project documentation
```


---

## 💡 Features and Functionalities

- **Customer Management**
  - Add, view, and update customer details
  - Calculate total orders placed

- **Product Management**
  - Add, view, and update product information
  - Check stock availability

- **Inventory Management**
  - Add or update inventory levels
  - Check low stock or out-of-stock items
  - Calculate inventory value

- **Order and Order Detail Management**
  - Create new orders linked to customers
  - Add products to an order
  - View order summary and subtotal
  - Apply discounts to order items

- **Encapsulation & Composition**
  - Classes follow encapsulation with private attributes and getter/setter methods
  - Order class uses composition to hold Customer object
  - OrderDetail uses composition for both Order and Product

- **Exception Handling**
  - User-defined exceptions for error scenarios (e.g., invalid data, stock issues)

- **Database Integration**
  - MySQL database used for persistent storage
  - DB utility classes handle connections using property files

---

## ▶️ How the Project Works

1. Run the `main_module.py` file to launch the menu-driven application.
2. Choose operations like adding customers/products/orders/inventory.
3. Application interacts with the database using service classes.
4. You can perform CRUD operations, manage inventory and monitor low-stock alerts.
5. All entities are stored in MySQL tables and changes are committed in real-time.

---

## 🛠 Technologies Used

- Python (OOP Principles)
- MySQL
- PyMySQL / mysql-connector-python
- Custom Exception Handling
- File-based configuration reading

---

## ✅ Final Notes

TechShop is designed to be modular and extendable. You can easily add more features like Payment Processing, Reports, or Admin Authentication in future iterations.

