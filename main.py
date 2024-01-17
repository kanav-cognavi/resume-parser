import streamlit as st
import pdfplumber
from langchain.output_parsers.json import SimpleJsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4",temperature=0.7,openai_api_key="add your open api key here")  # Adjust temperature for creativity
output_parser = SimpleJsonOutputParser()
st.title("Resume Parser")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file:
    pdf = pdfplumber.open(uploaded_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

    resume_prompt = """
            This is the text of a parsed resume {text}
            Please read through the text and extract following keys:
            name, email, skills, education_records
            Give the response in json format
    """
    prompt = ChatPromptTemplate.from_template(resume_prompt)

    chain = prompt | model | output_parser
    st.write("Parsed Resume in json")
    st.write(chain.invoke({"text":text}))
