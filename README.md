<div align="center">
  <img src="https://static.pepy.tech/badge/YnExchangePY"><img/>
  <img src="https://static.pepy.tech/badge/YnExchangePY/month"><img/>
  <img src="https://static.pepy.tech/badge/YnExchangePY/week"><img/>
</div><br/><br/>

# Documentation

### Description:
This Python library provides functionalities to get cryptocurrency prices and perform conversions between Iranian Toman (IRT) and USD, for all supported cryptocurrencies.

### Key Features:
* Get the current price of various cryptocurrencies in IRT or USD.
* Convert between IRT and USD for any of the supported cryptocurrencies.
* Get country currencies price
* Get chart of crypto prices
* Donate to the library developer (optional).

# Installation
```bash
pip install YnExchangePY
```
# Functionality
The library provides functions for retrieving the price of all cryptocurrencies. Each function takes 3 arguments:<br/>
* currency (str): This argument specifies the desired currency (either "IRT" or "USD").
* grouping (bool, optional): This argument is optional (defaults to False). If set to True, the function will format the price with comma separators for readability.
* crypto_name (str) : This argument is for the name of the desired crypto to get its price<br/><br/>
**Here's a list of all the available functions:**
* ```YN_Exchange.CRYPTO_PRICES(crypto_name : str,currency:str,grouping : bool = False)```
* ```YN_Exchange.GOLD_PRICE(carat : int,mass : str="gram")```
* ```YN_Exchange.CURRENCY_PRICE(currency : str,price_currency : str = "IRT")```
* ```YN_Exchange.USD_PRICE()```
* ```YN_Exchange.CRYPTO_CHART(crypto : str,timeout : int=5,currency : str="usdt")```
* ```YN_Exchange.calculator(value:float,currency:str,crypto:str,grouping : bool=False)```
* ```YN_Exchange.DONATE()```

# Example Usage
### Get crypto live prices:
```python
import YN_Exchange

# Get Bitcoin price in USD with grouping
bitcoin_usd_price = YN_Exchange.CRYPTO_PRICES(crypto_name="BTC",currency="USD",grouping=True)
print(f"Bitcoin price in USD: ${bitcoin_usd_price}")

# Get Ethereum price in IRT(no grouping)
ethereum_irt_price = YN_Exchange.CRYPTO_PRICES(crypto_name="ETH",currency="IRT")
print(f"Ethereum price in IRT: {ethereum_irt_price}")
```
### Get gold price (Only IRT currency):
```py
import YN_Exchange

# Get 18k ct gold with gram:
_18k_gold=YN_Exchange.GOLD_PRICE(carat=18,mass="gram") # You can give "kilo" parameter to mass to calculate kilograms
print(_18k_gold)

# Get 24k ct gold with gram:
_24k_gold=YN_Exchange.GOLD_PRICE(carat=24,mass="gram") # You can give "kilo" parameter to mass to calculate kilograms
print(_24k_gold)
```
### Get price of ounce metals (Only USD currency):
This method is being updated
### Get currency prices:
```py
import YN_Exchange

# Get USD(united state dollar) price (Only IRT):
usd_price=YN_Exchange.USD_PRICE()
print(usd_prices)

# Get EUR(europe euro) price:
eur_price=YN_Exchange.CURRENCY_PRICE(currency="EUR",price_currency="USD") # You can use "IRT" parameter instead of "USD" parameter
print(eur_price)
```
The USD function is separated from the main function due to differences
### Get chart of crypto prices:
```py
import YN_Exchange

#Get bitcoin price chart
YN_Exchange.CRYPTO_CHART(crypto="BTC,timeout=7,currency="USDT") # USDT currency : USD
```
* After executing this method, a file named "{your crypto} chart.png" will be created.
* Some cryptocurrencies do not have a table with USD currency, so you have to use IRT currency.
* If there is a problem in displaying the table, it will be displayed in the photo.
* The "timeout" argument is the amount of time the page takes to load.
* If you have a weak internet, set the "timeout" argument to a number above 7

# Error Handling
If the function encounters an error, such as an invalid currency or a network issue, it will raise a ```ValueError``` exception. You can handle this exception using a try-except block.
# Limitations
* The library relies on scraping data from a website, which may be subject to changes or become unavailable.
* The library only supports a limited number of cryptocurrencies.
# Additional notes
### Here are some ways you can contribute to the YN_Exchange project:
* **Donate:** If you've found my library to be useful, I would greatly appreciate it if you would consider making a donation. Your donation will help me to continue to develop and maintain the library, and to add new features in the future.

**Donate function**
```python
YN_Exchange.DONATE()
```
