# AI Assignment Solver with Streamlit

This repository contains my first **Large Language Model (LLM)** project—an AI-powered assignment solver built using **Streamlit**. The app accepts various file formats (PDF, Word, PowerPoint, Excel, Python code) and generates assignment solutions using Google’s **Gemini 1.5 Flash** LLM.

[Deployed Here](https://ai-assignment-solver.streamlit.app/)

## Features

- **File Upload Support**: Handles multiple file formats (PDF, DOCX, PPTX, XLSX, PY).
- **AI-Generated Solutions**: Uses the Gemini 1.5 Flash LLM to generate step-by-step solutions.
- **Multiple Related Files**: Allows users to upload related files (like data or code) and integrates their content into the solution generation process.
- **Streamlit-Based UI**: Simple, intuitive interface for uploading files and receiving results.

## How It Works

1. **Upload Assignment**: You can upload your assignment in supported formats (PDF, DOCX, PPTX, XLSX, or Python code).
2. **Solution Generation**: The app reads the content from your files, sends it to the Gemini model, and generates a detailed solution based on the assignment’s instructions.
3. **Receive Results**: The AI provides a structured solution, which you can review and use for learning purposes.

### Supported File Types

- PDF (.pdf)
- Word Document (.docx)
- PowerPoint (.pptx)
- Excel Spreadsheet (.xlsx)
- Python Code (.py)

## Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.8+
- Google Gemini API access (API key required)

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SUKHMAN-SINGH-1612/ai-assignment-solver.git
   cd ai-assignment-solver
2. Create a Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
4. Set Google API Key:
   ```bash
   export GOOGLE_API_KEY="your-google-api-key"
5. Run the Streamlit App:
   ```bash
    streamlit run main.py

## How to Use
1. Upload your assignment file in the supported formats (PDF, DOCX, PPTX, XLSX, PY).
2. Optionally, upload any additional related files.
3. Click "Generate Solution" to have the LLM process the assignment and provide a solution.
4. The solution is displayed within the app for you to review.
## Project Purpose
This app was built as part of my portfolio project to explore the integration of LLMs with file handling and natural language understanding. The app is a demonstration of:
- Working with file uploads in Streamlit.
- Parsing multiple file formats.
- Interfacing with Google’s Gemini LLM API to generate content.

## Important Disclaimer
This app is intended for demonstration purposes only. It is not designed to be used for actual coursework or assignments. If you use the app for academic purposes, you are responsible for ensuring compliance with academic integrity policies. This project serves as a learning and portfolio tool, and I do not encourage or endorse its use for cheating or plagiarism.

## Future Improvements
- Enhance parsing for additional file types.
- Optimize the integration for even more complex file structures.
- Add support for other LLM APIs.
- Improve UI/UX.
