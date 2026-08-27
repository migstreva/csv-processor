from metrics import calculate_metrics
import pytest

def test_calculate_metrics():
    sales = [
        {
            "product": "Laptop",
            "quantity": "2",
            "price": "4500"
        },
        {
            "product": "Mouse",
            "quantity": "5",
            "price": "100"
        }
    ]

    metrics = calculate_metrics(sales)

    assert metrics.total_revenue == 9500
    assert metrics.total_sales == 2
    assert metrics.average_sale == 4750
    assert metrics.best_selling_product == "Mouse"
    assert metrics.best_selling_quantity == 5

def test_calculate_metrics_with_empty_sales():
    with pytest.raises(ValueError):
        calculate_metrics([])
