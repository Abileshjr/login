import streamlit as st
st.set_page_config(page_title="Login Page", page_icon="🔐", layout="centered")
st.image(r"C:\Users\kidjiraiya\Desktop\anime-one-piece-brook-one-piece-franky-one-piece-wallpaper-preview.jpg", use_container_width=True)
# for Centered Login Form
st.markdown("<h1>PIRATES RECORDS</h1>", unsafe_allow_html=True)
st.write("")
# for Login Form
with st.form("login_form", clear_on_submit=True):
    username = st.text_input("Username", placeholder="Enter your PIRATE NAME")
    password = st.text_input("PI-code", type="password", placeholder="Enter your SECRET CODE")

    col1, col2 = st.columns(2)
    with col1:
        submit = st.form_submit_button("Submit")
    with col2:
        cancel = st.form_submit_button("Cancel")
# for Button Clicks
if submit:
    if username and password:
        st.success(f"Login successful! Welcome, {username}!")
    else:
        st.error("Please enter both username and password!")

