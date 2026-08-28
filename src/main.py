from pathlib import Path
from csv_reader import read_sales
from metrics import calculate_metrics

def main():
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "sales.csv"

    sales = read_sales(file_path)
    metrics = calculate_metrics(sales)

    print("Total revenue:", metrics.total_revenue)
    print("Total sales:", metrics.total_sales)
    print("Average sale:", metrics.average_sale)
    print("Best selling product:", metrics.best_selling_product)
    print("Best selling quantity:", metrics.best_selling_quantity)
    print(metrics.sales_by_product)

if __name__ == "__main__":
    main()