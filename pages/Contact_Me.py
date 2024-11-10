import streamlit as st
import re
from send_email import send

FORM_KEY = "form"

def valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return re.match(regex, email)

st.header("Contact Me")

with st.form(FORM_KEY):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")

    if button and (not any(user_email.strip()) or not any(raw_message.strip())):
        st.info("Fill the email and message fields")
    elif button and not valid_email(user_email):
        st.info("Invalid email")
    elif button:
        send(message)
        st.info("Your email was sent successfully")