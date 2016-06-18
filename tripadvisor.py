import json
import threading

import requests
from bs4 import BeautifulSoup


def get_details(current_resto):
    response = requests.get(current_resto['url'])
    soup = BeautifulSoup(response.text, 'html.parser')
    current_resto.update({
        'locality': soup.find(class_='locality').span.text,
        'phone': getattr(soup.find(class_='phoneNumber'), 'text', '')
    })


def main():
    base_url = 'https://www.tripadvisor.com'
    response = requests.get(base_url + '/Restaurants-g294079-Paraguay.html')
    soup = BeautifulSoup(response.text, 'html.parser')

    threads = []
    results = []
    restaurants = soup.find_all('div', class_='shortSellDetails')

    for restaurant in restaurants:
        link = restaurant.find(class_='property_title')
        current_resto = {
            'name': link.text.strip(),
            'url': base_url + link['href'],
            'cuisines': [c.text for c in restaurant.select('.cuisine')]
        }
        t = threading.Thread(target=get_details, args=(current_resto,))
        threads.append(t)
        t.start()
        results.append(current_resto)

    for t in threads:
        t.join()

    print json.dumps(results, indent=2)


if __name__ == '__main__':
    main()
