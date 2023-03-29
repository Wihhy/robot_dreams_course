import requests

URL_FOR_WEATHER = 'https://api.open-meteo.com/v1/forecast'
URL_FOR_SEARCH = 'https://geocoding-api.open-meteo.com/v1/search?name='
CITY = ''
LATITUDE = ''
LONGITUDE = ''


# Приймає від користувача назву міста та записує цю назву у глобальну змінну city
def take_city():
    global CITY
    CITY = input('Напишіть місто для якого ви хочете отримати погоду у форматі "Kharkiv":\n')


# Виконує пошук міста зв переданою назвою, перепитує у користувача, та записує координати
def search_city():
    search = requests.get(url=f'{URL_FOR_SEARCH}{CITY}')
    result = search.json()['results']
    for item in result:
        valid = input(f'Ви маєте на увазі місто {item["name"]}, {item["country"]}, {item["admin1"]}?\n'
                      f'Відповідайте yes, або no\n')
        if valid.lower() == 'yes':
            global LATITUDE, LONGITUDE
            LATITUDE = item['latitude']
            LONGITUDE = item['longitude']
            break


# Родить запит поточної погоди за визначеними координатами і друкує її у консоль
def request_weather():
    weather_response = requests.get(url=f'{URL_FOR_WEATHER}?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true')
    weather = weather_response.json()
    print(f'Поточна погода у місті {CITY}:\n'
          f'Температура: {weather["current_weather"]["temperature"]} градусів цельсію\n'
          f'Швидкість вітру: {weather["current_weather"]["windspeed"]} кілометрів за годину\n')


if __name__ == '__main__':
    while True:
        try:
            take_city()
            search_city()
            request_weather()
        except Exception as exc:
            print(exc)
            continue
