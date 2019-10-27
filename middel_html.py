from __init__ import ITEM_HTML
from bs4 import BeautifulSoup

soup = BeautifulSoup(ITEM_HTML,'html.parser')


def find_item_name():
    locator = "article.product_pod h3 a "
    item_link = soup.select_one(locator)
    item_name = item_link.attrs['href']
    return item_name



def find_item_price():
    locator = "article.product_pod p.price_color "
    item_price = soup.select_one(locator).string
    return item_price[1:]


def find_rating():
    locator = "article.product_pod p.star-rating"
    start_rating_tag = soup.select_one(locator)
    calsses = start_rating_tag.attrs['class']
    final_rate = [r for r in calsses if r != 'star-rating']
    return final_rate[0]

print(find_rating())
