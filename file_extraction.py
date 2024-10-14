import os
import PyPDF2
import docx
import pandas as pd

#class to extract/parse text from different file formats
class FileExtractor:
    def __init__(self, file):
        self.file = file
        self.file_extension = self.get_file_extension()
    
    #function to get the file extension
    def get_file_extension(self):
        return self.file.name.split('.')[-1].lower()
    
    #function to extract text from a PDF file
    def extract_text_from_pdf(self):
        reader = PyPDF2.PdfReader(self.file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    
    #function to extract text from a Word (.docx) file
    def extract_text_from_word(self):
        doc = docx.Document(self.file)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text

    
    #function to extract text from an Excel (.xlsx) file
    def extract_text_from_excel(self):
        df = pd.read_excel(self.file)
        text = ""
        for col in df.columns:
            text += ' '.join(df[col].astype(str).tolist()) + "\n"
        return text
    
    #function to extract text from a CSV file
    def extract_text_from_csv(self):
        df = pd.read_csv(self.file)
        text = ""
        for col in df.columns:
            text += ' '.join(df[col].astype(str).tolist()) + "\n"
        return text
    
    #function to extract text from a text file
    def extract_text_from_text(self):
        with open(self.file, 'r') as f:
            text = f.read()
        return text
    
    #function to extract text from the uploaded file based on the file extension
    def extract_text(self):
        if self.file_extension == "docx":
            return self.extract_text_from_word()
        elif self.file_extension == "pptx":
            return self.extract_text_from_ppt()
        elif self.file_extension == "xlsx":
            return self.extract_text_from_excel()