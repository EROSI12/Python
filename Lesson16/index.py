import streamlit as st

st.title("Hello, World with Streamlit!")
st.write("Welcome to the Streamlit app")

if st.button('Click Me'):
    st.write('Button clicked!')
    st.checkbox("check me")

if st.checkbox("check me to show some text"):
    # If checkbox is checked, display the text
    st.write("hello digitalschool")

    user_input = st.text_input("Enter text", "Enter some text here")
    st.write("You Entered:", user_input)

    age = st.number_input("Enter your age", min_value=1, max_value=100)
    st.write(f'Your age: {age}')

    message = st.text_area("Enter a message")
    st.write(f"Your message: {message}")

    choice = st.radio("Pick one", ['Choice 1', 'Choice 2', 'Choice 3'])  # Corrected the typo here
    st.write(f"You chose: {choice}")

    if st.button("Success"):
        st.success("It was sent successfully")

        try:
            1 / 0
        except Exception as e:
            st.exception(e)

import streamlit as st

def main():
    st.title("Personal Information Form")

    st.header("Enter Your Details")

    # Get user inputs
    name = st.text_input("Enter your first name")
    surname = st.text_input("Enter your surname")
    age = st.number_input("Enter your age", min_value=0, value=18)
    height = st.number_input("Enter your height (in cm)", min_value=0, value=170)

    if st.button("Submit"):
        # Display a message with the entered details
        st.write(f"Hello {name} {surname}!")
        st.write(f"You are {age} years old and your height is {height} cm.")
        st.write("Thank you for submitting your details!")

if __name__ == "__main__":
    main()
