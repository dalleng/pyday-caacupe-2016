import json

import requests
from bs4 import BeautifulSoup


def get_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return {
        'locality': soup.find(class_='locality').text[:-2],
        'phone': getattr(soup.find(class_='phoneNumber'), 'text', '')
    }


def main():
    base_url = 'https://www.tripadvisor.com'
    response = requests.get(base_url + '/Restaurants-g294079-Paraguay.html')
    soup = BeautifulSoup(response.text, 'html.parser')

    restaurants = soup.find_all('div', class_='shortSellDetails')
    results = []

    for restaurant in restaurants:
        link = restaurant.find(class_='property_title')
        current_resto = {
            'name': link.text.strip(),
            'url': base_url + link['href'],
            'cuisines': [c.text for c in restaurant.select('.cuisine')]
        }
        current_resto.update(get_details(current_resto['url']))
        results.append(current_resto)

    print json.dumps(results, indent=2)


if __name__ == '__main__':
    main()
