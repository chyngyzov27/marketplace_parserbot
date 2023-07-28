from requests import get
from bs4 import BeautifulSoup
import csv

MAIN_URL = 'https://enter.kg/graficheskie-planshety_bishkek'

def get_html(url):
    response = get(url)
    return response.text


def write_to_csv(data):
    with open("enter_kg.csv", 'a') as file1:
        writer = csv.writer(file1, delimiter='/')
        writer.writerow((data['title'],
                         data['price'],
                         data['img']))


def get_product_data(html):
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find_all('div', class_='row')

    for product in products:
        img = product.find('a').find('img').get('src')
        title = product.find('div', class_='rows').find('a').text
        price = product.find('span', class_='price').text

        data = {'title': title, 'price': price, 'img': img}
        write_to_csv(data)


def main():
    get_product_data(get_html(MAIN_URL))


main()