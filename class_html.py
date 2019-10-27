from __init__ import ITEM_HTML
from bs4 import BeautifulSoup

class ParsedItem:
    def __init__(self,page):
        self.soup = BeautifulSoup(page,'html.parser')

    def find_item_name(self):
        locator = "article.product_pod h3 a "
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name
    def find_item_link(self):
        locator = "article.product_pod h3 a "
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['href']
        return item_name

    def find_item_price(self):
        locator = "article.product_pod p.price_color "
        item_price = self.soup.select_one(locator).string
        return item_price[1:]

    def find_rating(self):
        locator = "article.product_pod p.star-rating"
        start_rating_tag = self.soup.select_one(locator)
        calsses = start_rating_tag.attrs['class']
        final_rate = [r for r in calsses if r != 'star-rating']
        return final_rate[0]


item = ParsedItem(ITEM_HTML)

print(item.find_rating())
print(item.find_item_name())
print(item.find_item_price())
print(item.find_item_link())
