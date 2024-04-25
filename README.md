<div align="center">
  <img src="https://static.pepy.tech/badge/YnExchangePY"><img/>
  <img src="https://static.pepy.tech/badge/YnExchangePY/month"><img/>
  <img src="https://static.pepy.tech/badge/YnExchangePY/week"><img/>
</div><br/><br/>

# Documentation

### Description:
This Python library provides functionalities to get cryptocurrency prices and perform conversions between Iranian Toman (IRT) and USD, for 16 supported cryptocurrencies.

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
BISO<br />
TRX

# Installation
```bash
pip install YnExchangePY
```
# Functionality
The library provides functions for retrieving the price of 16 cryptocurrencies. Each function takes two arguments:<br/>
* currency (str): This argument specifies the desired currency (either "IRT" or "USD").
* grouping (bool, optional): This argument is optional (defaults to False). If set to True, the function will format the price with comma separators for readability.<br/><br/>
**Here's a list of all the available functions:**
* ```YN_Exchange.TON_PRICE(currency, grouping=False)```
* ```YN_Exchange.BTC_PRICE(currency, grouping=False)```
* ```YN_Exchange.ETH_PRICE(currency, grouping=False)```
* ```YN_Exchange.USDT_PRICE(currency, grouping=False)```
* ```YN_Exchange.SHIB_PRICE(currency, grouping=False)```
* ```YN_Exchange.BNB_PRICE(currency, grouping=False)```
* ```YN_Exchange.DOGE_PRICE(currency, grouping=False)```
* ```YN_Exchange.ADA_PRICE(currency, grouping=False)```
* ```YN_Exchange.SOL_PRICE(currency, grouping=False)```
* ```YN_Exchange.XRP_PRICE(currency, grouping=False)```
* ```YN_Exchange.USDC_PRICE(currency, grouping=False)```
* ```YN_Exchange.ETC_PRICE(currency, grouping=False)```
* ```YN_Exchange.PEPE_PRICE(currency, grouping=False)```
* ```YN_Exchange.ATM_PRICE(currency, grouping=False)```
* ```YN_Exchange.GOLD_PRICE(carat,mass)```
* ```YN_Exchange.GOLD_OUNCE_PRICE()```
* ```YN_Exchange.SILVER_OUNCE_PRICE```
* ```YN_Exchange.PLATINUM_OUNCE_PRICE```
* ```YN_Exchange.PALLADIUM_OUNCE_PRICE```
* ```YN_Exchange.USD()```
* ```YN_Exchange.EUR(currency)```
* ```YN_Exchange.AED(currency)```
* ```YN_Exchange.GBP(currency)```
* ```YN_Exchange.TRY(currency)```
# Example Usage
### Get crypto live prices:
```python
import YN_Exchange

# Get Bitcoin price in USD with comma separators
bitcoin_usd_price = YN_Exchange.BTC_PRICE("USD", grouping=True)
print(f"Bitcoin price in USD: ${bitcoin_usd_price}")

# Get Ethereum price in IRT
ethereum_irt_price = YN_Exchange.ETH_PRICE("IRT")
print(f"Ethereum price in IRT: {ethereum_irt_price}")
```
### Get gold price (Only IRT currency):
```py
import YN_Exchange

# Get 18k ct gold with gram:
18k_gold=YN_Exchange.GOLD_PRICE(carat=18,mass="gram") # You can give "kilo" parameter to mass to calculate kilograms
print(18k_gold)

# Get 24k ct gold with gram:
24k_gold=YN_Exchange.GOLD_PRICE(carat=24,mass="gram") # You can give "kilo" parameter to mass to calculate kilograms
print(24k_gold)
```
### Get price of ounce metals (Only USD currency):
```py
import YN_Exchange

# Get ounce of gold:
gold_ounce=YN_Exchange.GOLD_OUNCE_PRICE()
print(gold_ounce)

# Get ounce of sliver:
silver_ounce=YN_Exchange.SILVER_OUNCE_PRICE()
print(silver_ounce)

# Get ounce of platinum:
platinum_ounce=YN_Exchange.PLATINUM_OUNCE_PRICE()
print(platinum_ounce)

# Get ounce of palladium:
palladium_ounce=YN_Exchange.PALLADIUM_OUNCE_PRICE()
print(palladium_ounce)
```
### Get currency prices:
```py
import YN_Exchange

# Get USD(united state dollar) price (Only IRT):
usd_price=YN_Exchange.USD()
print(usd_prices)

# Get EUR(europe euro) price:
eur_price=YN_Exchange.EUR(currency="USD") # You can use "IRT" parameter instead of "USD" parameter
print(eur_price)

# Get AED(arab emirates dirham) price:
aed_price=YN_Exchange.aed(currency="USD") # You can use "IRT" parameter instead of "USD" parameter
print(aed_price)

# Get GBP(great britain pound) price:
gbp_price=YN_Exchange.GBP(currency="USD") # You can use "IRT" parameter instead of "USD" parameter
print(gbp_price)

# Get TRY(turkish lira) price:
try_price=YN_Exchange.TRY(currency="USD) # You can use "IRT" parameter instead of "USD" parameter
```
# Error Handling
If the function encounters an error, such as an invalid currency or a network issue, it will raise a ```ValueError``` exception. You can handle this exception using a try-except block.
# Limitations
* The library relies on scraping data from a website, which may be subject to changes or become unavailable.
* The library only supports a limited number of cryptocurrencies (currently 16).
# Additional notes
### Here are some ways you can contribute to the YN_Exchange project:
* **Donate:** If you've found my library to be useful, I would greatly appreciate it if you would consider making a donation. Your donation will help me to continue to develop and maintain the library, and to add new features in the future.

**Donate function**
```python
yn_exchange.donate()
```
