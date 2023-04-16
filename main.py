import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(url, headers):
    payload = {'long_url': url}
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    response_dict = response.json()
    return response_dict['link']


def count_clicks(url, headers):
    parsed = urlparse(url)
    if parsed.scheme:
        url = f'{parsed.netloc}{parsed.path}'
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(url)
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    response_dict = response.json()
    return response_dict['total_clicks']


def is_bitlink(url, headers):
    parsed = urlparse(url)
    if parsed.scheme:
        url = f'{parsed.netloc}{parsed.path}'
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url)
    response = requests.get(api_url, headers=headers)
    return response.ok


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Обработка введенных в консоль URL-адресов')
    parser.add_argument('link', help='Cсылки')
    args = parser.parse_args()

    bitly_token = os.getenv('BITLY_TOKEN')
    headers = {'Authorization': f'Bearer {bitly_token}'}

    if is_bitlink(args.link, headers):
        print('Кол-во переходов по ссылке битли: ', count_clicks(args.link, headers))
    else:
        print('Короткая ссылка: ', shorten_link(args.link, headers))


if __name__ == '__main__':
    main()