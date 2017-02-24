import requests
from lxml import html


class LeBonCoinScrapper:

    def get_html_page(self, category, where, query, zip_code_list, min_price,
                      max_price, in_title):
        '''c (category) : Category TODO : Get category dict
        w (where) : town  TODO : Get town dict
        q (query) : query
        location (zip_code) : string of all zip code (with , between them)
        WARNING : location has to comply with w
        ps : min price WARNING : Value depends on category
        pe : max price WARNING : Value depends on category
        it (in title) : Boolean : query in title (1 or 0)
        ur (urgent) ; Show only urgent ad (1 or 0)
        '''
        zip_codes = ', '.join(zip_code_list)
        searching_page = requests.get(
            'https://www.leboncoin.fr/annonces/offres/ile_de_france/',
            params={'c': category, 'w': where, 'q': query,
                    'location': zip_codes, 'ps': min_price, 'pe': max_price,
                    'it': in_title})
        return html.fromstring(searching_page.content)

    def get_items_title(self, html_page):
        ''' Return list of all title in html page (from top to the bottom)'''

        title_html = html_page.xpath("//section[@id='listingAds']"
                                     "//h2[@class='item_title']/text()")
        title_list = []
        for title in title_html:
            title_list.append(title.strip())
        return title_list

    def get_items_date(self, html_page):
        ''' Return list of all dates in html page (from top to the bottom)'''

        date_html = html_page.xpath("//section[@id='listingAds']"
                                    "//aside[@class='item_absolute']"
                                    "/p[@class='item_supp']/@content")
        date_list = []
        for date in date_html:
            date_list.append(date.strip())
        return date_list

    def get_items_price(self, html_page):
        ''' Return list of all dates in html page (from top to the bottom)'''

        price_html = html_page.xpath("//section[@id='listingAds']"
                                     "//h3[@class='item_price']/@content")
        price_list = []
        for price in price_html:
            price_list.append(price.strip())
        return price_list
