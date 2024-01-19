from img_to_text import to_text
from pdf_to_img import to_img
from question_answering import get_answer
poppler_path = r"C:\Program Files\poppler-23.11.0\Library\bin"
tesseract_path = r'C:\Program Files\tesseract\tesseract.exe'

def pdf_to_text(pdf_file):
    text = ""
    images = to_img(poppler_path, pdf_file)
    for img in images:
        text += to_text(tesseract_path, img)
    return text

import gradio as gr

demo = gr.Blocks()

with demo:
    gr.Markdown("Upload a pdf")
    file_input = gr.File()
    question_field = gr.Textbox()
    upload_button = gr.Button("upload")
    text_output = gr.Textbox()


    def start(file_input, question_field):
        docs_text = pdf_to_text(file_input)
        answer = get_answer(docs_text, question_field)
        return answer


    upload_button.click(start, inputs=[file_input, question_field], outputs=[text_output])


demo.queue().launch(share=True, debug=True)