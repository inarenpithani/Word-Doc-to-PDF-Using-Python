import gradio as gr
from utils.convert_helper import convert_word_to_pdf

def gradio_convert_word_to_pdf(input_word):
    try:
        input_word_path = input_word.name
        output_pdf_path = r"C:\Users\Naren\Desktop\Data Science End to End Projects\Word-Doc-to-PDF-Using-Python\output2.pdf"

        result_message = convert_word_to_pdf(input_word_path, output_pdf_path)

        return result_message 
    except Exception as e:
        return f"An Error Occurred: {str(e)}"


# Create gradio based User interface

iface =  gr.Interface(fn = gradio_convert_word_to_pdf,
                      inputs = gr.inputs.File(label = "Input Word DOcument", type = "file"),
                      outputs = gr.outputs.Textbox(label = "Converstion Status"),
                      live = True,
                      title = "Word to PDF Converter",
                      description = "Convert Word documents to PDF files",
                      )

if __name__ == "__main__":
    iface.launch()