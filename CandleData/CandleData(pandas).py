# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 08:11:38 2018

@author: fxcm
"""
import datetime
import pandas as pd


url = 'https://candledata.fxcorporate.com/'##This is the base url
periodicity='m1' ##periodicity, can be m1, H1, D1
url_suffix = '.csv.gz' ##Extension of the file name
symbol = 'EURUSD' ##symbol we want to get tick data for
##Available Currencies 
##AUDCAD,AUDCHF,AUDJPY, AUDNZD,CADCHF,EURAUD,EURCHF,EURGBP
##EURJPY,EURUSD,GBPCHF,GBPJPY,GBPNZD,GBPUSD,GBPCHF,GBPJPY
##GBPNZD,NZDCAD,NZDCHF.NZDJPY,NZDUSD,USDCAD,USDCHF,USDJPY


##The candle files are stored in compressed csv.  The storage structure comes as {periodicity}/{symbol}/{year}/{week_of_year}.csv.gz
##The first week of the year will be 1.csv.gz where the 
##last week might be 52 or 53.  That will depend on the year.
##Once we have the week of the year we will be able to pull the correct file with the data that is needed.
start_dt =  datetime.date(2017,7,5)##random start date
end_dt = datetime.date(2017,12,16)##random end date


start_wk = start_dt.isocalendar()[1]##find the week of the year for the start  
end_wk = end_dt.isocalendar()[1] ##find the week of the year for the end 
year = str(start_dt.isocalendar()[0]) ##pull out the year of the start

###The URL is a combination of the currency, periodicity,  year, and week of the year.
###Example URL https://candledata.fxcorporate.com/m1/EURUSD/2017/29.csv.gz
###The example URL should be the first URL of this example
data=pd.DataFrame()
##This will loop through the weeks needed, create the correct URL and print out the lenght of the file.
for i in range(start_wk, end_wk ):
    url_data = url + periodicity + '/' + symbol + '/' + year + '/' + str(i) + url_suffix
    print(url_data)
    tempdata = pd.read_csv(url_data, compression='gzip')
    data=pd.concat([data, tempdata])
print(data)