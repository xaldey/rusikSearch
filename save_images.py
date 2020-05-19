import requests as req
from parse_site import main_array
import csv
from parse_site import UserAgent
FILE = 'results/export.csv'
DIR_FOR_IMAGES = 'results/'

link_array = []


def read_file(file):
    with open(FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            link_array.append({
                'name': row[0],
                'link': row[2],
            })
            line_count += 1
            # print(row)
    # link_array.remove('Image Link')


print('*' * 50)
# print(link_array)


def download_image(array):
    for item in array:
        with req.get(item['link']) as rq:
            with open(DIR_FOR_IMAGES + item['name'] + '.jpg', 'wb') as file:
                file.write(rq.content)
                print(f'Downloading {file}')


if __name__ == '__main__':
    read_file(FILE)
    # print(link_array)
    download_image(link_array)


