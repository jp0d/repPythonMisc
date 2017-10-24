# import system related libraries
import os
import io
import math
import shutil
import traceback
import logging
import sys
# import time and date related libraries
from datetime import datetime
from datetime import timedelta
import time
# import web interaction libraries
import requests
import json
import urllib
import urllib3
import bs4
import numpy as np
import pandas as pd

def coinNews(coin, element):
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	url = 'https://www.google.com.au/search?safe=active&tbm=nws&q=' + coin + '+coin'
	res = requests.get(url, verify=False)
	data = bs4.BeautifulSoup(res.text, 'html.parser')

	for d in data.select(element):
		print(d.getText())


def main(argv):
	coinNews(argv[1], argv[2])

if __name__ == "__main__":
	main(sys.argv)