import streamlit as st

FORM_KEY = "form"

st.header("Contact Me")

with st.form(FORM_KEY):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")

    if button:
        print("I was pressed")