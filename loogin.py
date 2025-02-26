import streamlit as st
st.set_page_config(page_title="Login Page", page_icon="🔐", layout="centered")
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://editorial.pxcrush.net/carsales/general/editorial/2024-ford-mustang-gt-fastback-manual-05.jpg?width=1024&height=682");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    [data-testid="stForm"] {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 30px;
        border-radius: 10px;
    }
    h1, label {
        color: white !important;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
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

