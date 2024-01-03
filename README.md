# Introduction
FXCM provide several sample data for free. Historical candle data. Order flow, sentiment and volume.

## TickData
Please take a look at our Tick Data Downloader [FXCM apps](https://www.fxcm.com/markets/trading-tools/trading-apps/).

### Note:

o	Past performance is not indicative of future results

o	Timestamps are in UTC

o	Data points are indicative and based on the lowest spreads available exclusively on Active Trader accounts

o	This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula/)

o	For more information, you may contact us: api@fxcm.com 

## CandleData

Historical Time Series or Candle Data sample.

https://candledata.fxcorporate.com/{periodicity}/{instrument}/{year}/{int of week of year}.csv.gz

      Periodicity:  m1, H1, D1

      Instrument:   AUDCAD, AUDCHF, AUDJPY, AUDNZD, CADCHF, EURAUD,
                    EURCHF, EURGBP, EURJPY, EURUSD, GBPCHF, GBPJPY,
                    GBPNZD, GBPUSD, NZDCAD, NZDCHF, NZDJPY, NZDUSD,
                    USDCAD, USDCHF, USDJPY

      Year:         2017, 2018, 2019, 2020

      Week:         1 to 52/53 (only applicable to m1 and H1)

To give an example, the path for extracting EURUSD minute-data for the 1st week of 2020 would be

https://candledata.fxcorporate.com/m1/EURUSD/2020/1.csv.gz

To give an example, the path for extracting EURUSD hourly-data for the 1st week of 2020 would be

https://candledata.fxcorporate.com/H1/EURUSD/2020/1.csv.gz

To give an example, the path for extracting EURUSD daily-data for 2020 would be

https://candledata.fxcorporate.com/D1/EURUSD/2020.csv.gz

If you are familiar with Python, we have three scripts that you may use for [Python 2.7](https://github.com/fxcm/MarketData/blob/master/CandleData/CandleData27.py), [Python 3.4](https://github.com/fxcm/MarketData/blob/master/CandleData/CandleData34.py), or a [pandas data frame](https://github.com/fxcm/MarketData/blob/master/CandleData/CandleData(pandas).py)

Please use our FXCM [apps](https://www.fxcm.com/markets/trading-tools/trading-apps/) if you want the full data.

### Note:

o	Past performance is not indicative of future results

o	Timestamps are in UTC

o	Data points are indicative and based on the lowest spreads available exclusively on Active Trader accounts

o	Daily data is only updated yearly

o	This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula/)

o	For more information, you may contact us: api@fxcm.com 



## Order Flow

Enjoy a free one-month sample of our historical Orders Data.

	https://sampledata.fxcorporate.com/orders/sample.csv.gz


    Each data set would include:
            •DateTime (UTC)
            •Symbol
            •Quantity (Volume)
            •Rate (Price)


### Note:

o	Past performance is not indicative of future results

o	Scope of the data may vary per product	

o	This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula)

o	For more information, you may contact us: api@fxcm.com

 
## Sentiment

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


### Note:
o	Past performance is not indicative of future results

o	Scope of the data may vary per product

o	This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula/)

o	For more information, you may contact us: api@fxcm.com
 

## Volume

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


### Note:

o	Past performance is not indicative of future results

o	Scope of the data may vary per product

o	This is for personal use and abides by our [EULA](https://www.fxcm.com/uk/forms/eula/)

o	For more information, you may contact us: api@fxcm.com

## Disclaimer:

High Risk Investment Notice: 
 
The FXCM Group is a holding company of Forex Capital Markets Limited (FXCM LTD), FXCM EU LTD (FXCM EU), FXCM Australia Pty. Limited (FXCM AU), FXCM South Africa (PTY) Ltd (FXCM ZA), FXCM Markets Limited (FXCM Markets), and all affiliates of aforementioned firms, or other firms under the FXCM Group of companies [collectively “FXCM”]. The FXCM Group is headquartered at 20 Gresham Street, 4th Floor, London EC2V 7JE, United Kingdom. Read and understand the Terms and Conditions on the FXCM Group’s websites prior to taking further action.

FXCM LTD: CFDs are complex instruments and come with a high risk of losing money rapidly due to leverage. 69% of retail investor accounts lose money when trading CFDs with this provider. You should consider whether you understand how CFDs work and whether you can afford to take the high risk of losing your money. FXCM LTD is authorised and regulated in the UK by the Financial Conduct Authority. Registration number 217689. Registered in England and Wales with Companies House company number 04072877.

FXCM EU: CFDs are complex instruments and come with a high risk of losing money rapidly due to leverage. 77% of retail investor accounts lose money when trading CFDs with this provider. You should consider whether you understand how CFDs work and whether you can afford to take the high risk of losing your money. FXCM EU is a Cyprus Investment Firm (“CIF”) registered with the Cyprus Department of Registrar of Companies (HE 405643) and authorised and regulated by the Cyprus Securities and Exchange Commission (“CySEC”) under license number 392/20.

FXCM AU: By trading, you could sustain a total loss of your deposited funds. The products may not be suitable for all investors. Please ensure that you fully understand the risks involved. If you decide to trade products offered by FXCM AU, you must read and understand the Financial Services Guide, Product Disclosure Statement, and Terms of Business. FXCM AU is regulated by the Australian Securities and Investments Commission, AFSL 309763. FXCM AU ACN: 121934432. The information provided by FXCM AU is intended for residents of Australia and is not directed at any person in any country or jurisdiction where such distribution or use would be contrary to local law or regulation. Please read the full Terms and Conditions.

FXCM Markets: Losses can exceed deposited funds. FXCM Markets is incorporated in Bermuda as an operating subsidiary within the FXCM group and is not required to hold any financial services license or authorisation in Bermuda to offer its products and services.

Past Performance: Past Performance is not an indicator of future results.
