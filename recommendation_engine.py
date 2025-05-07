import pandas as pd

def load_catalog(file_path):
    return pd.read_csv(file_path)

def recommend_products(role_type, catalog_df):
    role_type = role_type.lower()
    recommended = catalog_df[catalog_df['Role_Type'].str.lower() == role_type]
    return recommended[['Product_ID', 'Product_Name', 'Description']]
