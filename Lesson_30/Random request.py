import requests
import random

urls = [
    'google.com',
    'apple.com',
    'facebook.com',
    'twitter.com',
    'amazon.com',
]

url = random.choice(urls)
res = requests.get(f'https://{url}')
print(f'Зроблено запит на сайт {url}, отримано статус код: {res.status_code}, довжина HTML-коду :{len(res.text)}')

