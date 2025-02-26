import streamlit as st
# Set page title and favicon
st.set_page_config(page_title="Login Page", page_icon="🔐", layout="centered")
st.image("https://www.wallpaperflare.com/one-piece-wallpaper-anime-brook-one-piece-franky-one-piece-wallpaper-sfswd", use_container_width=True)
# Centered Login Form
st.markdown("<h1>PIRATES RECORDS</h1>", unsafe_allow_html=True)
st.write("")

# Login Form
with st.form("login_form", clear_on_submit=True):
    username = st.text_input("Username", placeholder="Enter your PIRATE NAME")
    password = st.text_input("PI-code", type="password", placeholder="Enter your SECRET CODE")

    col1, col2 = st.columns(2)
    with col1:
        submit = st.form_submit_button("Submit")
    with col2:
        cancel = st.form_submit_button("Cancel")

# Handle Button Clicks
if submit:
    if username and password:
        st.success(f"Login successful! Welcome, {username}!")
    else:
        st.error("Please enter both username and password!")

