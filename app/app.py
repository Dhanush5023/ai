import os
from langchain.llms import OpenAI
from langchain.utilities import SerpAPIWrapper
import streamlit as st

# Set API Keys
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "32342892897b45a2b341d365042684cedc97e3d366ef91f90024cfb9c3ae4150"  # Alternatively, load from .env

# Research Agent using SerpAPI
def research_agent(query):
    search = SerpAPIWrapper()
    return search.run(query)

# Use Case Generation Agent
def use_case_agent(industry_insights):
    llm = OpenAI(temperature=0.7)
    prompt = f"""
    Based on the following industry insights, generate 5 relevant AI/GenAI use cases:
    {industry_insights}
    """
    return llm(prompt)

# Streamlit App
st.title("Multi-Agent System for AI Use Case Generation")

company_or_industry = st.text_input("Enter a Company or Industry for Research")
if st.button("Generate Proposal"):
    st.write("Conducting research...")
    research = research_agent(company_or_industry)
    st.write(research)
