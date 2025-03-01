
import streamlit as st


st.title("Hello, World with Streamlit!")


st.write("Welcome to the Streamlit app")


if st.button('Click Me'):

    st.write('Button clicked!')
    st.checkbox("check me")

if st.checkbox("check me to show some text"):
    # If checkbox is checked, display the text
    st.write("hello digitalschool")

    user_input = st.text_input("Enter text","Shenoni nje text")
    st.write("You Entered:",user_input)

    age = st.number_input("Enter you age", min_value=1, max_value=100)
    st.write(f'You age: {age}')

    message = st.text_area("Enter a message")
    st.write(f"Your message:{message}")

    choice = st.radio("Pick one", ['Choice 1','Choice 2','Chice 3'])
    st.write(f"You choe:{choice}")

    if st.button("Success"):
        st.success("It was send successfully")

        try:

            1 / 0
        except Exception as e:
            st.exception(e)