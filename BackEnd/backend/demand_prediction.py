import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression


def predict_demand():

    conn = sqlite3.connect("database/orders.db")

    query = """
    SELECT product, quantity
    FROM orders
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    if df.empty:
        return []

    predictions = []

    products = df["product"].unique()

    for product in products:

        product_df = df[df["product"] == product]

        quantities = product_df["quantity"].tolist()

        X = []
        y = []

        for i in range(len(quantities)):
            X.append([i])
            y.append(quantities[i])

        if len(y) < 2:

            predicted_quantity = int(y[-1] * 1.2)

        else:

            model = LinearRegression()

            model.fit(X, y)

            predicted_quantity = int(
                model.predict([[len(y)]])[0]
            )

        predictions.append({
            "product": product,
            "predicted_quantity": max(predicted_quantity, 0)
        })

    return sorted(
        predictions,
        key=lambda x: x["predicted_quantity"],
        reverse=True
    )