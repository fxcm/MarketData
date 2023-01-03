# FXCMTickData
Enjoy free access to our historical Tick Data.

Our repository contains Tick Data from January 2019. The data is compiled by trading instrument for that trading week. The files are stored in our public directory and is updated monthly.

https://tickdata.fxcorporate.com/{instrument}/{year}/{int of week of year}.csv.gz

    Instrument: 
                  AUDCAD, AUDCHF, AUDJPY, AUDNZD, CADCHF, EURAUD,
                  EURCHF, EURGBP, EURJPY, EURUSD, GBPCHF, GBPJPY,
                  GBPNZD, GBPUSD, NZDCAD, NZDCHF, NZDJPY, NZDUSD,
                  USDCAD, USDCHF, USDJPY, AUDUSD, CADJPY, GBPCAD,
                  USDTRY, EURNZD, GBPAUD

    Year:         2019, 2020, 2021, 2022, 2023

    Week:         1 to 52/53

To give an example, the path for extracting EURUSD data for the 1st week of 2022 would be

https://tickdata.fxcorporate.com/EURUSD/2022/1.csv.gz

If you are familiar with Python, we have two scripts that you may use for [Python 2.7](https://github.com/fxcm/MarketData/blob/master/TickData/TickData27.py) and [Python 3.4](https://github.com/fxcm/MarketData/blob/master/TickData/TickData34.py)


## Note:

o	Losses can exceed deposits

o	Past performance is not indicative of future results

o	Timestamps are in UTC

o	Data points are indicative and based on the lowest spreads available exclusively on Active Trader accounts

o	This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula/)

o	For more information, you may contact us: api@fxcm.com 

