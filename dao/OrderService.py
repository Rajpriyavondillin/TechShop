
# dao/order_service.py

from entity.Order import Order
from entity.Customer import Customer
from datetime import datetime
from util.DBConnUtil import get_connection

class OrderService:
    def __init__(self):
        self.orders = {}  # Key: OrderID, Value: Order object

    def add_order(self, order):
        self.orders[order.get_order_id()] = order

    def get_order_by_id(self, order_id):
        return self.orders.get(order_id, None)

    def create_order(self, order_id: int, customer: Customer, order_date: datetime):
        order = Order(order_id, customer, order_date)
        self.orders[order_id] = order
        return order

    def get_order(self, order_id: int) -> Order:
        return self.orders.get(order_id)

    def update_order_status(self, order_id: int, new_status: str) -> bool:
        order = self.orders.get(order_id)
        if order:
            order.update_order_status(new_status)
            return True
        return False

    def calculate_total_amount(self, order_id):
        try:
            db = get_connection()
            cursor = db.cursor()

            # Fetch all order details for this order
            query = """
                SELECT od.Quantity, p.Price
                FROM OrderDetails od
                JOIN Product p ON od.ProductID = p.ProductID
                WHERE od.OrderID = %s
            """
            cursor.execute(query, (order_id,))
            order_items = cursor.fetchall()

            total_amount = 0
            for quantity, price in order_items:
                total_amount += quantity * float(price)

            # Update the order's total amount in the Orders table
            update_query = "UPDATE Orders SET TotalAmount = %s WHERE OrderID = %s"
            cursor.execute(update_query, (total_amount, order_id))
            db.commit()
            print(f"Total amount ₹{total_amount:.2f} updated successfully for Order ID {order_id}")

        except Exception as e:
            print("Error calculating total amount:", e)

        finally:
            cursor.close()
            db.close()

    def cancel_order(self, order_id: int) -> bool:
        order = self.orders.get(order_id)
        if order:
            order.cancel_order()
            return True
        return False

    def calculate_order_total(self, order_id: int) -> float:
        order = self.orders.get(order_id)
        if order:
            return order.calculate_total_amount()
        return 0.0

    def get_order_details(self, order_id: int) -> str:
        order = self.orders.get(order_id)
        return order.get_order_details() if order else "Order not found."

    def add_order_detail(self, order_id: int, order_detail):
        order = self.orders.get(order_id)
        if order:
            order.add_order_detail(order_detail)

    def get_all_orders(self):
        return list(self.orders.values())
