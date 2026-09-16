import requests
from bs4 import BeautifulSoup

url = input(" Enter website URL (like https://example.com): ")

# Ask the website for its words
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the big titles
titles = soup.find_all('h1')

print("\n Big titles on this page:")
for title in titles:
    print("- " + title.text)
