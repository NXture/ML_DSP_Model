import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


page = st.sidebar.selectbox("Select Explore Or Predict from the dropbox below", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
