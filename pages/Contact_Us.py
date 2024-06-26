import streamlit as st
from send_email import send_email

st.header(
    'Contact Me'
)

with st.form(key="emai_form"):
    user_email = st.text_input('Enter email address')
    topic_options = ['Job Inquiries', 'Project Proposals', 'Other']
    topic = st.selectbox('What topic do you want to discuss?', topic_options)
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {topic}
{raw_message}
"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info('Your email was sent successfully!')