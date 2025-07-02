from util.DBConnUtil import get_connection
from entity.Payment import Payment
from Exceptions.exceptions import PaymentFailedException

class PaymentService:
    def make_payment(self, payment: Payment):
        db = None
        cursor = None
        try:
            db = get_connection()
            cursor = db.cursor()
            query = "INSERT INTO Payment (PaymentID, OrderID, Amount, Method, Status) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (
                payment.get_payment_id(),
                payment.get_order_id(),
                payment.get_amount(),
                payment.get_method(),
                payment.get_status()
            ))
            db.commit()
        except Exception as e:
            raise PaymentFailedException("Payment failed due to: " + str(e))
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

    def get_payments_by_order_id(self, order_id):
        db = None
        cursor = None
        try:
            db = get_connection()
            cursor = db.cursor()
            query = "SELECT * FROM Payment WHERE OrderID = %s"
            cursor.execute(query, (order_id,))
            result = cursor.fetchall()
            return result
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()
