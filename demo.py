import streamlit as st
import random
import time

# Page title
st.set_page_config(page_title="Smart Helmet – Fatigue Detection")

st.title("🪖 Smart Helmet with Fatigue Detection")
st.write("This is a demo web app using Streamlit")

# Sidebar
st.sidebar.header("Helmet Status")
start = st.sidebar.button("Start Monitoring")

# Main logic
if start:
    st.success("Helmet Monitoring Started")

    st.subheader("Sensor Readings")

