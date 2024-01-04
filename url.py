import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Input URL
# url = input("Enter the URL: ")
url = "https://www.geeksforgeeks.org/what-is-an-operating-system/"

# Web scraping
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    article_element = soup.find('div', class_='text')
    if article_element:
        article_text = article_element.get_text()



html_content = response.content.decode('utf-8')

print(html_content)



















# NLP Question-Answering Model

# qa_model = pipeline("question-answering")
# question = input("Ask a question: ")
# answer = qa_model(question=question, context=html_content)

# print("Answer:", answer['answer'])