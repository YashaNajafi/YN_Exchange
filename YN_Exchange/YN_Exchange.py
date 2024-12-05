#----------------<info>-----------
# Developed by : Yasha Najafi
# Developer github : https://github.com/YashaNajafi
# Developer info page : https://YashaNajafi.github.io/about_me
# Module version : 5.0.2
# Module name : YN_EXCHANGE
# Number of supported crypto : ***
# References : https://ok-ex.io/ | https://www.tgju.org/ | https://www.xe.com/

#----------------<libs>----------
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
#----------------<functions>----------
    #-------------------<grouping>--------
def SEPARATION_OF_NUMBERS(number):
   return f"{number:,}"
#----------<crypto>-----------
def CRYPTO_PRICES(crypto_name : str,currency:str,grouping : bool = False):
    url = f"https://ok-ex.io/buy-and-sell/{crypto_name.upper()}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    irt_price = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg").text
    usd_price = soup.find("div", class_="text-neutral-400 lg:text-2xl text-lg leading-8 whitespace-nowrap mt-0 lg:mt-2 ml-4 lg:ml-5 ltr").text
    irt_price=irt_price.replace(",","")
    irt_price=irt_price.replace("\n","")
    usd_price=usd_price.replace("$ ","")
    usd_price=usd_price.replace("\n","")
    usd_price=usd_price.replace(",","")
    if currency == "IRT":
        price = irt_price
    elif currency == "USD":
        price = usd_price
    else:
        raise ValueError("Invalid currency entered!")
    if grouping:
        return SEPARATION_OF_NUMBERS(float(price))
    else:
        return float(price)
#----------<gold>------------
def GOLD_PRICE(carat : int,mass : str="gram",grouping : bool = False):
    _18k_url="https://www.tgju.org/profile/geram18"
    _24k_url="https://www.tgju.org/profile/geram24"

    if carat == 18:
        response = requests.get(_18k_url)
    elif carat==24:
        response = requests.get(_24k_url)
    else:
        raise ValueError(f"Carat does not have a value with the name <{carat}>")

    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.find("span", {'data-col': 'info.last_trade.PDrCotVal'})
    gold_price=element.text
    gold_price=gold_price.replace(",","")
    gold_price=float(gold_price)
    gold_price=gold_price//10

    if mass=="gram":
        if grouping:
            return SEPARATION_OF_NUMBERS(gold_price)
        return gold_price
    elif mass=="kilo":
        if grouping:
            return SEPARATION_OF_NUMBERS(gold_price*1000)
        return gold_price*1000
    else:
        raise ValueError(f"Mass does not have a value with the name <{mass}>")
#---------<currency>----------
def CURRENCY_PRICE(currency : str,price_currency : str = "IRT"):
    irt_url = f"https://www.tgju.org/profile/price_{currency.lower()}"
    usd_url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={currency.upper()}&To=USD"

    irt_response = requests.get(irt_url)
    irt_soup = BeautifulSoup(irt_response.content, "html.parser")
    irt_price = irt_soup.find("span", {'data-col': 'info.last_trade.PDrCotVal'})

    usd_response = requests.get(usd_url)
    usd_soup = BeautifulSoup(usd_response.content, "html.parser")
    usd_price = usd_soup.find("p", {'class': 'sc-1c293993-1 fxoXHw'})

    if price_currency == "IRT":
        price=irt_price.text
        if "," in price:
            price=price.replace(",","")
        price=int(price)
        price=price//10
    elif price_currency == "USD":
        price=usd_price.text
        price=price.replace(" US Dollars","")
        price=float(price)
    else:
        raise ValueError(f"Currency does not have a value with the name <{price_currency}>")

    return price

def USD_PRICE():        #this function only for irt price
    url = "https://www.tgju.org/profile/price_dollar_rl"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.find("span", {'data-col': 'info.last_trade.PDrCotVal'})
    usd_price=element.text
    if usd_price == "-":
        return "Oops ! USD Price not updated,please try agian."
    if "," in usd_price:
        usd_price=usd_price.replace(",","")
    usd_price=float(usd_price)
    usd_price=usd_price//10
    return usd_price
#------------<chart>----------
def CRYPTO_CHART(crypto : str,timeout : int=5,currency : str="usd"):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    if currency=="usd" or "USD": currency="usdt"
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://ok-ex.io/trade/chart/{currency.lower()}?coin={crypto.lower()}&prov=2&interval&hasVolume=false&isFullScreen=true&fullscreenButton=false")
    time.sleep(timeout)
    driver.save_screenshot(f"{crypto.upper()} Chart.png")
    driver.quit()
    os.system("cls")
    print("SAVED!")
#--------<calculators>--------
def CALCULATOR(value:float,currency:str,crypto:str,grouping : bool=False,calculat_mode : str = "CV2C",other_crypto : str = None):
    if calculat_mode=="CryptoValue2Currency" or calculat_mode=="CV2C":
        response = value*CRYPTO_PRICES(crypto_name=crypto,currency=currency)
    elif calculat_mode=="CryptoValue2OtherCrypto" or calculat_mode=="CV2OC" and other_crypto==None:
        raise ValueError("Please enter other_crypto!")
    elif calculat_mode=="CryptoValue2OtherCrypto" or calculat_mode=="CV2OC":
        response = value*CRYPTO_PRICES(crypto_name=crypto,currency="USD")
        response = response/CRYPTO_PRICES(crypto_name=other_crypto,currency="USD")
    else:
        raise ValueError(f"calculat_mode does not have a value named {calculat_mode}")

    if grouping:
        return SEPARATION_OF_NUMBERS(response)
    else:
        return response

#--------<donate>--------
def DONATE():
    return "UQCZgyJ4XB7c1GMnLgefqcc-zOA98hyOlMLZpO0EsCNxBq-e\n\n\nTON WALLET!"
