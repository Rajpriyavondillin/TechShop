# dao/order_detail_service.py

from entity.OrderDetail import OrderDetail
from entity.Product import Product
from entity.Order import Order
from util.DBConnUtil import get_connection

class OrderDetailService:
    def __init__(self):
        self.order_details = {}  # Key: OrderDetailID, Value: OrderDetail object

    def create_order_detail(self, order_detail_id: int, order: Order, product: Product, quantity: int) -> OrderDetail:
        detail = OrderDetail(order_detail_id, order, product, quantity)
        self.order_details[order_detail_id] = detail

        # ✅ Only if the 'order' has a method 'add_order_detail'
        if hasattr(order, 'add_order_detail'):
            order.add_order_detail(detail)

        return detail

    def get_order_details_by_order_id(self, order_id):
        return [
            detail for detail in self.order_details.values()
            if detail.get_order().get_order_id() == order_id
        ]

    def add_order_detail(self, order_detail):
        try:
            db = get_connection()
            cursor = db.cursor()
            query = """
                INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (
                order_detail.get_order_detail_id(),
                order_detail.get_order().get_order_id(),
                order_detail.get_product().get_product_id(),
                order_detail.get_quantity()
            ))
            db.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            db.close()

    def get_order_detail(self, order_detail_id: int) -> OrderDetail:
        return self.order_details.get(order_detail_id)

    def update_quantity(self, order_detail_id: int, new_quantity: int) -> bool:
        detail = self.order_details.get(order_detail_id)
        if detail:
            detail.update_quantity(new_quantity)
            return True
        return False

    def apply_discount(self, order_detail_id: int, discount_percent: float) -> bool:
        detail = self.order_details.get(order_detail_id)
        if detail:
            detail.add_discount(discount_percent)
            return True
        return False

    def get_order_detail_info(self, order_detail_id: int) -> str:
        detail = self.order_details.get(order_detail_id)
        return detail.get_order_detail_info() if detail else "Order detail not found."

    def get_all_order_details(self):
        return list(self.order_details.values())
