import requests
from bs4 import BeautifulSoup

def get_text(URL):

# Making a GET request
    r = requests.get(URL)

# Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('div', class_='entry-content')

    lines = s.find_all('p')

    bar_names = []

    for line in lines:
        line_array = line.get_text("|", strip=True).split("|")
        for item in line_array:
            bar_names.append(item)



    return bar_names




