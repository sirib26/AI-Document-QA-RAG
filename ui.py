import streamlit as st
import requests

st.title("📄 AI Document Q&A System")

question = st.text_input("Ask a question about your document")

if st.button("Submit"):
    if question:
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": question}
        )
        answer = response.json()["answer"]
        st.write("### Answer:")
        st.write(answer)