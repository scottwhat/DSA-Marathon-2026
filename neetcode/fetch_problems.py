import requests
from bs4 import BeautifulSoup
import json

url = "https://neetcode.io/roadmap"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Save the HTML to inspect
with open('neetcode_page.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

print("HTML saved to neetcode_page.html")
