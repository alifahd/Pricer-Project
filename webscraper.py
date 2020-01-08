import requests
from bs4 import BeautifulSoup

state = True;

while (state == True):
    url = input("Enter URL --> ")
    type(url)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    posts = soup.find(class_='price_FHDfG large_3aP7Z')

    if (posts == None):
        posts = soup.find(class_='price_FHDfG large_3aP7Z salePrice_kTFZ3').get_text()
    else:
        posts = posts.getText();

    print(posts)

#python webscraper.py
