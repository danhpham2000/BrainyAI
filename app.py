import streamlit as st


dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon=":material/dashboard:")
history = st.Page("pages/history.py", title="History", icon=":material/history:")

chatbot = st.Page("pages/chatbot.py", title="Chatbot", icon=":material/robot:")




pg = st.navigation({
    "Profile": [dashboard, history],
    "BrainyAI": [chatbot]
})

pg.run()