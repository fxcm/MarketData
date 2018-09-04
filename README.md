# Market Data

## FXCMTickData
Enjoy free access to our historical Tick Data.

Our repository contains Tick Data from 4 January 2015. The data is compiled by trading instrument for that trading week. The files are stored in our public directory and is updated every Monday.

https://tickdata.fxcorporate.com/{instrument}/{year}/{int of week of year}.csv.gz

    Instrument: 
                  AUDCAD, AUDCHF, AUDJPY, AUDNZD, CADCHF, EURAUD,
                  EURCHF, EURGBP, EURJPY, EURUSD, GBPCHF, GBPJPY,
                  GBPNZD, GBPUSD, NZDCAD, NZDCHF, NZDJPY, NZDUSD,
                  USDCAD, USDCHF, USDJPY, AUDUSD, CADJPY, GBPCAD,
                  USDTRY, EURNZD

    Year:         2015, 2016, 2017, 2018

    Week:         1 to 52/53

To give an example, the path for extracting EURUSD data for the 1st week of 2015 would be

https://tickdata.fxcorporate.com/EURUSD/2015/1.csv.gz

If you are familiar with Python, we have two scripts that you may use for [Python 2.7](https://github.com/FXCMAPI/FXCMTickData/blob/master/TickData27.py) and [Python 3.4](https://github.com/FXCMAPI/FXCMTickData/blob/master/TickData34.py)


## Note:

o	Losses can exceed deposits

o	Past performance is not indicative of future results

o	Timestamps are in UTC

o	Data points are indicative and based on the lowest spreads available exclusively on Active Trader accounts

o	This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula/)

o	For more information, you may contact us: premiumdata@fxcm.com 

## FXCMTimeSeriesData

Enjoy free access to our historical Time Series or Candle Data.

Our repository contains Candle Data from 1 January 2012. The data is compiled by trading instrument for that trading week for m1 & H1, and trading year for D1. The files are stored in our public directory and is updated every Monday for minute (m1) and hour (H1) data only.

https://candledata.fxcorporate.com/{periodicity}/{instrument}/{year}/{int of week of year}.csv.gz

      Periodicity:  m1, H1, D1

      Instrument:   AUDCAD, AUDCHF, AUDJPY, AUDNZD, CADCHF, EURAUD,
                    EURCHF, EURGBP, EURJPY, EURUSD, GBPCHF, GBPJPY,
                    GBPNZD, GBPUSD, NZDCAD, NZDCHF, NZDJPY, NZDUSD,
                    USDCAD, USDCHF, USDJPY

      Year:         2012, 2013, 2014, 2015, 2016, 2017, 2018

      Week:         1 to 52/53 (only applicable to m1 and H1)

To give an example, the path for extracting EURUSD minute-data for the 1st week of 2012 would be

https://candledata.fxcorporate.com/m1/EURUSD/2012/1.csv.gz

To give an example, the path for extracting EURUSD hourly-data for the 1st week of 2012 would be

https://candledata.fxcorporate.com/H1/EURUSD/2012/1.csv.gz

To give an example, the path for extracting EURUSD daily-data for 2012 would be

https://candledata.fxcorporate.com/D1/EURUSD/2012.csv.gz

If you are familiar with Python, we have three scripts that you may use for [Python 2.7](https://github.com/FXCMAPI/FXCMTimeSeriesData/blob/master/CandleData27.py), [Python 3.4](https://github.com/FXCMAPI/FXCMTimeSeriesData/blob/master/CandleData34.py), or a [pandas data frame](https://github.com/FXCMAPI/FXCMTimeSeriesData/blob/master/CandleData(pandas).py)


## Note:

o	Losses can exceed deposits

o	Past performance is not indicative of future results

o	Timestamps are in UTC

o	Data points are indicative and based on the lowest spreads available exclusively on Active Trader accounts

o	Daily data is only updated yearly

o	This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula/)

o	For more information, you may contact us: premiumdata@fxcm.com 



## FXCMOrders

Enjoy a free one-month sample of our historical Orders Data.

	https://sampledata.fxcorporate.com/orders/sample.csv.gz


    Each data set would include:
            •DateTime (UTC)
            •Symbol
            •Quantity (Volume)
            •Rate (Price)


## Note:
•Losses can exceed deposits

•Past performance is not indicative of future results

•Scope of the data may vary per product	

•This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula)

•For more information, you may contact us: premiumdata@fxcm.com

 
## FXCMSentiment

Enjoy a free one-month sample of our historical Sentiment Data also known as SSI.

	https://sampledata.fxcorporate.com/sentiment/{instrument}.csv.gz

    Instrument: 
             AUDJPY, AUDUSD, CADJPY, CHFJPY, EURAUD, EURCAD, EURCHF, EURGBP,
             EURJPY, EURNOK, EURSEK, EURUSD, GBPCHF, GBPJPY, GBPUSD, NZDJPY,
             NZDUSD, USDCAD, USDCHF, USDCNH, USDJPY, USDNOK, USDSEK, FRA40,
             GER30, JPN225, SPX500, UK100, US30, USOil, XAGUSD, XAUUSD


    Each data set would include:
            •DateTime (EST)
            •Symbol
            •Name
            •Value


## Note:
•Losses can exceed deposits

•Past performance is not indicative of future results

•Scope of the data may vary per product

•This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula/)

•For more information, you may contact us: premiumdata@fxcm.com
 

## FXCMVolume

Enjoy a free one-month sample of our historical Volume Data.

	https://sampledata.fxcorporate.com/volume/{instrument}.csv.gz

    Instrument: 
             AUDJPY, AUDUSD, CADJPY, CHFJPY, EURAUD, EURCAD, EURCHF, EURGBP,
             EURJPY, EURNOK, EURSEK, EURUSD, GBPCHF, GBPJPY, GBPUSD, NZDJPY,
             NZDUSD, USDCAD, USDCHF, USDCNH, USDJPY, USDNOK, USDSEK, FRA40,
             GER30, JPN225, SPX500, UK100, US30, USOil, XAGUSD, XAUUSD


    Each data set would include:
            •DateTime (UTC)
            •Symbol
            •Name
            •Value


## Note:
•Losses can exceed deposits

•Past performance is not indicative of future results

•Scope of the data may vary per product

•This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula/)

•For more information, you may contact us: premiumdata@fxcm.com
 
 
