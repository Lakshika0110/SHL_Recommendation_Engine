# recommendation_engine.py

import pandas as pd

# Load product catalog
df = pd.read_csv('product_catalog.csv')

def recommend_products(role):
    if role.lower() == 'entry-level':
        return df[df['recommended_for'].str.contains('Entry-level', case=False)]
    elif role.lower() == 'leadership':
        return df[df['recommended_for'].str.contains('Leadership', case=False)]
    elif role.lower() == 'software':
        return df[df['recommended_for'].str.contains('Software', case=False)]
    elif role.lower() == 'customer-facing':
        return df[df['recommended_for'].str.contains('Customer-facing', case=False)]
    else:
        return df  # Return all if no match

if __name__ == "__main__":
    user_role = input("Enter role type (entry-level / leadership / software / customer-facing): ")
    recommendations = recommend_products(user_role)
    print("\nRecommended Assessments:\n")
    print(recommendations[['product_name', 'skill_area', 'recommended_for']])
