import requests
from leboncoin_scrapper import LeBonCoinScrapper

''' Structure of main_dict :
        {query1 : ([category1, category2, ], max_price, in_title),
         query2 : ([category1, category2, ], max_price, in_title)}'''

main_dict = {'Ecran ordinateur': ([16, 15], 6, 1),
             'Console PS4': ([43], 14, 1)}

scrapper = LeBonCoinScrapper(main_dict, 1, ['91300', '92160'])

print(scrapper.process_requests())
