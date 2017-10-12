import os
import io
import time
from datetime import datetime
from datetime import timedelta
import requests
import json
import urllib
import urllib3
import bs4
import math
import numpy as np
import pandas as pd

def main(coin, days):
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	url = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym=' + coin + '&tsyms=BTC,USD,AUD&ts='
	t1 = datetime.fromtimestamp(1420070400)
	furl = url + str(time.mktime(t1.timetuple()))
	http = urllib3.PoolManager()
	data = http.request('GET',furl)
	#	print(response.data)
	
	t2 = t1 + timedelta(days=days)
	counter = 0;
	
	while(t2 < datetime.now()):
		counter += 1
		t2 = t2 + timedelta(days=days)
		furl = url + str(time.mktime(t2.timetuple()))
#		data = http.request('GET', furl)
		data = http.urlopen('GET', furl)
#		print(furl)
		print(str(counter) + str(data.data) + ' timestamp:' + t2.strftime('%Y-%m-%dT%H:%M%SZ'))

if __name__ == "__main__":
	main('SC', 30)

