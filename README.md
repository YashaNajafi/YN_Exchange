# YN Exchange
<br>
<div align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue">
  <img src="https://static.pepy.tech/badge/YnExchangePY">
  <img src="https://static.pepy.tech/badge/YnExchangePY/month">
  <img src="https://static.pepy.tech/badge/YnExchangePY/week">
  <img src="https://img.shields.io/badge/Python-_3.10_%7C_3.11_%7C_3.12_%7C_3.13-yellow">
</div>

# Documentation

### <a href="https://yashanajafi.github.io/YN_Exchange/">Direct Documentation ( Only PC ) Website</a>

### Description:
This Python library provides functionalities to get cryptoCurrency prices and perform conversions between Iranian Toman (IRT) and USD, for all supported cryptocurrencies.

### Key Features:
* Real-time cryptoCurrency price data retrieval .
* Support for multiple exchanges .
* Perform conversions between USD, IRT, and supported cryptocurrencies.
* Get the current price of metals ( Gold , Copper , Silver and ... ) .
* Get the current price of natural resources ( oil , gas and ... ) .
* Generate cryptoCurrency tables (requires `kaleido` library for table rendering).
* Asynchronous data fetching .
* Customizable data formats .
* Save data to cache .
* Smart calculator

<hr>

### Installation:
- Install the library using pip:
```bash
pip install YnExchangePY
```

### Dependencies
- Required: `kaleido` library for generating crypto tables ( Images )
```bash
pip install kaleido
```

<hr>

# Usage ( Normal Version )

## Crypto Section :

- <b> Get Crypto Price : </b>

```python
# Import to your project :
from YN_Exchange import Exchange

# "Cache" Argument It is set to "False" by default
# "Cache_Duration" it is set to per second
ExchangeOBJ = Exchange.CryptoManager(Cache = True , Cache_Duration = 300) # Make object of CryptoManager

# "Currency" Argument supported Currency is : USD , IRT ( Default : USD )
# "Grouping" It is set to "False" by default
# Grouping ( False ) Output : 96000
# Grouping ( True ) Output : 96,000
BTC_Price = ExchangeOBJ.GetCryptoPrice(CryptoName = "BTC",Currency = "USD",Grouping = True) # Get crypto price
```

<b> If the Cache is active, the information is received and displayed from the Cache until the Cache_Duration expires, and after the Cache expires, the information is received from the server again and stored in the Cache. </b>

<hr>

- <b>Generate Crypto Charts :</b>

### Examples ( Demo ) :

<img src="https://s8.uupload.ir/files/ton-usdt_chart_f0oo.jpg" width="300px"> <img src="https://s8.uupload.ir/files/ton-usdt_chart_7aod.jpg" width="500px">

<hr>

### Example usage :

```python
# Import to your project :
from YN_Exchange import Exchange

# "Cache" Argument It is set to "False" by default
# "Cache_Duration" it is set to per second
# Cache not active for charts
ExchangeOBJ = Exchange.CryptoManager(Cache = True , Cache_Duration = 300) # Make object of CryptoManager

# Generate chart
# For save chart as image definitely install kaleido
# You can edit argument for edit your chart for example, if you set the histogram argument to "False", the histograms will be removed from the chart.
ExchangeOBJ.GenerateCryptoChart(CryptoSymbol = "TON/USDT)
```

<b>You can edit argument for edit your chart for example, if you set the histogram argument to "False", the histograms will be removed from the chart.<b>
<br>
<b> For save chart as image definitely install kaleido ( [Click](#installation) ) </b>

### Charts Argument :
- ```ImageSave : bool = True```
- ```HTML_Save : bool = False```
- ```Json_Save : bool = False```
- ```ChartTemplate : str = "Professional"```
- ```Exchange : str = "binance"```
- ```CryptoSymbol : str = "BTC/USDT"```
- ```Limit : int = 100```
- ```Timeframe = '1d'```
- ```IchimokuLine : bool = True```
- ```IchimokuCloud : bool = True```
- ```Candlesticks : bool = True```
- ```Chikou : bool = True```
- ```Tenkan : bool = True```
- ```Kijun : bool = True```
- ```MACD_Line : bool = True```
- ```SignalLine : bool = True```
- ```Histogram : bool = True```

<b>You can customize your charts with arguments</b>

<hr>

## Metal Section :
- <b> Get Price : </b>
```python
# Import to your project :
from YN_Exchange import Exchange

# "Cache" Argument It is set to "False" by default
# "Cache_Duration" it is set to per second
MetalsOBJ = Exchange.MetalManager(Cache = True , Cache_Duration = 300) # Make object of MetalManager

GoldPrice = MetalsOBJ.GetGoldPrice(Carat=24,Grouping=True)
```
<b>You will see the rest of the functions of this class</b>
<br>

### Functionality :
- ```GetPlatinumPrice(Grouping : bool = "False")``` Ounce per USD
- ```GetSilverPrice(Grouping : bool = "False")``` Ounce per USD
- ```GetPalladiumPrice(Grouping : bool = "False")``` Ounce per USD
- ```GetTinPrice(Grouping : bool = "False")``` Tonne per USD
- ```GetZincPrice(Grouping : bool = "False")``` Tonne per USD
- ```GetNickelPrice(Grouping : bool = "False")``` Tonne per USD
- ```GetLeadPrice(Grouping : bool = "False")``` Tonne per USD
- ```GetCopperPrice(Grouping : bool = "False")``` Pound per USD
- ```GetAluminiumPrice(Grouping : bool = "False")``` Tonne per USD
- ```GetGoldPrice(Grouping : bool = "False",carat : int = 18,weight : str = "gram")``` Weight : [kilo,gram,ounce] and Only IRT Price

<hr>

## Natural Resources Section :
- <b> Get Price : </b>
```python
# Import to your project :
from YN_Exchange import Exchange

# "Cache" Argument It is set to "False" by default
# "Cache_Duration" it is set to per second
NaturalOBJ = Exchange.NaturalResourcesManager(Cache = True , Cache_Duration = 300) # Make object of NaturalResourcesManager

BrentOil = NaturalOBJ.GetBrentOil(Grouping = True)
OilWTI = NaturalOBJ.GetCrudeOilWTI(Grouping = True)
NaturalGas = NaturalOBJ.GetNaturalGas(Grouping = True)
```

### Functionality :
- ```GetCrudeOilWTI``` Barrel per USD
- ```GetBrentOil``` Barrel per USD
- ```GetNaturalGas``` Mmbtu per USD

<hr>

## Calculator Section :
<b>You can use this functions in ```Calculator()``` class<b>
<br>
- <b>Example usage code : </b>
```python
# Import to your project :
from YN_Exchange import Exchange

CalculatorOBJ = Exchange.Calculator() # Make object of Calculator

Result = CalculatorOBJ.CryptoValue2Currency(CryptoName="BTC",Currency="USD",Grouping = True)
```


### Functionality :
- ```CryptoValue2Currency(Value: int, CryptoName: str = "BTC", Currency: str = "USD", Grouping: bool = False)```
- ```Currency2CryptoValue(Value: int, CryptoName: str = "BTC", Currency: str = "USD", Grouping: bool = False)```
- ```CryptoValue2CryptoValue(CryptoValue: int, CryptoName1: str = "BTC", CryptoName2: str = "ETH", Grouping: bool = False)```
- ```CryptoValue2GoldWeight(GoldCarat: int = 18, GoldWeight: str = "gram", CryptoName: str = "BTC")```
- ```GoldWeight2CryptoValue(GoldCarat: int = 18, GoldWeight: str = "gram", GoldValue: int = 1, CryptoName: str = "BTC")```
- ```GoldWeight2Currency(GoldCarat: int = 18, GoldWeight: str = "gram", GoldValue: int = 1, Currency: str = "USD")```
- ```Currency2GoldWeight(GoldCarat: int = 18, GoldWeight: str = "gram", CurrencyValue : int = 5000000)```


<hr>

## Exchanges API Section :

<b>A class to receive digital currency information from APIs of world's most prestigious exchanges</b>
<br>
- <b> Example usage code : </b>
```python
# Import to your project :
from YN_Exchange import Exchange

ExchangeOBJ = Exchange.ExchangeAPI(Exchange = "binance") # Make object of ExchangeAPI

BTC = ExchangeOBJ.GetCryptoData(CryptoSymbol = "BTC/USDT")
```
- <b>Output</b>
```json
{'symbol': 'BTC/USDT', 'timestamp': 1736598300337, 'datetime': '2025-01-11T12:25:00.337Z', 'high': 95836.0, 'low': 92206.02, 'bid': 94613.99, 'bidVolume': 5.67459, 'ask': 94614.0, 'askVolume': 0.35323, 'vwap': 94125.84165815, 'open': 94805.6, 'close': 94614.0, 'last': 94614.0, 'previousClose': 94805.6, 'change': -191.6, 'percentage': -0.202, 'average': 94709.8, 'baseVolume': 25125.20063, 'quoteVolume': 2364930656.128506, 'markPrice': None, 'indexPrice': None, 'info': {'symbol': 'BTCUSDT', 'priceChange': '-191.60000000', 'priceChangePercent': '-0.202', 'weightedAvgPrice': '94125.84165815', 'prevClosePrice': '94805.60000000', 'lastPrice': '94614.00000000', 'lastQty': '0.03192000', 'bidPrice': '94613.99000000', 'bidQty': '5.67459000', 'askPrice': '94614.00000000', 'askQty': '0.35323000', 'openPrice': '94805.60000000', 'highPrice': '95836.00000000', 'lowPrice': '92206.02000000', 'volume': '25125.20063000', 'quoteVolume': '2364930656.12850630', 'openTime': '1736511900337', 'closeTime': '1736598300337', 'firstId': '4392795366', 'lastId': '4396948127', 'count': '4152762'}}
```
<hr>

## Cache Section :
<b>All the classes in the library have the "clear_cache" function, which you can use to clear the cache of that class.</b>
<br>
<b>Caches are saved as json files on your computer</b>

<hr>

# Usage ( Async Version ) :
<b>For usage Async version you must import</b> ```AsyncExchange``` <b>module</b>
<br>
<b>And for usage you can use</b> ```asyncio.run()``` <b>function</b>
<br>

- <b>Example Usage :</b>
```python
# Import to your project :
from YN_Exchange import AsyncExchange
import asyncio

# The use of all async functions is the same as the main functions :
ExchangeOBJ = AsyncExchange.AsyncCryptoManager(Cache = True , Cache_Duration = 300)

CryptoPrice = asyncio.run(ExchangeOBJ.GetCryptoPrice(CryptoName = "BTC",Currency = "USD",Grouping = True))
```
<br>

<b>To use functions, you can easily use them by adding the word "async" to the first of the main functions.</b>

<hr>

# Donation
- <b>TON , USDT Wallet ( Tonkeeper ) : </b> <br>
``` UQCZgyJ4XB7c1GMnLgefqcc-zOA98hyOlMLZpO0EsCNxBq-e ```
- <b>BTC Wallet : </b> <br>
``` bc1qpgzy8hpklpp0zwan5ha4lfzavvtjf286w0tlzc ```
- <b>ETH Wallet : </b> <br>
```0xE95FAEc8B847F18B3bC5dc1bB8256fb376d2e459```
- <b>TRX Wallet : </b> <br>
```TG8MpYtysGngjK7tPdCATLqLJKwm5vbfYi```
