import streamlit as st
import google.generativeai as genai
import os
from file_extraction import FileExtractor

# Set the API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("No API key found. Please set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

#master prompt from prompt.txt
with open("prompt.txt", "r") as f:
    master_prompt = f.read()

#page title
st. title("AI Assignment Solver")
st. write("Welcome to my first Large Language Model (LLM) project! This Streamlit-based app is designed to assist with generating solutions for assignments by leveraging AI capabilities. It extracts the content from uploaded files (such as PDFs, Word documents, PowerPoint presentations, Excel sheets, and Python code) and uses a powerful language model to process the information and provide solutions.")
st.markdown('<h2 style="font-size: 24px;">Important Notice</h2>', unsafe_allow_html=True)
st.write("This app is solely a demonstration of LLM technology as part of my portfolio project. It is not intended for direct use in academic or professional assignments. If you choose to use this app for course or class assignments, please be aware that you are responsible for any issues related to plagiarism or academic integrity violations. I strongly encourage you to use the app for learning and inspiration rather than submitting AI-generated content as your own work.")
#file handling
assignment_instructions = st.file_uploader("Upload the assignment instruction file", type = ["pdf", "docx"])
if assignment_instructions is not None:
    file_extractor = FileExtractor(assignment_instructions)
    assignment_instructions_text = file_extractor.extract_text()
    extra_files = st.radio("Do you assignment related files, needed to be uploaded?", ("Yes", "No"))
    if extra_files == "Yes":
        extra_files = st.file_uploader("Upload the extra files", type = ["pdf", "docx", "xlsx", "csv", "txt"], accept_multiple_files = True)
        if extra_files is not None:
            extra_files_text = ""
            for file in extra_files:
                file_extractor = FileExtractor(file)
                extra_files_text += f"File: {file.name}\n"
                extra_files_text += file_extractor.extract_text() + "\n"

    #input special instructions
    special_instructions = st.text_area("Any special instructions?")

    #assemble the prompt
    if extra_files == "Yes":
        prompt = master_prompt + "assignment instructions document = " + assignment_instructions_text + "assignment related files content = " +  extra_files_text + "special instructions from user = " +special_instructions
    else:
        prompt = master_prompt + "assignment instructions document = " + assignment_instructions_text + "special instructions from user = " +special_instructions

    #generate button
    if st.button("Generate Solution"):
        response = model.generate_content(prompt)
        st.write(response.text)
