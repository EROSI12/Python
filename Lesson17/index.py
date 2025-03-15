import streamlit as st


col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")


with col1:
    st.header("Column 1")
    st.write("Content for column 1")

with col2:
    st.header("Column 2")
    st.write("Content for column 2")

with col3:
    st.header("Column 3")
    st.write("Content for column 3")

with col4:
    st.header("Column 4")
    st.write("Content for column 4")

with col5:
    st.header("Column 5")
    st.write("Content for column 5")

import streamlit as st


with st.form("my_form", clear_on_submit=True):

    name = st.text_input('Name')
    age = st.number_input('Age', min_value=0)
    email = st.text_input('Email')
    biography = st.text_area('Biography')
    terms = st.checkbox('I agree to the terms and conditions')

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not terms:
            st.error("You must agree to the terms and conditions.")
        else:
            st.write(f"Name: {name}")
            st.write(f"Age: {age}")
            st.write(f"Email: {email}")
            st.write(f"Biography: {biography}")
            st.success("Form submitted successfully!")

import streamlit as st

tap1, tap2, tap3 = st.tabs(["Tap1", "Tap2", "Tap3"])

with tap1:
    st.header("Content for Tap1")
    st.write("This is content for Tap1")

with tap2:
    st.header("Content for Tap2")
    st.write("This is content for Tap2")

with tap3:
    st.header("Content for Tap3")
    st.write("This is content for Tap3")

