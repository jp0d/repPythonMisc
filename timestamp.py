import os
import io
import time
from datetime import datetime
import requests
import json
import urllib
import bs4
import math
import numpy as np
import pandas as pd

def main():
	url = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym=SC&tsyms=BTC,USD,AUD&ts='
	t = datetime.datetime(1452680400)
	furl = url + str(time.mktime(t1.timetuple()))
	data = requests.get(furl)
	print(data.text)

if __name__ == "__main__":
	main()

