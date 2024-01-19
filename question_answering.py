from transformers import pipeline

def get_answer(context, question):
    qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")
    return qa_model(question = question, context = context)

