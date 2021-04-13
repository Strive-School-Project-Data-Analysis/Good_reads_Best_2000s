import requests
from bs4 import BeautifulSoup

url = 'https://www.goodreads.com/list/show/5.Best_Books_of_the_Decade_2000s?page=1'

def get_data(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    return soup


def get_next_page(soup):
    """This Function returns the URL to the next page on the list"""


    pages = soup.find('div', {'class': 'pagination'})
    if not pages.find('span', {'class': 'next_page disabled'}):
        url = 'https://www.goodreads.com/'+str(pages.find(class_='next_page')['href'])
        return url
    else:
        return


while True:
    soup = get_data(url)
    #book_info(soup)
    url = get_next_page(soup)
    if not url:
        break
    else:
        print(url)