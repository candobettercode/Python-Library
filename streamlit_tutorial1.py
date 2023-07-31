import streamlit as st
import time as t
st.image("yellow wall.jpg")

# title - It is used to add title of the app
st.title("Welcome to my first streamlit program")

# Header
st.header("Machine Learning")

# Sub header
st.subheader("Linear Regression")

# to give Information
st.info("Information details of user")

# warning message
st.warning("COme on time or else you will be remarked absent")

# Error Message
st.error("Wrong PAsswoord")

# Success MEssage
st.success("COngralution!!!!")

# MArkdown
st.markdown("# SBMP")
st.markdown("## SBMP")
st.markdown("### SBMP")
st.markdown(":moon:")

st.text("COmputer Enginerring")

# Write a Caption
st.caption("Caption is here")

# Write function
st.write("Employee Name")
st.write(range(50))

# To display maths function
st.latex(r''' a+b x^3+c''')

# widget

# Create a checkbox
st.checkbox("Login")

#create a button
st.button("CLick")

# Radio widget
st.radio("Pick your Gender",["Male","Female","Other"])

# Select Box widget
st.selectbox("Pick your course",["ML","Cloud","Cyber Security"])

# Multi Select
st.multiselect("Choose the Department",["COmputer","Chemical","Electrical"])

# Select Slider
st.select_slider("Rating",["Bad","Good","Excellent"])

# slider
st.slider("Enter your number",0,30)

# number input
st.number_input("Pick a Number",0,30)

# text input
st.text_input("Enter Email")

#date input
st.date_input("Enter birthdate")

# time input
st.time_input("What is the time??")

# Text area
st.text_area("Describe yourself")

# upload file
st.file_uploader("Upload your file")

st.color_picker("CHoose color")

st.progress(80)

#spinner
with st.spinner("Just wait..."):
    t.sleep(1)

# baloon
st.balloons()

# sidebar
st.sidebar.title("Computer Engineering")
st.sidebar.text_input("Email")

# Data Visualization

import pandas as pd
import numpy as np

st.title("Barchart")

data = pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)

st.title("Linechart")

data = pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.line_chart(data)

st.title("Area chart")

data = pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.area_chart(data)