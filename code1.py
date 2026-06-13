from google import genai
import streamlit as st
client = genai.Client(api_key='AQ.Ab8RN6JXKF1rbcLJWBYyUg6Oke7OXCe-33p1PRoY4OdTlnbNZw')

st.title("Talk to Agent")
st.writer("This app demonstrates a conservational agent.")

user_input = st.text_input("Ask a Question:")
if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
    response = client.models.generate_content(
        model = 'gemini-flash-latest', contents=user_input
    )
    st.write(response.text)
    