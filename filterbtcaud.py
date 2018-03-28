# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:38:17 2018

@author: bojack
"""

import requests
import json
import rethinkdb as r
url = 'https://rest.coinapi.io/v1/orderbooks/current?filter_symbol_id=BTC_AUD'
headers = {'X-CoinAPI-Key' : '6EE37647-0EE0-49F5-8BDE-80DA4BE1C592'}
response = requests.get(url, headers=headers)
text=json.loads(response.text)
r.connect('localhost',28015).repl()
r.db('test').table_create('data').run()
r.table('data').insert(text).run()   