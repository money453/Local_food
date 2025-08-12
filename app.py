import streamlit as st
import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect("food_wastage.db")

st.title("Local Food Wastage Management System")

# Menu
menu = ["Home", "View Providers", "View Receivers", "Food Listings", "Claims", "Run Query"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to Local Food Wastage Management System")
    st.write("This app allows you to view and analyze data related to food providers, receivers, and food claims.")

elif choice == "View Providers":
    df = pd.read_sql_query("SELECT * FROM providers", conn)
    st.dataframe(df)

elif choice == "View Receivers":
    df = pd.read_sql_query("SELECT * FROM receivers", conn)
    st.dataframe(df)

elif choice == "Food Listings":
    df = pd.read_sql_query("SELECT * FROM food_listings", conn)
    st.dataframe(df)

elif choice == "Claims":
    df = pd.read_sql_query("SELECT * FROM claims", conn)
    st.dataframe(df)

elif choice == "Run Query":
    st.subheader("Run Custom SQL Query")
    query = st.text_area("Enter SQL Query")
    if st.button("Execute"):
        try:
            df = pd.read_sql_query(query, conn)
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error: {e}")
