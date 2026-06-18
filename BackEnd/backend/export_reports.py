import sqlite3
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table


def export_csv():

    conn = sqlite3.connect("database/orders.db")

    df = pd.read_sql_query(
        "SELECT * FROM orders",
        conn
    )

    conn.close()

    df.to_csv(
        "orders_report.csv",
        index=False
    )

    return "orders_report.csv"


def export_excel():

    conn = sqlite3.connect("database/orders.db")

    df = pd.read_sql_query(
        "SELECT * FROM orders",
        conn
    )

    conn.close()

    df.to_excel(
        "orders_report.xlsx",
        index=False
    )

    return "orders_report.xlsx"


def export_pdf():

    conn = sqlite3.connect("database/orders.db")

    df = pd.read_sql_query(
        "SELECT * FROM orders",
        conn
    )

    conn.close()

    pdf = SimpleDocTemplate(
        "orders_report.pdf"
    )

    data = [df.columns.tolist()] + df.values.tolist()

    table = Table(data)

    pdf.build([table])

    return "orders_report.pdf"