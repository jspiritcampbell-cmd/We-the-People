import streamlit as st
import pandas as pd
import numpy as np

# App title
st.title("My Streamlit App")

# Sidebar
st.sidebar.header("Settings")
option = st.sidebar.selectbox(
    "Choose an option:",
    ("Overview", "Data", "About")
)

# Main content
if option == "Overview":
    st.subheader("Welcome!")
    st.write("This is a basic Streamlit app. Use the sidebar to explore different sections.")

elif option == "Data":
    st.subheader("Data Preview")
    data = pd.DataFrame({
        "Column 1": np.random.randn(10),
        "Column 2": np.random.randn(10)
    })
    st.dataframe(data)

    st.line_chart(data)

elif option == "About":
    st.subheader("About This App")
    st.write("Created with Streamlit. Modify this file to add your own features!")

# Footer
st.markdown("---")
st.caption("© 2025 My Streamlit App")
