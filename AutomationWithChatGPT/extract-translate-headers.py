import requests
from bs4 import BeautifulSoup
import googletrans

# Get html content from web page
url = 'https://www.techworld-with-nana.com/post/a-guide-of-how-to-get-started-in-it-in-2023-top-it-career-paths'
# url = 'https://www.linkedin.com/in/erhany/'
page = requests.get(url)

# Parse the page content
soup = BeautifulSoup(page.content, 'html.parser')

# Get all html headers
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Initialize Google translator
translator = googletrans.Translator()

# Translate each header to French
french_headers = []
for header in headers:
    translated_header = {
      "text": translator.translate(header.text, dest='fr').text,
      "name": header.name
    }
    # print(translate_result)
    french_headers.append(translated_header)

# print(french_headers)

# Save headers translated to French into an html file
with open('french_headers.html', 'w') as f:
    f.write('<html><head><title>Translated French Headers</title></head><body>\n')
    for header in french_headers:
        f.write(f'<{header["name"]}>{header["text"]}</{header["name"]}>\n')
    f.write('</body></html>\n')
