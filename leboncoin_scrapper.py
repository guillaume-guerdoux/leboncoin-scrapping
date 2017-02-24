import requests
from lxml import html


class LeBonCoinScrapper:

    def __init__(self, main_dict, where, zip_code_list=[]):
        ''' Structure of main_dict :
                {query1 : ([category1, category2, ], max_price, in_title),
                 query2 : ([category1, category2, ], max_price, in_title)}'''
        self.main_dict = main_dict
        self.where = where
        self.zip_code_list = zip_code_list

    def get_html_page(self, category, query, max_price, in_title):
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
        zip_codes = ', '.join(self.zip_code_list)
        searching_page = requests.get(
            'https://www.leboncoin.fr/annonces/offres/ile_de_france/',
            params={'c': category, 'w': self.where, 'q': query,
                    'location': zip_codes, 'pe': max_price,
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

    def process_requests(self):
        final_result = {}
        for query, parameters in self.main_dict.items():
            final_result[query] = []
            price_max = parameters[1]
            in_title = parameters[2]
            for category in parameters[0]:
                html_page = self.get_html_page(category, query,
                                               price_max, in_title)
                title_list = self.get_items_title(html_page)
                date_list = self.get_items_date(html_page)
                price_list = self.get_items_price(html_page)
                combination_list = []
                for index, date in enumerate(date_list):
                    combination_list.append((title_list[index], date,
                                             price_list[index]))
                final_result[query].append(combination_list)
        return final_result
