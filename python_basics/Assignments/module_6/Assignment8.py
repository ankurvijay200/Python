import streamlit as st

# Task 1 :-
st.title("Welcome to Streamlit!")

name = st.text_input("Enter your name:")

if st.button("Greet Me"):
    st.write(f"Hello, {name}!")
    
#-----------------------------------------------------------------------------------------------
# Task 2:-
import streamlit as st

st.title("Price Calculator")

price = st.number_input("Original Price:", min_value=0.0, value=1000.0)
discount = st.slider("Discount Percentage (%)", 0, 50, 10)

if st.button("Calculate Final Price"):
    final_price = price - (price * discount / 100)
    st.success(f"Final Price: {final_price}")
    
    comparison_data = [
        ["Before", price],
        ["After", final_price]
    ]
    st.table(comparison_data)

#-----------------------------------------------------------------------------------------------
# Task 3:-
import streamlit as st

st.title("Product Management Dashboard")

st.sidebar.header("Product Details Form")
product_name = st.sidebar.text_input("Product Name")
category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Home & Kitchen", "Books", "Sports"])
price = st.sidebar.number_input("Price", min_value=0.0, value=100.0)

if st.sidebar.button("Add Product"):
    st.success("Product added successfully!")
    st.write("### Product Details")
    st.write(f"**Product Name:** {product_name}")
    st.write(f"**Category:** {category}")
    st.write(f"**Price:** {price}")
    
#-----------------------------------------------------------------------------------------------
# Task 4:-

import streamlit as st

st.title("Simple Sales Dashboard")
st.write("A small dashboard displaying monthly sales data.")

months = ["January", "February", "March", "April"]
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

selected_month = st.selectbox("Select Month", months)

selected_sales = sales[selected_month]
st.metric(label=f"Sales for {selected_month}", value=selected_sales)

st.write("### Sales Bar Chart")
st.bar_chart(list(sales.values()))