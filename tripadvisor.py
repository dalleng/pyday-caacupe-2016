import json

import requests
from bs4 import BeautifulSoup


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
        results.append(current_resto)

    print json.dumps(results)


if __name__ == '__main__':
    main()
