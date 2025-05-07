# app.py

import streamlit as st
import pandas as pd
from utils import preprocess_catalog, get_recommendations

st.title('SHL Recommendation Engine')

uploaded_file = st.file_uploader('Upload Product Catalog CSV', type=['csv'])

if uploaded_file is not None:
    catalog_df = preprocess_catalog(uploaded_file)

    role_type = st.text_input("Enter role type (entry-level / leadership / software / customer-facing):").strip().lower()

    if st.button('Get Recommendations'):
        if role_type:
            recommendations = get_recommendations(catalog_df, role_type)
            if not recommendations.empty:
                st.subheader('Recommended Products:')
                st.dataframe(recommendations)
            else:
                st.warning('No recommendations found for this role type.')
        else:
            st.warning('Please enter a role type.')
