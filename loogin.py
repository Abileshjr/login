import streamlit as st
# Set page title and favicon
st.set_page_config(page_title="Login Page", page_icon="🔐", layout="centered")

# CSS for Background Image and Styling
def add_bg_from_url():
    bg_image = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://www.wallpaperflare.com/one-piece-wallpaper-anime-brook-one-piece-franky-one-piece-wallpaper-sfswd");
        background-size: cover;
        background-repeat: no-repeat;
    }

    [data-testid="stForm"] {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 30px;
        border-radius: 10px;
    }

    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px;
        width: 100%;
    }

    div.stButton > button:hover {
        background-color: #45a049;
    }

    h1, label {
        color: white !important;
        text-align: center;
    }

    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

# Apply Background Image
add_bg_from_url()

# Centered Login Form
st.markdown("<h1>Login Page1</h1>", unsafe_allow_html=True)
st.write("")

# Login Form
with st.form("login_form1", clear_on_submit=True):
    username = st.text_input("Username1", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

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

