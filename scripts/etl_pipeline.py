import pandas as pd

def extract_data(path):
    return {
        "orders": pd.read_csv(path + "olist_orders_dataset.csv"),
        "customers": pd.read_csv(path + "olist_customers_dataset.csv"),
        "order_items": pd.read_csv(path + "olist_order_items_dataset.csv"),
        "payments": pd.read_csv(path + "olist_order_payments_dataset.csv"),
        "products": pd.read_csv(path + "olist_products_dataset.csv"),
        "reviews": pd.read_csv(path + "olist_order_reviews_dataset.csv"),
    }

def transform_data(data):
    orders = data["orders"]
    customers = data["customers"]
    order_items = data["order_items"]
    payments = data["payments"]
    products = data["products"]
    reviews = data["reviews"]

    # Clean
    orders.drop_duplicates(inplace=True)

    # Convert types
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

    # Merge
    df = orders.merge(customers, on='customer_id', how='left')
    df = df.merge(order_items, on='order_id', how='left')
    df = df.merge(payments, on='order_id', how='left')
    df = df.merge(products, on='product_id', how='left')
    df = df.merge(reviews, on='order_id', how='left')

    # Features
    df['total_order_value'] = df['price'] + df['freight_value']
    df['is_cancelled'] = df['order_status'] == 'canceled'

    return df

def load_data(df, path):
    df.to_csv(path + "final_analytics_dataset.csv", index=False)

if __name__ == "__main__":
    raw_path = "../data/raw/"
    processed_path = "../data/processed/"

    data = extract_data(raw_path)
    df = transform_data(data)
    load_data(df, processed_path)

    print("ETL Pipeline Completed Successfully!")