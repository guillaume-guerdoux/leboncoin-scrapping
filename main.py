import requests


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

searching_page = requests.get(
    'https://www.leboncoin.fr/annonces/offres/ile_de_france/',
    params={'c': 16, 'w': 1, 'q': 'Ecran ordinateur',
            'location': '91300, 92160', 'pe': 6, 'it': 0})
print(searching_page.url)
