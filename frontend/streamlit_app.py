import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="LLM Guardrails Gateway",
    layout="centered"
)

st.title(" LLM Guardrails Gateway")

st.write("Secure AI Middleware")

user_input = st.text_area(
    "Enter your prompt"
)

if st.button("Execute"):

    payload = {
        "message": user_input
    }

    try:

        response = requests.post(
            API_URL,
            json=payload
        )

        if response.status_code == 200:

            data = response.json()

            st.success("Validated Response")

            st.write(data["response"])

        else:

            st.error(response.json()["detail"])

    except Exception as e:

        st.error(f"Error: {str(e)}")