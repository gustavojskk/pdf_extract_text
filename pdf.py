import fitz
import json
import nltk
from nltk import sent_tokenize

nltk.download('punkt')

def extract_text_from_pdf(pdf_path):
    text_data = []

    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text_data.append(page.get_text())

    return text_data

def organize_text_into_topics(text_data):
    topics = []

    for page_text in text_data:
        paragraphs = page_text.split('\n\n')
        topics.extend(paragraphs)

    return topics

def generate_questions(topics):
    questions = []

    for topic in topics:
        sentences = sent_tokenize(topic)
        
        if sentences:
            question = {
                'topic': topic,
                'questions': [f"What is {sent}?" for sent in sentences]
            }
            questions.append(question)

    return questions

def save_to_json(data, json_path):
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    pdf_path = "khomp.pdf"
    json_path = "saida.json"

    text_data = extract_text_from_pdf(pdf_path)
    topics = organize_text_into_topics(text_data)
    questions = generate_questions(topics)

    save_to_json(questions, json_path)
