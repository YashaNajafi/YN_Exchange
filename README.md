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

# Usage

* Importing the library:
```py
from YN_Exchange import yn_exchange
```

* Getting the price of a cryptocurrency:<br />
**IRT** : **Iranian Toman**<br />
**USD** : **United States Doller**

```py
ton_price_irt = yn_exchange.TON_COIN_PRICE(currency="IRT")
ton_price_usd = yn_exchange.TON_COIN_PRICE(currency="USD")

print(f"1 TON = {ton_price_irt} IRT")
print(f"1 TON = ${ton_price_usd} USD")
```

* Converting between IRT and USD:
```py
irt_to_usd = yn_exchange.calculator(100000, "IRT", "BTC")
usd_to_irt = yn_exchange.calculator(10, "USD", "ETH")

print(f"100,000 IRT = ${irt_to_usd} USD")
print(f"$10 USD = {usd_to_irt} IRT")
```

* Donating to the library developer (optional):
```py
yn_exchange.donate()
```

# Functions

```py
TON_COIN_PRICE()
BTC_PRICE()
ETH_PRICE()
USDT_PRICE()
SHIB_PRICE()
BNB_PRICE()
DOGE_PRICE()
ADA_PRICE()
SOL_PRICE()
XRP_PRICE()
USDC_PRICE()
ETC_PRICE()
PEPE_PRICE()
ATM_PRICE()
BISO_PRICE()
donate()
calculator()
```
