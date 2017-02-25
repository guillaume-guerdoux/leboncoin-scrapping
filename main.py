import requests
import json
from leboncoin_scrapper import LeBonCoinScrapper
from utils import *
from twilio.rest import TwilioRestClient

if __name__ == "__main__":
    ''' Structure of main_dict :
            {query1 : ([category1, category2, ], max_price, in_title),
             query2 : ([category1, category2, ], max_price, in_title)}'''

    main_dict = {'Ecran ordinateur': ([16, 15], 6, 1)}
                 #'Console PS4': ([43], 14, 1)}

    scrapper = LeBonCoinScrapper(main_dict, 1, ['92160'])

    ad_list = scrapper.process_requests()

    body = 'Une nouvelle anonce a été passée \n'
    for query, query_ads in ad_list.items():
        for category_ad in query_ads:
            for ad in category_ad:
                print(ad)
                title = ad[0]
                price = ad[2]
                place = ad[3]
                body += (title + "\n" +
                         price + '€ à ' + place + '\n')

    with open('config/phone_number.json') as phoneNumbers:
        phones_numbers = json.load(phoneNumbers)
        send_text_messages(phones_numbers[0]['destinataire'],
                           phones_numbers[0]['expediteur'], body)
