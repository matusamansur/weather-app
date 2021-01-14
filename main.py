import requests
from bs4 import BeautifulSoup

while True:
    
    city = input("Type the name of the city: ")
    queryFormatted = city.replace(" ", "+") + "+weather"
    url = "https://www.google.com/search?q=" + queryFormatted
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    fullWeather = soup.find_all('div', id='wob_wc')
    location = fullWeather[0].find('div', id="wob_loc").text
    date = fullWeather[0].find('div', id="wob_dts").text
    weather = fullWeather[0].find('span', id="wob_dc").text
    temperatureC = fullWeather[0].find('span', id="wob_tm").text
    temperatureF = fullWeather[0].find('span', id="wob_ttm").text
    rain = fullWeather[0].find('span', id="wob_pp").text
    humidity = fullWeather[0].find('span', id="wob_hm").text
    windKPH = fullWeather[0].find('span', id="wob_ws").text
    windMPH = fullWeather[0].find('span', id="wob_tws").text

    opt = input("Press (1) for (Celsius & km/h) or (2) for (Fahrenheit & mph) ")
    print("\n" + location + " - " + date)
    print(weather + " - " + temperatureC + " °C") if opt != 1 else print(weather + " - " + temperatureF + " °F")
    print("Rain: " + rain + " - " + "Humidity: " + humidity + " - " + "Wind: " + windKPH + "\n") if opt != 1 else print("Rain: " + rain + " - " + "Humidity: " + humidity + " - " + "Wind: " + windMPH + "\n")

    opt = input("Press (1) to search another city or (0) to exit the program ")
    if(opt == '0'):
        print("Exiting...")
        exit(0)