import time
import os
import ssl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import mechanize
from str_searcher import string_exctractor
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import csv
import MySQLdb
import sqlalchemy
from sqlalchemy import create_engine
from html_table_extractor.extractor import Extractor
from datetime import datetime
def brow():
    browser= mechanize.Browser()
    browser.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')]
    browser.set_handle_robots(False)
    browser.set_handle_equiv(False)
    return browser
def brow2():
    browser2=mechanize.Browser()
    browser2.set_handle_robots(False)
    browser2.set_handle_equiv(False)
    browser2.addheaders=[('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')]
    return browser2



def brow3():
    browser3=mechanize.Browser()
    browser3.set_handle_robots(False)
    browser3.set_handle_equiv(False)
    browser3.addheaders=[('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')]
    return browser3


secondary_url='https://www.nse.co.ke/market-statistics.html?start=50'
base_url='https://www.nse.co.ke/market-statistics.html'
alt_url='https://fib.co.ke/live-markets/'
third_url='https://www.nse.co.ke/nse-25-index.html'
engine = create_engine('mysql://root:''@localhost:3306/trades14nov', echo=False)
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
url=base_url
url2=secondary_url

def play():
    browser=brow()
    result = browser.open(url)
    html=result.read()
    today = str(datetime.now().date())
    fil_name = today+"-nse_equity_stats"
    with open(fil_name+'nse_html.txt','w+') as f:
        f.write(html)


    return html
def play2():
    browser2=brow2()
    result2=browser2.open(url2)
    html2=result2.read()
    today = str(datetime.now().date())
    fil_name = today+"-nse_equity_stats"
    with open(fil_name+'nse_html2.txt','w+') as f:
        f.write(html2)
    return html2

def play3():
    browser3=brow3()
    result3=browser3.open(third_url)
    html3=result3.read()

    return html3





def load_html(fil):
    f=open(fil,'r')
    s=f.read()
    return s


def create_csv(v):
    for i,df in enumerate(pd.read_html(v,header=0)):
        df.to_csv('data9.csv'.format(i))

def in_db(fil):
    csv_data = csv.reader(file(fil))
    mydb = MySQLdb.connect(host='localhost',
        user='root',
        passwd='',
        db='trades14nov',autocommit=true)
    csv_data.to_sql(mydb,name='compans',if_exists='replace',flavor='mysql')
def o(t):
    s=string_exctractor("<table","</table>",t)
    print t
    #t=load_html("thursday.txt")

    #extractor = Extractor(t).parse()

    #extractor.write_to_csv(path='/home/k1ng/trades')

def g(t1):
    s=string_exctractor("<table","</table>",t1)
    #t=load_html("thursday.txt")
    extractor = Extractor(s).parse()
    extractor.write_to_csv(path='/home/k1ng/trades2')

#r=load_html('friday16.html')

#nse=play()
#nse2=play2()
#o(nse)
#g(nse2)
o(play3())
