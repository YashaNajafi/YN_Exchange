<div align="center">
  <img src="https://static.pepy.tech/badge/YnExchangePY"><img/>
  <img src="https://static.pepy.tech/badge/YnExchangePY/month"><img/>
  <img src="https://static.pepy.tech/badge/YnExchangePY/week"><img/>
</div><br/><br/>

# Documentation

### Description:
This Python library provides functionalities to get cryptocurrency prices and perform conversions between Iranian Toman (IRT) and USD, for 15 supported cryptocurrencies.

### Key Features:
* Get the current price of various cryptocurrencies in IRT or USD.
* Convert between IRT and USD for any of the supported cryptocurrencies.
* Donate to the library developer (optional).

### Supported Cryptocurrencies:<br />
TON<br />
BTC<br />
ETH<br />
USDT<br />
SHIB<br />
BNB<br />
DOGE<br />
ADA<br />
SOL<br />
XRP<br />
USDC<br />
ETC<br />
PEPE<br />
ATM<br />
BISO

# Installation
```bash
pip install YnExchangePY
```
# Functionality
The library provides functions for retrieving the price of 15 cryptocurrencies. Each function takes two arguments:<br/>
* currency (str): This argument specifies the desired currency (either "IRT" or "USD").
* grouping (bool, optional): This argument is optional (defaults to False). If set to True, the function will format the price with comma separators for readability.<br/><br/>
**Here's a list of all the available functions:**
* ```yn_exchange.TON_PRICE(currency, grouping=False)```
* ```yn_exchange.BTC_PRICE(currency, grouping=False)```
* ```yn_exchange.ETH_PRICE(currency, grouping=False)```
* ```yn_exchange.USDT_PRICE(currency, grouping=False)```
* ```yn_exchange.SHIB_PRICE(currency, grouping=False)```
* ```yn_exchange.BNB_PRICE(currency, grouping=False)```
* ```yn_exchange.DOGE_PRICE(currency, grouping=False)```
* ```yn_exchange.ADA_PRICE(currency, grouping=False)```
* ```yn_exchange.SOL_PRICE(currency, grouping=False)```
* ```yn_exchange.XRP_PRICE(currency, grouping=False)```
* ```yn_exchange.USDC_PRICE(currency, grouping=False)```
* ```yn_exchange.ETC_PRICE(currency, grouping=False)```
* ```yn_exchange.PEPE_PRICE(currency, grouping=False)```
* ```yn_exchange.ATM_PRICE(currency, grouping=False)```
# Example Usage
```python
from YN_Exchange import yn_exchange

# Get Bitcoin price in USD with comma separators
bitcoin_usd_price = yn_exchange.BTC_PRICE("USD", grouping=True)
print(f"Bitcoin price in USD: ${bitcoin_usd_price}")

# Get Ethereum price in IRT
ethereum_irt_price = yn_exchange.ETH_PRICE("IRT")
print(f"Ethereum price in IRT: {ethereum_irt_price}")
```
# Error Handling
If the function encounters an error, such as an invalid currency or a network issue, it will raise a ```ValueError``` exception. You can handle this exception using a try-except block.
# Limitations
* The library relies on scraping data from a website, which may be subject to changes or become unavailable.
* The library only supports a limited number of cryptocurrencies (currently 15).
# Additional notes
### Here are some ways you can contribute to the YN_Exchange project:
* **Donate:** If you've found my library to be useful, I would greatly appreciate it if you would consider making a donation. Your donation will help me to continue to develop and maintain the library, and to add new features in the future.

**Donate function**
```python
yn_exchange.donate()
```
