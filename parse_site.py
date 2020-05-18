import csv
import requests, shutil
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

UserAgent().chrome
MAIN_URL = 'http://camgirlvideos.org/page/'
FILE = 'results/export2-500.csv'
main_array = []


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Title', 'Link', 'Image Link', 'Date published'])
        for elem in items:
            writer.writerow([elem['title'], elem['link'], elem['image_link'], elem['date_published']])


print('*' * 50)


def make_array():
    for page in range(2, 500):
        page_link = MAIN_URL + str(page)
        print(page_link)
        response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
        # for key, value in response.request.headers.items():
        #     print(key + ": " + value)
        page_array = []
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        # title = soup.html.head.title.text
        obj = soup.findAll('div', class_="hentry-pad blocks")
        for elem in obj:
            page_array.append({
                'title': elem.find('h4', class_="entry-title").get_text(),
                'link': elem.find('a').get('href'),
                'image_link': elem.find('img').get('src'),
                'date_published': elem.find('time', class_="date time published updated sc").get('datetime'),
            })
            # print(page_array)
        main_array.extend(page_array)
        print('*' * 50)
        time.sleep(1)
        save_file(main_array, FILE)


def save_image():
    pass


if __name__ == '__main__':
    make_array()
