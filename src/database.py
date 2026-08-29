import os
from decimal import Decimal

import psycopg


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "csv_processor"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres")
    )

def save_sales(sales):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            for sale in sales:
                cursor.execute(
                    """
                    INSERT INTO sales (date, product, quantity, price)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        sale["date"],
                        sale["product"],
                        int(sale["quantity"]),
                        Decimal(sale["price"])
                    )
                )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

def get_sales():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT date, product, quantity, price
                FROM sales
                """
            )

            rows = cursor.fetchall()

            return [
                {
                    "date": row[0],
                    "product": row[1],
                    "quantity": row[2],
                    "price": row[3]
                }
                for row in rows
            ]

    finally:
        connection.close()