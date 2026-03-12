import streamlit as st

st.set_page_config(page_title="Example AI", layout="centered")

# Olive green background
st.markdown("""
<style>
.stApp {
    background-color: #556B2F;
}
.typing {
    font-size:60px;
    font-weight:bold;
    text-align:center;
    color:white;
}
</style>
<h1 class="typing">Example AI</h1>
""", unsafe_allow_html=True)

st.write("### Enter your details")

# Frontend input boxes
st.text_input("Username")
st.text_input("Email")

# Frontend button
st.button("Submit")