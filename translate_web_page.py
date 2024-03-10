import requests
from googletrans import Translator
from bs4 import BeautifulSoup


def translate_web_page(url):
    try:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extracting text from the HTML content
        text = soup.get_text()
        translator = Translator()
        translated_text = translator.translate(text, dest='bn')

        return translated_text.text

    except Exception as e:
        print("Error translating", e)
        return None


url = 'https://towardsdatascience.com/translate-any-two-languages-in-60-lines-of-python-b54dc4a9e739'
translated_content = translate_web_page(url)
print(translated_content)
