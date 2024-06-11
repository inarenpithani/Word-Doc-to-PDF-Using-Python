from utils.helper import WordToPDFConverter

def convert_word_to_pdf(input_path, output_path):
    try:
        WordToPDFConverter.convert_word_to_pdf(input_path, output_path)

        return f"Conversion completed. PDF saved as {output_path}"
    except Exception as e:
        return f"An Error occuered: {str(e)}"