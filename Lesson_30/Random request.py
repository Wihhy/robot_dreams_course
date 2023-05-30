import requests
import random
import unittest
from unittest.mock import patch


urls = [
    'google.com',
    'apple.com',
    'facebook.com',
    'twitter.com',
    'amazon.com',
]


def get_random_request(urls_list):
    url = random.choice(urls_list)
    res = requests.get(f'https://{url}')
    return f'Зроблено запит на сайт {url}, отримано статус код: {res.status_code}, довжина HTML-коду :{len(res.text)}'


print(get_random_request(urls))


class TestGetRandomRequest(unittest.TestCase):
    @patch('requests.get')
    def test_get_random_request(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = '<html><body>Test</body></html>'
        random_url = 'google.com'
        with patch('random.choice', return_value=random_url):
            result = get_random_request(urls)
            mock_get.assert_called_once_with(f'https://{random_url}')
            self.assertIn(f'Зроблено запит на сайт {random_url}', result)
            self.assertIn('отримано статус код: 200', result)

    @patch('requests.get')
    def test_get_random_request_failed_request(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        random_url = 'example.com'
        with patch('random.choice', return_value=random_url):
            result = get_random_request(urls)
            mock_get.assert_called_once_with(f'https://{random_url}')
            self.assertIn(f'Зроблено запит на сайт {random_url}', result)
            self.assertIn('отримано статус код: 404', result)
            self.assertIn('довжина HTML-коду :0', result)
