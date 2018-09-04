
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 15:46:59 2016

@author: fxcm
"""
##from StringIO import StringIO
from io import BytesIO
import gzip
import urllib
import datetime 


url = 'https://tickdata.fxcorporate.com/'##This is the base url 
url_suffix = '.csv.gz' ##Extension of the file name
symbol = 'EURUSD' ##symbol we want to get tick data for
##Available Currencies 
##AUDCAD,AUDCHF,AUDJPY, AUDNZD,CADCHF,EURAUD,EURCHF,EURGBP
##EURJPY,EURUSD,GBPCHF,GBPJPY,GBPNZD,GBPUSD,GBPCHF,GBPJPY
##GBPNZD,NZDCAD,NZDCHF.NZDJPY,NZDUSD,USDCAD,USDCHF,USDJPY


##The tick files are stored a compressed csv.  The storage structure comes as {symbol}/{year}/{week_of_year}.csv.gz  
##The first week of the year will be 1.csv.gz where the 
##last week might be 52 or 53.  That will depend on the year.
##Once we have the week of the year we will be able to pull the correct file with the data that is needed.
start_dt =  datetime.date(2015,7,16)##random start date
end_dt = datetime.date(2015,8,16)##random end date 


start_wk = start_dt.isocalendar()[1]##find the week of the year for the start  
end_wk = end_dt.isocalendar()[1] ##find the week of the year for the end 
year = str(start_dt.isocalendar()[0]) ##pull out the year of the start

###The URL is a combination of the currency, year, and week of the year.
###Example URL https://tickdata.fxcorporate.com/EURUSD/2015/29.csv.gz
###The example URL should be the first URL of this example

##This will loop through the weeks needed, create the correct URL and print out the lenght of the file.
for i in range(start_wk, end_wk ):
    url_data = url + symbol+'/'+year+'/'+str(i)+url_suffix
    print(url_data)
    requests = urllib.request.urlopen(url_data)
    buf = BytesIO(requests.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
    print(len(data))