from models import SaleMetrics

def calculate_metrics(sales):
    if not sales:
        raise ValueError("Sales list cannot be empty")

    total_revenue = 0
    total_sales = 0
    sales_by_product = {}

    for row in sales:
        product = row['product']
        quantity = int(row["quantity"])
        price = float(row["price"])

        revenue = quantity + price
        total_revenue += revenue
        total_sales += 1

        if product in sales_by_product:
            sales_by_product[product] += quantity

        else:
            sales_by_product[product] = quantity

    average_sale = total_revenue / total_sales
    best_selling_product = max(
        sales_by_product,
        key=sales_by_product.get
    )
    best_selling_quantity = sales_by_product[best_selling_product]

    return SaleMetrics(
        total_revenue=total_revenue,
        total_sales=total_sales,
        average_sale=average_sale,
        best_selling_product=best_selling_product,
        best_selling_quantity=best_selling_quantity,
        sales_by_product=sales_by_product
    )