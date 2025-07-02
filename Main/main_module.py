from dao.CustomerService import CustomerService
from dao.ProductService import ProductService
from dao.OrderService import OrderService
from dao.OrderDetailService import OrderDetailService
from dao.InventoryService import InventoryService
from entity.Customer import Customer
from entity.Product import Product
from entity.Order import Order
from entity.OrderDetail import OrderDetail
from entity.Inventory import Inventory
from datetime import datetime


def main():
    customer_service = CustomerService()
    product_service = ProductService()
    order_service = OrderService()
    order_detail_service = OrderDetailService()
    inventory_service = InventoryService()

    while True:
        print("\n===== TechShop Menu =====")
        print("1. Add Customer")
        print("2. Update Customer Info")
        print("3. Get Customer Details")
        print("4. Add Product")
        print("5. Update Product Info")
        print("6. Get Product Details")
        print("7. Add Inventory")
        print("8. View Inventory")
        print("9. Create Order")
        print("10. Add Order Detail")
        print("11. View Order Details")
        print("12. Cancel Order")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer_id = int(input("Enter Customer ID: "))
            first = input("Enter First Name: ")
            last = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            address = input("Enter Address: ")
            customer = Customer(customer_id, first, last, email, phone, address)
            customer_service.add_customer(customer)

        elif choice == '2':
            cid = int(input("Enter Customer ID: "))
            email = input("New Email: ")
            phone = input("New Phone: ")
            address = input("New Address: ")
            customer_service.update_customer_info(cid, email, phone, address)

        elif choice == '3':
            cid = int(input("Enter Customer ID: "))
            customer_service.get_customer_details(cid)

        elif choice == '4':
            pid = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            desc = input("Enter Description: ")
            price = float(input("Enter Price: "))
            product = Product(pid, name, desc, price)
            product_service.add_product(product)

        elif choice == '5':
            pid = int(input("Enter Product ID: "))
            price = float(input("New Price: "))
            desc = input("New Description: ")
            product_service.update_product_info(pid, price, desc)

        elif choice == '6':
            pid = int(input("Enter Product ID: "))
            product_service.get_product_details(pid)


        elif choice == '7':
            inventory_id = int(input("Enter Inventory ID: "))
            pid = int(input("Enter Product ID: "))
            qty = int(input("Enter Quantity In Stock: "))
            date = input("Enter Last Stock Update (YYYY-MM-DD): ")
            product = product_service.get_product_by_id(pid)  # Ensure this method exists
            if not product:
                print("Product not found.")
            else:
                inventory = Inventory(inventory_id, product, qty)
                inventory_service.add_inventory(inventory)

        elif choice == '8':
            inventory_service.list_all_products()



        elif choice == '9':
            oid = int(input("Enter Order ID: "))
            cid = int(input("Enter Customer ID: "))
            date_str = input("Enter Order Date (YYYY-MM-DD): ")
            order_date = datetime.strptime(date_str, "%Y-%m-%d")
            customer = customer_service.get_customer_by_id(cid)
            if not customer:
                print("Customer not found.")
            else:
                order_date = datetime.strptime(date_str, "%Y-%m-%d")
                order = Order(oid, customer, order_date)
                order_service.create_order(order)


        elif choice == '10':
            detail_id = int(input("Enter Order Detail ID: "))
            oid = int(input("Enter Order ID: "))
            pid = int(input("Enter Product ID: "))
            qty = int(input("Enter Quantity: "))
            order = order_service.get_order_by_id(oid)
            product = product_service.get_product_by_id(pid)
            order_detail = OrderDetail(detail_id, order, product, qty)
            order_detail_service.add_order_detail(order_detail)
            order_service.calculate_total_amount(oid)

        elif choice == '11':
            oid = int(input("Enter Order ID: "))
            order_detail_service.get_order_details_by_order_id(oid)

        elif choice == '12':
            oid = int(input("Enter Order ID to cancel: "))
            order_service.cancel_order(oid)

        elif choice == '13':
            print("Exiting TechShop. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


