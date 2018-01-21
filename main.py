import requests
import json
from leboncoin_scrapper import LeBonCoinScrapper
from utils import *
from twilio.rest import TwilioRestClient

import numpy as np

if __name__ == "__main__":


    #fast_text = np.fromfile(file='fast_text/wiki.fr.vec', count=10000000)
    '''embedding = dict()
    i = 0
    with open('fast_text/wiki.fr.vec') as infile:
        for line in infile:
            print(i)
            if i > 10000:
                break
            else:
                word, vec_s = line.strip().split(' ', 1)
                vec = np.array([float(v) for v in vec_s.split(' ')])
                embedding[word] = vec
                i += 1'''
    '''Structure of main_dict :
            {query1 : ([category1, category2, ], max_price, in_title),
             query2 : ([category1, category2, ], max_price, in_title)}'''

    main_dict = {'Ecran ordinateur': ([16, 15], 20, 1)}
                 #'Console PS4': ([43], 14, 1)}

    scrapper = LeBonCoinScrapper(main_dict, 1, ['75012'])

    ad_list = scrapper.process_requests()
    body = 'Une nouvelle anonce a été passée \n'
    for query, query_ads in ad_list.items():
        for category_ad in query_ads:
            for ad in category_ad:
                title = ad[0]
                price = ad[2]
                place = ad[3]
                body += (title + "\n" +
                         price + '€ à ' + place + '\n')
    print(body)
    if body != 'Une nouvelle anonce a été passée \n':
        print("ok")
        '''with open('config/phone_number.json') as phoneNumbers:
            phones_numbers = json.load(phoneNumbers)
            send_text_messages(phones_numbers[0]['destinataire'],
                               phones_numbers[0]['expediteur'], body)'''
