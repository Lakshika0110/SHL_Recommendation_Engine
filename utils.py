# utils.py

import pandas as pd

def preprocess_catalog(file):
    df = pd.read_csv(file)
    df.columns = [col.strip().lower() for col in df.columns]
    df['recommended_for'] = df['recommended_for'].str.strip().str.lower()
    return df

def get_recommendations(df, role_type):
    recommendations = df[df['recommended_for'].str.contains(role_type, na=False)]
    return recommendations[['product_id', 'product_name', 'product_type', 'skill_area']]
