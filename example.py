import streamlit as st
import time

st.set_page_config(page_title="Example AI", layout="wide")

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = 1

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- STYLE ----------
st.markdown("""
<style>

/* animated background */
.stApp{
background: linear-gradient(-45deg,#556B2F,#6B8E23,#3B5323,#2E8B57);
background-size:400% 400%;
animation:gradientBG 10s ease infinite;
}

@keyframes gradientBG{
0%{background-position:0% 50%}
50%{background-position:100% 50%}
100%{background-position:0% 50%}
}

/* landing title */
.centerTitle{
text-align:center;
font-size:95px;
color:#00E5FF;
font-weight:bold;
margin-top:120px;
text-shadow:0 0 20px #00E5FF;
}

/* top title */
.topTitle{
text-align:center;
font-size:110px;
color:#00E5FF;
font-weight:bold;
margin-top:10px;
text-shadow:0 0 20px #00E5FF;
animation:moveUp 1.2s ease;
}

@keyframes moveUp{
from{
margin-top:200px;
font-size:95px;
}
to{
margin-top:10px;
font-size:110px;
}
}

/* subtitle */
.subtitle{
text-align:center;
font-size:28px;
color:#ffffff;
margin-bottom:30px;
}

/* input container */
div[data-baseweb="input"]{
border-radius:15px;
border:2px solid #00E5FF;
background:rgba(255,255,255,0.1);
backdrop-filter:blur(10px);
transition:0.3s;
}

/* glow */
div[data-baseweb="input"]:hover{
box-shadow:0 0 20px #00E5FF;
border-color:#FFD700;
}

/* input text */
input{
color:white !important;
font-size:16px !important;
}

input::placeholder{
color:#e0e0e0 !important;
}

/* buttons */
div.stButton > button{
background:rgba(0,0,0,0.4);
border:2px solid #00E5FF;
color:white;
font-size:18px;
padding:10px 25px;
border-radius:15px;
transition:0.3s;
}

div.stButton > button:hover{
transform:scale(1.15);
background:#FFD700;
color:black;
}

/* chat bubbles */
.userBubble{
background:#00E5FF;
padding:12px;
border-radius:10px;
margin:5px;
color:black;
}

.aiBubble{
background:#2E8B57;
padding:12px;
border-radius:10px;
margin:5px;
color:white;
}

/* footer */
.footer{
position:fixed;
bottom:10px;
right:20px;
color:white;
font-size:16px;
}

</style>
""", unsafe_allow_html=True)


# ---------- PAGE 1 ----------
if st.session_state.page == 1:

    st.markdown('<div class="centerTitle">example.ai</div>', unsafe_allow_html=True)

    st.write("")

    # smaller centered boxes
    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        username = st.text_input("Username")
        email = st.text_input("Email")

        if st.button("Enter"):
            if username and email:
                st.session_state.page = 2
                st.rerun()

    st.markdown('<div class="footer">Created by Team AiSyn</div>', unsafe_allow_html=True)


# ---------- PAGE 2 ----------
elif st.session_state.page == 2:

    st.markdown('<div class="topTitle">example.ai</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Your Personal AI Assistant</div>', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="userBubble">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="aiBubble">{msg["content"]}</div>', unsafe_allow_html=True)

    prompt = st.text_input("", placeholder="Ask anything")

    if prompt:

        st.session_state.messages.append({"role":"user","content":prompt})
        st.markdown(f'<div class="userBubble">{prompt}</div>', unsafe_allow_html=True)

        st.write("### Can I do it?")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("YES"):

                response="Yes! I can help you with that."

                placeholder=st.empty()
                text=""

                for char in response:
                    text+=char
                    placeholder.markdown(
                        f'<div class="aiBubble">{text}</div>',
                        unsafe_allow_html=True
                    )
                    time.sleep(0.03)

                st.session_state.messages.append({"role":"ai","content":response})

        with col2:
            if st.button("NO"):

                response="Alright! Ask something else."

                placeholder=st.empty()
                text=""

                for char in response:
                    text+=char
                    placeholder.markdown(
                        f'<div class="aiBubble">{text}</div>',
                        unsafe_allow_html=True
                    )
                    time.sleep(0.03)

                st.session_state.messages.append({"role":"ai","content":response})
