from docx2pdf import convert
import os, sys

def convert_word_to_pdf(input_path, output_path):
    try:
        convert(input_path, output_path)
        print(f"Conversion completed. PDF saved as {output_path}")
    except Exception as e:
        print(f"An Error occurred: {str(e)}")

if __name__ == "__main__":
    input_path = r"C:\Users\Naren\Desktop\Data Science End to End Projects\Word-Doc-to-PDF-Using-Python\Java.docx"

    output_path = r"C:\Users\Naren\Desktop\Data Science End to End Projects\Word-Doc-to-PDF-Using-Python\output.pdf"

    if os.path.exists(input_path):
        convert_word_to_pdf(input_path, output_path)
    
    else:
        print(f"Input word document file '{input_path}' does not exist")

