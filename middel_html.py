from __init__ import ITEM_HTML
from bs4 import BeautifulSoup

soup = BeautifulSoup(ITEM_HTML,'html.parser')


def find_item_name():
    get_title = soup.find_all('h3','title')
    return get_title


print(find_item_name())
