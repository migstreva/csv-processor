from pathlib import Path

from csv_reader import read_sales


def test_read_sales():
    file_path = Path(__file__).parent / "data" / "test_sales.csv"
    sales = read_sales(file_path)

    assert sales == [
        {
            "date": "2026-08-01",
            "product": "Laptop",
            "quantity": "2",
            "price": "4500"
        },
        {
            "date": "2026-08-01",
            "product": "Mouse",
            "quantity": "5",
            "price": "100"
        }
    ]

def test_read_empty_sales():
    file_path = Path(__file__).parent / "data" / "empty_sales.csv"
    sales = read_sales(file_path)

    assert sales == []
