from dataclasses import dataclass

@dataclass
class SaleMetrics:
    total_revenue: float
    total_sales: int
    average_sale: float
    best_selling_product: str
    best_selling_quantity: int
    sales_by_product: dict