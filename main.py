import argparse
import os
import requests

from dotenv import load_dotenv
from typing import Dict, Optional
from urllib.parse import urlparse


def is_bitlink(url: str, headers: Dict[str, str]) -> bool:
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    resp = requests.get(f'{api_url}{url}', headers=headers)
    return resp.ok


def parse_url(url: str) -> str:
    parse = urlparse(url)
    netloc = parse.netloc
    path = parse.path
    return f'{netloc}{path}'


def count_clicks(bitlink: str, headers: Dict[str, str]) -> str:
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    params = (
        ('unit', 'month'),
        ('units', '-1'),
    )
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()['total_clicks']


def shorten_link(url: str, headers: Dict[str, str]) -> str:
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {
        'group_guid': 'Bm6363FiCth',
        'domain': 'bit.ly',
        'long_url': f'{url}'
    }
    resp = requests.post(api_url,
                         headers=headers,
                         json=payload
                         )

    resp.raise_for_status()
    return resp.json()['link']


def main(url: str):

    token = os.getenv('BIT_ACCESS_TOKEN')
    headers = {'Authorization': f'Bearer {token}'}
    try:
        bitlink = parse_url(url)
        if is_bitlink(bitlink, headers):
            print('short url provided')
            click_count = count_clicks(bitlink, headers)
            print(f'Total clicks count: {click_count}')
        else:
            short_url = shorten_link(url, headers)
            print(short_url)
    except requests.exceptions.HTTPError as err:
        print(f'an error occurred\n{err}')


if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL to be shorten')
    args = parser.parse_args()
    main(args.url)
