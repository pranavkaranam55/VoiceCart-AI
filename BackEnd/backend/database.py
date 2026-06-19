import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "orders.db")

with sqlite3.connect(DB_PATH) as conn:

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        language TEXT,
        status TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()


def save_orders(order_list, language):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect(DB_PATH, timeout=10) as conn:

        cursor = conn.cursor()

        for order in order_list:

            cursor.execute(
                """
                INSERT INTO orders
                (product, quantity, language, status, timestamp)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    order["product"],
                    order["quantity"],
                    language,
                    "Confirmed",
                    current_time
                )
            )

        conn.commit()


def get_dashboard_stats():

    with sqlite3.connect(DB_PATH, timeout=10) as conn:

        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM orders")
        today_orders = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM orders WHERE status='Confirmed'"
        )
        delivered_orders = cursor.fetchone()[0]

        live_orders = 0

        cursor.execute("SELECT SUM(quantity) FROM orders")
        total_quantity = cursor.fetchone()[0]

        if total_quantity is None:
            total_quantity = 0

        revenue = total_quantity * 100

        return {
            "today_orders": today_orders,
            "live_orders": live_orders,
            "delivered_orders": delivered_orders,
            "revenue": revenue
        }
def get_all_orders():

    with sqlite3.connect(DB_PATH) as conn:

        cursor = conn.cursor()

        cursor.execute("""
        SELECT product, quantity, language, status, timestamp
        FROM orders
        ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        orders = []

        for row in rows:

            orders.append({
                "product": row[0],
                "quantity": row[1],
                "language": row[2],
                "status": row[3],
                "timestamp": row[4]
            })

        return orders

def get_analytics_stats():

    with sqlite3.connect(DB_PATH) as conn:

        cursor = conn.cursor()

        cursor.execute("""
        SELECT product, SUM(quantity)
        FROM orders
        GROUP BY product
        ORDER BY SUM(quantity) DESC
        LIMIT 1
        """)

        highest = cursor.fetchone()

        if highest:
            highest_item = f"{highest[0]} ({highest[1]} Sales)"
        else:
            highest_item = "No Data"

        cursor.execute("""
        SELECT product
        FROM orders
        GROUP BY product
        ORDER BY SUM(quantity) DESC
        LIMIT 5
        """)

        products = cursor.fetchall()

        top_products = ", ".join([p[0] for p in products])

        cursor.execute("SELECT COUNT(DISTINCT timestamp) FROM orders")
        avg_orders = cursor.fetchone()[0]

        cursor.execute("SELECT SUM(quantity) FROM orders")
        total_quantity = cursor.fetchone()[0]

        if total_quantity is None:
            total_quantity = 0

        weekly_sales = total_quantity * 100

        return {
            "highest_selling_item": highest_item,
            "top_products": top_products,
            "average_orders_per_day": f"{avg_orders} Orders",
            "weekly_sales": f"₹{weekly_sales}"
        }