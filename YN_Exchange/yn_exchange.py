#----------------<info>-----------
# Developed by : Yasha Najafi
# Developer github : https://github.com/YashaNajafi
# Developer info page : https://YashaNajafi.github.io/about_me
# Module version : 2.5.2
# Module name : YN_EXCHANGE
# Number of supported crypto : 15
# Reference : https://ok-ex.io/

#----------------<libs>----------
import requests
from bs4 import BeautifulSoup
#----------------<functions>----------
    #-------------------<grouping>--------
def SEPARATION_OF_NUMBERS(number=int()):
    n_str = str(number)
    result = ""
    while len(n_str) > 0:
        group = n_str[-3:]  
        result = group + "," + result 
        n_str = n_str[:-3]
    return result[:-1]
    #----------------<ton function>----------
def TON_COIN_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/TON/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        ton_price=element.text
        ton_price=ton_price.replace(",","")
        ton_price=int(ton_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(ton_price)
        else:
            return ton_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/TON/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        ton_price=element.text
        ton_price=ton_price.replace("$ ","")
        ton_price=float(ton_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(ton_price)
        else:
            return ton_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<btc function>----------
def BTC_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/BTC/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        btc_price=element.text
        btc_price=btc_price.replace(",","")
        btc_price=int(btc_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(btc_price)
        else:
            return btc_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/BTC/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        btc_price=element.text
        btc_price=btc_price.replace("$ ","")
        btc_price=float(btc_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(btc_price)
        else:
            return btc_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<eth funtion>----------
def ETH_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/ETH/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        eth_price=element.text
        eth_price=eth_price.replace(",","")
        eth_price=int(eth_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(eth_price)
        else:
            return eth_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/ETH/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        eth_price=element.text
        eth_price=eth_price.replace("$ ","")
        eth_price=float(eth_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(eth_price)
        else:
            return eth_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<usdt function>----------
def USDT_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/USDT/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        usdt_price=element.text
        usdt_price=usdt_price.replace(",","")
        usdt_price=int(usdt_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(usdt_price)
        else:
            return usdt_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/USDT/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        usdt_price=element.text
        usdt_price=usdt_price.replace("$ ","")
        usdt_price=float(usdt_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(usdt_price)
        else:
            return usdt_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<shib function>----------
def SHIB_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/SHIB/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        shib_price=element.text
        shib_price=shib_price.replace(",","")
        shib_price=int(shib_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(shib_price)
        else:
            return shib_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/SHIB/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        shib_price=element.text
        shib_price=shib_price.replace("$ ","")
        shib_price=float(shib_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(shib_price)
        else:
            return shib_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<bnb function>----------
def BNB_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/BNB/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        bnb_price=element.text
        bnb_price=bnb_price.replace(",","")
        bnb_price=int(bnb_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(bnb_price)
        else:
            return bnb_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/BNB/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        bnb_price=element.text
        bnb_price=bnb_price.replace("$ ","")
        bnb_price=float(bnb_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(bnb_price)
        else:
            return bnb_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<doge function>----------
def DOGE_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/DOGE/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        doge_price=element.text
        doge_price=doge_price.replace(",","")
        doge_price=int(doge_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(doge_price)
        else:
            return doge_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/DOGE/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        doge_price=element.text
        doge_price=doge_price.replace("$ ","")
        doge_price=float(doge_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(doge_price)
        else:
            return doge_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<ada function>----------
def ADA_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/ADA/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        ada_price=element.text
        ada_price=ada_price.replace(",","")
        ada_price=int(ada_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(ada_price)
        else:
            return ada_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/ADA/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        ada_price=element.text
        ada_price=ada_price.replace("$ ","")
        ada_price=float(ada_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(ada_price)
        else:
            return ada_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<sol function>----------
def SOL_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/SOL/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        sol_price=element.text
        sol_price=sol_price.replace(",","")
        sol_price=int(sol_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(sol_price)
        else:
            return sol_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/SOL/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        sol_price=element.text
        sol_price=sol_price.replace("$ ","")
        sol_price=float(sol_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(sol_price)
        else:
            return sol_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<xrp function>----------
def XRP_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/XRP/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        xrp_price=element.text
        xrp_price=xrp_price.replace(",","")
        xrp_price=int(xrp_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(xrp_price)
        else:
            return xrp_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/XRP/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        xrp_price=element.text
        xrp_price=xrp_price.replace("$ ","")
        xrp_price=float(xrp_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(xrp_price)
        else:
            return xrp_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<usdc function>----------
def USDC_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/USDC/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        usdc_price=element.text
        usdc_price=usdc_price.replace(",","")
        usdc_price=int(usdc_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(usdc_price)
        else:
            return usdc_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/USDC/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        usdc_price=element.text
        usdc_price=usdc_price.replace("$ ","")
        usdc_price=float(usdc_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(usdc_price)
        else:
            return usdc_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<etc function>----------
def ETC_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/ETC/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        etc_price=element.text
        etc_price=etc_price.replace(",","")
        etc_price=int(etc_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(etc_price)
        else:
            return etc_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/ETC/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        etc_price=element.text
        etc_price=etc_price.replace("$ ","")
        etc_price=float(etc_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(etc_price)
        else:
            return etc_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<pepe function>----------
def PEPE_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/PEPE/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        pepe_price=element.text
        pepe_price=pepe_price.replace(",","")
        pepe_price=int(pepe_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(pepe_price)
        else:
            return pepe_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/PEPE/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        pepe_price=element.text
        pepe_price=pepe_price.replace("$ ","")
        pepe_price=float(pepe_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(pepe_price)
        else:
            return pepe_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<atm function>----------
def ATM_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/ATM/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        atm_price=element.text
        atm_price=atm_price.replace(",","")
        atm_price=int(atm_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(atm_price)
        else:
            return atm_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/ATM/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        atm_price=element.text
        atm_price=atm_price.replace("$ ","")
        atm_price=float(atm_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(atm_price)
        else:
            return atm_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
    #----------------<biso function>----------
def BISO_PRICE(currency:str,grouping=False):
    if currency=="IRT":
        url = "https://ok-ex.io/buy-and-sell/BISO/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg")
        biso_price=element.text
        biso_price=biso_price.replace(",","")
        biso_price=int(biso_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(biso_price)
        else:
            return biso_price
    elif currency=="USD":
        url = "https://ok-ex.io/buy-and-sell/BISO/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        element = soup.find("div", class_="text-neutral-400 text-base leading-8 whitespace-nowrap mt-4 lg:ml-10")
        biso_price=element.text
        biso_price=biso_price.replace("$ ","")
        biso_price=float(biso_price)
        if grouping==True:
            return SEPARATION_OF_NUMBERS(biso_price)
        else:
            return biso_price
    else:
        raise ValueError(f"Currency does not have a value with the name <{currency}>")
#-------------------<main functions>-------------
def donate():
    print("0xE95FAEc8B847F18B3bC5dc1bB8256fb376d2e459\n\nTo donate, you can deposit the desired amount of usdt to the above wallet :)")
#--------------------<tool functions>------------
def calculator(value:float,currency:str,crypto:str):
    if currency=="IRT" and crypto=="TON":
        return value*TON_COIN_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="TON":
        return value*TON_COIN_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="BTC":
        return value*BTC_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="BTC":
        return value*BTC_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="ETH":
        return value*ETC_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="ETH":
        return value*ETC_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="USDT":
        return value*USDT_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="USDT":
        return value*USDC_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="SHIB":
        return value*SHIB_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="SHIB":
        return value*SHIB_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="BNB":
        return value*BNB_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="BNB":
        return value*BNB_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="DOGE":
        return value*DOGE_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="DOGE":
        return value*DOGE_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="ADA":
        return value*ADA_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="ADA":
        return value*ADA_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="SOL":
        return value*SOL_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="SOL":
        return value*SOL_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="XRP":
        return value*XRP_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="XRP":
        return value*XRP_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="USDC":
        return value*USDC_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="USDC":
        return value*USDC_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="ETC":
        return value*ETC_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="ETC":
        return value*ETC_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="PEPE":
        return value*PEPE_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="PEPE":
        return value*PEPE_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="ATM":
        return value*ATM_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="ATM":
        return value*ATM_PRICE(currency="USD")
    elif currency=="IRT" and crypto=="BISO":
        return value*BISO_PRICE(currency="IRT")
    elif currency=="USD" and crypto=="BISO":
        return value*BISO_PRICE(currency="USD")
    else:
        raise ValueError("This values not supported! try again")
