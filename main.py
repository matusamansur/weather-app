import requests
from bs4 import BeautifulSoup

#city = input("Type the name of the city: ")
#queryFormatted = city.replace(" ", "+") + "weather"
#url = "https://www.google.com/search?q=" + queryFormatted

url = "https://www.google.com/search?q=vitoria+weather"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
    }

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

fullWeather = soup.find('div', id="wob_wc")
location = fullWeather.find('div', id="wob_loc").text

#print(fullWeather)
print(location)