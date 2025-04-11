import streamlit as st
import os


if "messages" not in st.session_state:
    st.session_state["messages"] = []


st.header("Chat with BrainyAI")
uploaded_files = st.file_uploader("Upload your documents", accept_multiple_files=True)

for upload_file in uploaded_files:
    with open(os.path.join("documents", upload_file.name),"wb") as f:
        f.write(upload_file.getbuffer())
              
    













