import requests
import pandas as pd
from datetime import datetime

def fetch_live_nav(scheme_code):
    url = f'https://api.mfapi.in/mf/{scheme_code}'
    response = requests.get(url)
    data = response.json()
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']
    name = data['meta']['scheme_name']
    print(f'Fund: {name}')
    print(f'NAV: {nav}')
    print(f'Date: {date}')
    return {'name': name, 'nav': nav, 'date': date}

if __name__ == '__main__':
    fetch_live_nav(119551)
    print('Live NAV fetch complete!')
