import requests
from leboncoin_scrapper import LeBonCoinScrapper

scrapper = LeBonCoinScrapper()
searching_page = scrapper.get_html_page(16, 1, 'Ecran ordinateur',
                                        ['91300', '92160'], None, 6, 0)
titles = scrapper.get_items_title(searching_page)
dates = scrapper.get_items_date(searching_page)
prices = scrapper.get_items_price(searching_page)
print(titles, dates, prices)
