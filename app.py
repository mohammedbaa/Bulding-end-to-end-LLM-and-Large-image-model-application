from dotenv import load_dotenv
load_dotenv() ## load all the environment variables 


import streamlit as st 
import os 
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gimini pro model and get response 

model=genai.GenerativeModel("gemini-2.5-pro")

def get_gemini_response(qustion):
    response=model.generate_content(qustion)
    return response.text

## init streamlit app 
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input:",key="input")

submit=st.button("Ask the Qustion")

## When Submit is clicked 
if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)