#---------<info>-----------
# Developed by : Yasha Najafi
# Developer github : https://github.com/YashaNajafi
# Developer info page : https://YashaNajafi.github.io/about_me
# Module github page : https://github.com/YashaNajafi/YN_Exchange
# Module version : 6.0.0 (Async)
# Module name : YN_EXCHANGE (AsyncExchange)
# Number of supported crypto : ***
# References : https://ok-ex.io/ | https://www.tgju.org/ | https://www.xe.com/ | https://docs.ccxt.com/

#-----------<libs>----------
from bs4 import BeautifulSoup
import os , time , json ,logging , urllib3 , pandas , mplfinance , aiohttp , asyncio
from typing import Optional, Dict, Union
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as pyplot
import ccxt.async_support as ccxt

#------------<Functions>----------
    #---------<Grouping>-----------
def SEPARATION_OF_NUMBERS(number):
   if isinstance(number, str):
        number = float(number)
   return f"{number:,}"
#------------<Class>----------
class AsyncCryptoManager:

    #------------<PRIVATE VAR>-------------

    __CACHE_FILE = "CryptoCache.json"
    __SUPPORTED_CURRENCIES = ["IRT", "USD"]
    __SUPPORTED_TEMPLATE = ["Professional","Base","base","professional"]

    #---------------------------------------

    #------------<Init Function>-------------

    def __init__(self,Cache : bool = False , Cache_Duration: int = 300):
        #------------<Cache Config>-------------
        self.CacheManager = Cache
        self.Cache: Dict[str, Dict[str, Union[float, int]]] = {}
        self.Cache_Duration = Cache_Duration
        #---------------------------------------

        #------------<Log Config>-------------
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        #---------------------------------------

        #------------<Check Cache>-------------
        if self.CacheManager:
            self.Cache = self.__load_cache()
        #---------------------------------------

    #---------------------------------------

    #------------<Cache Fnctions>-------------

        #------------<Loads Data From Cache>-------------

    def __load_cache(self) -> Dict[str, Dict[str, Union[str, float, int]]]:
        if os.path.exists(self.__CACHE_FILE):
            try:
                #------------<Find And return Cache Data>-------------
                with open(self.__CACHE_FILE, "r") as f:
                    cache_data = json.load(f)
                    return cache_data
                #---------------------------------------
            except (json.JSONDecodeError, IOError) as e: # Error Handling And Manage Log
                logging.error(f"Error loading cache from file: {e}")
        return {} # Empty Cache

        #---------------------------------------

        #------------<Save Cache Data>-------------
    async def __save_cache(self):
        try:
            #------------<Save Cahche Data In Cache File>-------------
            with open(self.__CACHE_FILE, "w") as f:
                json.dump(self.Cache, f, indent=4)
            logging.info("Cache saved successfully.")
            #---------------------------------------
        except IOError as e:
            logging.error(f"Error saving cache to file: {e}") # Error Handling And Manage Log

        #---------------------------------------

        #------------<Check Crypto In Cache For Return>-------------
    def __is_cache_valid(self, CryptoName: str) -> bool:
        if CryptoName in self.Cache:
            cached_time = self.Cache[CryptoName]["Time"]
            if (time.time() - cached_time) < self.Cache_Duration: # Check Cache_Duration For Return Data From Cache
                return True
        return False
        #---------------------------------------

        #------------<Clear Cahche (For Developers)>-------------
    async def clear_cache(self):
        self.Cache.clear()
        if os.path.exists(self.__CACHE_FILE): # Check Cache Exists For Delete Cache Data
            os.remove(self.__CACHE_FILE) # Delete Cache Data
        logging.info("Cache cleared successfully.")
        #---------------------------------------

    #---------------------------------------

    #------------<Crypto Fnctions>-------------

        #------------<Crypto Price>-------------
    async def GetCryptoPrice(self, CryptoName : str = "BTC",Currency: str = "USD",Grouping: bool = False) -> Optional[Union[float, str]]:
        CryptoName = CryptoName.upper()
        Currency = Currency.upper()

        #------------<Check Supported Currencies (Error and Log Management)>-------------
        if Currency not in self.__SUPPORTED_CURRENCIES:
            logging.error(f"Unsupported Currency: {Currency}") # Log management
            raise ValueError(f"Unsupported Currency: {Currency}") # Error management
        #---------------------------------------


        #------------<Check Cache For Return Price>-------------
        if self.CacheManager and self.__is_cache_valid(CryptoName):
            logging.info(f"Using cached data for {CryptoName}") # Log Management
            Price = self.Cache[CryptoName][f"Price{Currency}"]  # Get Crypto Price From Cache File
            return SEPARATION_OF_NUMBERS(Price) if Grouping else Price # Return Price
        #---------------------------------------

        #------------<Get Crypto Price (WebScrap)>-------------
        try:
            #------------<Send Request And Get Data From WebSite>-------------
            url = f"https://ok-ex.io/buy-and-sell/{CryptoName.lower()}/" # Generate URL For Send Requests
            logging.info(f"Fetching data from {url}")     # Log Management

            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=10) as response: # Send Requests
                    #------------<Request Error Handling>-------------
                    if response.status != 200:
                        logging.error(f"Failed to fetch data, status code: {response.status}")
                        raise Exception(f"Failed to fetch data, status code: {response.status}")
                    #---------------------------------------

                    #------------<Find And Get Price>-------------
                    Content = await response.text()
                    soup = BeautifulSoup(Content, "html.parser")
                    irt_price = soup.find("div", class_="text-gray-500 lg:text-3xl text-lg").text.replace(",", "").strip()
                    usd_price = soup.find("div", class_="text-neutral-400 lg:text-2xl text-lg leading-8 whitespace-nowrap mt-0 lg:mt-2 ml-4 lg:ml-5 ltr").text.replace("$", "").replace(",", "").strip()
                    #---------------------------------------

            irt_price, usd_price = float(irt_price), float(usd_price) # Convert String To Float Variable
            #---------------------------------------

            #------------<Save Prices In Chache>-------------
            if self.CacheManager:
                self.Cache[CryptoName] = {
                    "Method": "GET",
                    "Crypto": CryptoName,
                    "PriceIRT": irt_price,
                    "PriceUSD": usd_price,
                    "Time": time.time(),
                    "Date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                }
                await self.__save_cache()
            #---------------------------------------

            #------------<Return Price>-------------
            price = irt_price if Currency == "IRT" else usd_price # Specify The Currency Type
            return SEPARATION_OF_NUMBERS(price) if Grouping else price # Return Price
            #---------------------------------------

            #------------<Error And Log Handling>-------------
        except Exception as e:
            logging.error(f"Error fetching data for {CryptoName}: {e}") # Log Handling
            return "Error fetching data, please try again later." # Error Handling

        except AttributeError as e:
            logging.error(f"Parsing error for {CryptoName}: {e}") # Log Handling
            return "Error parsing data, please try again later." # Error Handling
        #---------------------------------------

        #---------------------------------------

        #---------------------------------------

        #------------<Crypto Chart>-------------
    async def GenerateCryptoChart(
            self,
            ImageSave : bool = True,
            HTML_Save : bool = False,
            Json_Save : bool = False,
            ChartTemplate : str = "Professional",
            Exchange : str = "binance",
            CryptoSymbol : str = "BTC/USDT",
            Limit : int = 100,
            Timeframe = '1d',
            IchimokuLine : bool = True,
            IchimokuCloud : bool = True,
            Candlesticks : bool = True,
            Chikou : bool = True,
            Tenkan : bool = True,
            Kijun : bool = True,
            MACD_Line : bool = True,
            SignalLine : bool = True,
            Histogram : bool = True,
            ):

        logging.info("Getting data from method") # Log handling
        logging.info(f"Checking ChartTemplates : < {ChartTemplate} >") # Log handling

        #------------<Check ChartTemplates>-------------
        if ChartTemplate not in self.__SUPPORTED_TEMPLATE: # Checking from SUPPORTED_TEMPLATE variable
            raise ValueError(f"Unsupported Chart Template <{ChartTemplate}>")
        #---------------------------------------

        Exchange_Class = getattr(ccxt, Exchange.lower())
        self.Exchange = Exchange_Class()

        ohlcv = await self.Exchange.fetch_ohlcv(CryptoSymbol.upper(), Timeframe, limit=Limit)
        DataFrame = pandas.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        logging.info(f"Connected to {Exchange} exchange")

        # Ichimoku

        high9 = DataFrame['high'].rolling(window=9).max()
        low9 = DataFrame['low'].rolling(window=9).min()
        DataFrame['tenkan_sen'] = (high9 + low9) / 2

        High26 = DataFrame['high'].rolling(window=26).max()
        Low26 = DataFrame['low'].rolling(window=26).min()
        DataFrame['kijun_sen'] = (High26 + Low26) / 2

        DataFrame['senkou_span_a'] = ((DataFrame['tenkan_sen'] + DataFrame['kijun_sen']) / 2).shift(26)

        High52 = DataFrame['high'].rolling(window=52).max()
        Low52 = DataFrame['low'].rolling(window=52).min()
        DataFrame['senkou_span_b'] = ((High52 + Low52) / 2).shift(26)

        DataFrame['chikou_span'] = DataFrame['close'].shift(-26)

        # MACD

        Short_ema = DataFrame['close'].ewm(span=12, adjust=False).mean()
        Long_ema = DataFrame['close'].ewm(span=26, adjust=False).mean()
        DataFrame['macd'] = Short_ema - Long_ema
        DataFrame['signal'] = DataFrame['macd'].ewm(span=9, adjust=False).mean()
        DataFrame['histogram'] = DataFrame['macd'] - DataFrame['signal']

        # Generate Chart

        logging.info(f"Generating chart with < {ChartTemplate} > theme ")

        Name = CryptoSymbol.replace("/","-")

        if ChartTemplate in ["Professional", "professional"]:
            Chart = make_subplots(rows=2, cols=1, shared_xaxes=True,vertical_spacing=0.2, subplot_titles=(f'{CryptoSymbol} Candlestick Chart', 'MACD'))

            # Candlestick

            if Candlesticks :
                Chart.add_trace(
                    go.Candlestick(
                        x=DataFrame['timestamp'],
                        open=DataFrame['open'],
                        high=DataFrame['high'],
                        low=DataFrame['low'],
                        close=DataFrame['close'],
                        name='Candlesticks'
                    ),
                    row=1, col=1
                )

            # Ichimoku Lines Elements

            if Tenkan:
                Chart.add_trace(go.Scatter(x=DataFrame['timestamp'], y=DataFrame['tenkan_sen'], mode='lines', name='Tenkan-sen', line=dict(color='orange')),row=1, col=1)

            if Kijun:
                Chart.add_trace(go.Scatter(x=DataFrame['timestamp'], y=DataFrame['kijun_sen'], mode='lines', name='Kijun-sen', line=dict(color='blue')),row=1, col=1)

            if IchimokuLine:
                Chart.add_trace(go.Scatter(x=DataFrame['timestamp'], y=DataFrame['senkou_span_a'], mode='lines', name='Senkou Span A', line=dict(color='green', dash='dot')),row=1, col=1)
                Chart.add_trace(go.Scatter(x=DataFrame['timestamp'], y=DataFrame['senkou_span_b'], mode='lines', name='Senkou Span B', line=dict(color='red', dash='dot')),row=1, col=1)

            if Chikou:
                Chart.add_trace(go.Scatter(x=DataFrame['timestamp'], y=DataFrame['chikou_span'], mode='lines', name='Chikou Span', line=dict(color='purple')),row=1, col=1)

            if IchimokuLine and IchimokuCloud:
                Chart.add_trace(go.Scatter(
                x=pandas.concat([DataFrame['timestamp'], DataFrame['timestamp'][::-1]]),
                y=pandas.concat([DataFrame['senkou_span_a'], DataFrame['senkou_span_b'][::-1]]),
                fill='toself',
                fillcolor='rgba(0, 200, 100, 0.2)',
                line=dict(color='rgba(255,255,255,0)'),
                name='Ichimoku Cloud'
                ), row=1, col=1)

            elif IchimokuLine==False and IchimokuCloud:
                raise ValueError("Unable to draw <IchimokuCloud> , Because <IchimokuLine> lines are not active")

            # MACD

            if MACD_Line:
                Chart.add_trace(go.Scatter(x=DataFrame['timestamp'], y=DataFrame['macd'], mode='lines', name='MACD Line', line=dict(color='blue')),row=2, col=1)

            if Histogram:
                Chart.add_trace(go.Bar(x=DataFrame['timestamp'], y=DataFrame['macd'] - DataFrame['signal'], name='Histogram', marker_color='green'),row=2, col=1)

            if SignalLine:
                Chart.add_trace(go.Scatter(x=DataFrame['timestamp'], y=DataFrame['signal'], mode='lines', name='Signal Line', line=dict(color='red')),row=2, col=1)

            # Final Generate

            Chart.update_layout(height=800,title=f'{CryptoSymbol} Price Chart',xaxis_title='Date',yaxis_title='Price',template='plotly_dark')

            # Output

            if ImageSave:
                await asyncio.to_thread(Chart.write_image, f"{Name} Chart.jpg")
                logging.info(f"Image Chart generated with < {Name} Chart.jpg > name and < {ChartTemplate} > template")
            if HTML_Save:
                await asyncio.to_thread(Chart.write_html, f"{Name} Chart.html")
                logging.info(f"HTML Chart generated with < {Name} Chart.html > name and < {ChartTemplate} > template")
            if Json_Save:
                await asyncio.to_thread(Chart.write_image, f"{Name} Chart.json")
                logging.info(f"JSON Chart generated with < {Name} Chart.json > name and < {ChartTemplate} > template")

        elif ChartTemplate in ["Base", "base"]:
            ChartBase, Axes = pyplot.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [3, 1]})
            DataFrame['timestamp'] = pandas.to_datetime(DataFrame['timestamp'], unit='ms')
            DataFrame.set_index('timestamp', inplace=True)

            if Candlesticks:
                mplfinance.plot(DataFrame, type='candle', ax=Axes[0], volume=False, style='yahoo')

            Axes[0].set_title(f'{CryptoSymbol} Candlestick Chart')

            if MACD_Line:
                Axes[1].plot(DataFrame.index, DataFrame['macd'], label='MACD', color='blue')
            if SignalLine:
                Axes[1].plot(DataFrame.index, DataFrame['signal'], label='Signal', color='red')

            if Histogram:
                colors = DataFrame['histogram'].apply(lambda x: 'green' if x >= 0 else 'red')
                Axes[1].bar(DataFrame.index, DataFrame['histogram'], color=colors, label='Histogram', width=0.5)


            Axes[1].legend(loc='upper left')
            Axes[1].set_title('MACD')
            Axes[1].grid(True)
            Axes[0].grid(True)

            pyplot.tight_layout()
            await asyncio.to_thread(pyplot.savefig, f"{Name} Chart.jpg")
            logging.info(f"Chart generated with < {Name} Chart.jpg > name and < {ChartTemplate} > template")

        #---------------------------------------

        await self.Exchange.close()

    #---------------------------------------


class ExchangeAPI:
    def __init__(self,Exchange : str = "binance"):

        Exchange_Class = getattr(ccxt, Exchange.lower())
        self.Exchange = Exchange_Class()
        logging.info(f"Connected to {Exchange} exchange")

    async def GetCryptoData(self,CryptoSymbol : str):
        JsonData = await self.Exchange.fetch_ticker(CryptoSymbol.upper())
        await self.Exchange.close()
        return JsonData

class AsyncMetalManager:

    __CACHE_FILE = "MetalCache.json"

    #------------<Init Function>-------------

    def __init__(self,Cache : bool = False , Cache_Duration: int = 300):
        #------------<Cache Config>-------------
        self.CacheManager = Cache
        self.Cache: Dict[str, Dict[str, Union[float, int]]] = {}
        self.Cache_Duration = Cache_Duration
        #---------------------------------------

        #------------<Log Config>-------------
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        #---------------------------------------

        #------------<Check Cache>-------------
        if self.CacheManager:
            self.Cache = self.__load_cache()
        #---------------------------------------

    #---------------------------------------

    #------------<Cache Fnctions>-------------

        #------------<Loads Data From Cache>-------------

    def __load_cache(self) -> Dict[str, Dict[str, Union[str, float, int]]]:
        if os.path.exists(self.__CACHE_FILE):
            try:
                #------------<Find And return Cache Data>-------------
                with open(self.__CACHE_FILE, "r") as f:
                    cache_data = json.load(f)
                    return cache_data
                #---------------------------------------
            except (json.JSONDecodeError, IOError) as e: # Error Handling And Manage Log
                logging.error(f"Error loading cache from file: {e}")
        return {} # Empty Cache

        #---------------------------------------

        #------------<Save Cache Data>-------------
    def __save_cache(self):
        try:
            #------------<Save Cahche Data In Cache File>-------------
            with open(self.__CACHE_FILE, "w") as f:
                json.dump(self.Cache, f, indent=4)
            logging.info("Cache saved successfully.")
            #---------------------------------------
        except IOError as e:
            logging.error(f"Error saving cache to file: {e}") # Error Handling And Manage Log

        #---------------------------------------

        #------------<Check Crypto In Cache For Return>-------------
    def __is_cache_valid(self, MetalName: str) -> bool:
        if MetalName in self.Cache:
            cached_time = self.Cache[MetalName]["Time"]
            if (time.time() - cached_time) < self.Cache_Duration: # Check Cache_Duration For Return Data From Cache
                return True
        return False
        #---------------------------------------

        #------------<Clear Cahche (For Developers)>-------------
    def clear_cache(self):
        self.Cache.clear()
        if os.path.exists(self.__CACHE_FILE): # Check Cache Exists For Delete Cache Data
            os.remove(self.__CACHE_FILE) # Delete Cache Data
        logging.info("Cache cleared successfully.")
        #---------------------------------------

    #---------------------------------------

        #------------<Base Get Price>-------------
    async def __GetBasePrice(self,Grouping : bool = False,Metal : str = ""):
        #------------<Check Cache For Return Price>-------------
        if self.CacheManager and self.__is_cache_valid(Metal):
            logging.info(f"Using cached data for {Metal}") # Log Management
            Price = self.Cache[Metal]["Price"]  # Get Crypto Price From Cache File
            return SEPARATION_OF_NUMBERS(Price) if Grouping else Price # Return Price
        #---------------------------------------

        #------------<Get Price (WebScrap)>-------------
        try:
            #------------<Send Request And Get Data From WebSite>-------------
            URL = f"https://www.tgju.org/profile/basemetal-{Metal.lower()}" # Generate URL For Send Requests
            logging.info(f"Fetching data from {URL}")                    # Log Management

            async with aiohttp.ClientSession() as session:
                async with session.get(URL, timeout=10) as response: # Send Requests
                    #------------<Request Error Handling>-------------
                    if response.status != 200:
                        logging.error(f"Failed to fetch data, status code: {response.status}")
                        raise Exception(f"Failed to fetch data, status code: {response.status}")
                    #---------------------------------------

                    #------------<Find And Get Price>-------------
                    Content = await response.text()
                    soup = BeautifulSoup(Content, "html.parser") # Send Request (Site) Content For BS4
                    Price = soup.find("span", {'data-col': 'info.last_trade.PDrCotVal'}).text.replace(",","").strip()
                    #---------------------------------------

            Price = float(Price) # Convert String To Float Variable
            #---------------------------------------

            #------------<Save Prices In Chache>-------------
            if self.CacheManager:
                self.Cache[Metal] = {
                    "Method": "GET",
                    "Price": Price,
                    "Time": time.time(),
                    "Date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                }
                self.__save_cache()
            #---------------------------------------

            #------------<Return Price>-------------
            return SEPARATION_OF_NUMBERS(Price) if Grouping else Price # Return Price
            #---------------------------------------

            #------------<Error And Log Handling>-------------
        except Exception as e:
            logging.error(f"Error fetching data for {Metal} : {e}") # Log Handling
            return "Error fetching data, please try again later." # Error Handling

        except AttributeError as e:
            logging.error(f"Parsing error for {Metal} : {e}") # Log Handling
            return "Error parsing data, please try again later." # Error Handling
            #---------------------------------------
        #---------------------------------------

    async def __GetBaseOuncePrice(self,Grouping : bool = False,Metal : str = ""):

        #------------<Check Cache For Return Price>-------------
        if self.CacheManager and self.__is_cache_valid(Metal):
            logging.info(f"Using cached data for {Metal}") # Log Management
            Price = self.Cache[Metal]["Price"]  # Get Crypto Price From Cache File
            return SEPARATION_OF_NUMBERS(Price) if Grouping else Price # Return Price
        #---------------------------------------

        #------------<Get Price (WebScrap)>-------------
        try:
            #------------<Send Request And Get Data From WebSite>-------------
            URL = f"https://www.tgju.org/profile/{Metal.lower()}" # Generate URL For Send Requests
            logging.info(f"Fetching data from {URL}")                    # Log Management
            async with aiohttp.ClientSession() as session:
                async with session.get(URL, timeout=10) as response: # Send Requests
                    #------------<Request Error Handling>-------------
                    if response.status != 200:
                        logging.error(f"Failed to fetch data, status code: {response.status}")
                        raise Exception(f"Failed to fetch data, status code: {response.status}")
                    #---------------------------------------

                    #------------<Find And Get Price>-------------
                    Content = await response.text()
                    soup = BeautifulSoup(Content, "html.parser") # Send Request (Site) Content For BS4
                    Price = soup.find("span", {'data-col': 'info.last_trade.PDrCotVal'}).text.replace(",","").strip()
                    #---------------------------------------

            Price = float(Price) # Convert String To Float Variable
            #---------------------------------------

            #------------<Save Prices In Chache>-------------
            if self.CacheManager:
                self.Cache[Metal] = {
                    "Method": "GET",
                    "Price": Price,
                    "Time": time.time(),
                    "Date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                }
                self.__save_cache()
            #---------------------------------------

            #------------<Return Price>-------------
            return SEPARATION_OF_NUMBERS(Price) if Grouping else Price # Return Price
            #---------------------------------------

            #------------<Error And Log Handling>-------------
        except Exception as e:
            logging.error(f"Error fetching data for {Metal} : {e}") # Log Handling
            return "Error fetching data, please try again later." # Error Handling

        except AttributeError as e:
            logging.error(f"Parsing error for {Metal} : {e}") # Log Handling
            return "Error parsing data, please try again later." # Error Handling
            #---------------------------------------

    async def GetGoldPrice(self,Carat : int = 18,Weight : str = "gram",Grouping : bool = False):
        #------------<Check Supported Weight (Error and Log Management)>-------------
        if Weight.lower() not in ["gram","kilo","ounce"]:
            logging.error(f"Unsupported Weight: {Weight}") # Log management
            raise ValueError(f"Unsupported Weight: {Weight}") # Error management
        #---------------------------------------

        CheckedName = f"Gold{Carat}" if Weight.lower() in ["gram","kilo"] else f"Gold{Weight}"

        #------------<Check Cache For Return Price>-------------
        if self.CacheManager and self.__is_cache_valid(CheckedName):
            logging.info(f"Using cached data for Gold{Carat}k") # Log Management
            Price = self.Cache[f"Gold{Carat}"][f"Price"] if Weight.lower() in ["Kilo","gram"] else  self.Cache[f"Gold{Weight}"][f"Price"] # Get Crypto Price From Cache File
            return SEPARATION_OF_NUMBERS(Price) if Grouping else Price # Return Price
        #---------------------------------------

        #------------<Get Gold Price (WebScrap)>-------------
        try:
            #------------<Send Request And Get Data From WebSite>-------------
            CaratURL=f"https://www.tgju.org/profile/geram{Carat}" # Generate URL For Send Requests
            OunceURL = "https://www.tgju.org/profile/ons"
            if Weight.lower()=="ounce":
                logging.info(f"Fetching data from {OunceURL}")                    # Log Management
                MainURL = OunceURL
            else:
                logging.info(f"Fetching data from {CaratURL}")                    # Log Management
                MainURL = CaratURL

            async with aiohttp.ClientSession() as session:
                async with session.get(MainURL, timeout=10) as response: # Send Requests
                    #------------<Request Error Handling>-------------
                    if response.status != 200:
                        logging.error(f"Failed to fetch data, status code: {response.status}")
                        raise Exception(f"Failed to fetch data, status code: {response.status}")
                    #---------------------------------------

                    #------------<Find And Get Price>-------------
                    Content = await response.text()
                    soup = BeautifulSoup(Content, "html.parser") # Send Request (Site) Content For BS4
                    Price = soup.find("span", {'data-col': 'info.last_trade.PDrCotVal'}).text.replace(",","").strip()
                    #---------------------------------------


            Price = float(Price)//10 if Weight.lower()!="ounce" else Price # Convert String To Float Variable
            #---------------------------------------

            #------------<Save Prices In Chache>-------------
            if Weight.lower() in ["Kilo","gram"]:
                if self.CacheManager:
                    self.Cache[f"Gold{Carat}"] = {
                        "Method": "GET",
                        "Carat": Carat,
                        "Price": Price,
                        "Weight" : Weight,
                        "Time": time.time(),
                        "Date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    }
                    self.__save_cache()
            else:
                if self.CacheManager:
                    self.Cache[f"Gold{Weight}"] = {
                        "Method": "GET",
                        "Carat": Carat,
                        "Price": Price,
                        "Weight" : Weight,
                        "Time": time.time(),
                        "Date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    }
                    self.__save_cache()
            #---------------------------------------

            #------------<Return Price>-------------
            Price = Price*1000 if Weight.lower() in ["Kilo","kilo"] else Price # Specify The Currency Type
            return SEPARATION_OF_NUMBERS(Price) if Grouping else Price # Return Price
            #---------------------------------------

            #------------<Error And Log Handling>-------------
        except Exception as e:
            logging.error(f"Error fetching data for Gold{Carat}k : {e}") # Log Handling
            return "Error fetching data, please try again later." # Error Handling

        except AttributeError as e:
            logging.error(f"Parsing error for Gold{Carat}k : {e}") # Log Handling
            return "Error parsing data, please try again later." # Error Handling
            #---------------------------------------

        #---------------------------------------

    async def GetAluminiumPrice(self,Grouping : bool = False):
        return await self.__GetBasePrice(Grouping=Grouping,Metal="Aluminum")

    async def GetCopperPrice(self,Grouping : bool = False):
        return await self.__GetBasePrice(Grouping=Grouping,Metal="Copper")

    async def GetLeadPrice(self,Grouping : bool = False):
        return await self.__GetBasePrice(Grouping=Grouping,Metal="Lead")

    async def GetZincPrice(self,Grouping : bool = False):
        return await self.__GetBasePrice(Grouping=Grouping,Metal="Zinc")

    async def GetNickelPrice(self,Grouping : bool = False):
        return await self.__GetBasePrice(Grouping=Grouping,Metal="Nickel")

    async def GetTinPrice(self,Grouping : bool = False):
        return await self.__GetBasePrice(Grouping=Grouping,Metal="Tin")

    async def GetPalladiumPrice(self,Grouping : bool = False):
        return await self.__GetBaseOuncePrice(Grouping=Grouping,Metal="Palladium")

    async def GetSilverPrice(self,Grouping : bool = False):
        return await self.__GetBaseOuncePrice(Grouping=Grouping,Metal="Silver")

    async def GetPlatinumPrice(self,Grouping : bool = False):
        return await self.__GetBaseOuncePrice(Grouping=Grouping,Metal="Platinum")



class AsyncNaturalResourcesManager:
    __CACHE_FILE = "NaturalResourcesCache.json"

    #------------<Init Function>-------------

    def __init__(self,Cache : bool = False , Cache_Duration: int = 300):
        #------------<Cache Config>-------------
        self.CacheManager = Cache
        self.Cache: Dict[str, Dict[str, Union[float, int]]] = {}
        self.Cache_Duration = Cache_Duration
        #---------------------------------------

        #------------<Log Config>-------------
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        #---------------------------------------

        #------------<Requests Config>-------------
        self.HTTP = urllib3.PoolManager()
        #---------------------------------------

        #------------<Check Cache>-------------
        if self.CacheManager:
            self.Cache = self.__load_cache()
        #---------------------------------------

    #---------------------------------------

    #------------<Cache Fnctions>-------------

        #------------<Loads Data From Cache>-------------

    def __load_cache(self) -> Dict[str, Dict[str, Union[str, float, int]]]:
        if os.path.exists(self.__CACHE_FILE):
            try:
                #------------<Find And return Cache Data>-------------
                with open(self.__CACHE_FILE, "r") as f:
                    cache_data = json.load(f)
                    return cache_data
                #---------------------------------------
            except (json.JSONDecodeError, IOError) as e: # Error Handling And Manage Log
                logging.error(f"Error loading cache from file: {e}")
        return {} # Empty Cache

        #---------------------------------------

        #------------<Save Cache Data>-------------
    def __save_cache(self):
        try:
            #------------<Save Cahche Data In Cache File>-------------
            with open(self.__CACHE_FILE, "w") as f:
                json.dump(self.Cache, f, indent=4)
            logging.info("Cache saved successfully.")
            #---------------------------------------
        except IOError as e:
            logging.error(f"Error saving cache to file: {e}") # Error Handling And Manage Log

        #---------------------------------------

        #------------<Check Crypto In Cache For Return>-------------
    def __is_cache_valid(self, ResourcesName: str) -> bool:
        if ResourcesName in self.Cache:
            cached_time = self.Cache[ResourcesName]["Time"]
            if (time.time() - cached_time) < self.Cache_Duration: # Check Cache_Duration For Return Data From Cache
                return True
        return False
        #---------------------------------------

        #------------<Clear Cahche (For Developers)>-------------
    def clear_cache(self):
        self.Cache.clear()
        if os.path.exists(self.__CACHE_FILE): # Check Cache Exists For Delete Cache Data
            os.remove(self.__CACHE_FILE) # Delete Cache Data
        logging.info("Cache cleared successfully.")
        #---------------------------------------

    #---------------------------------------

    async def __BaseGetPrice(self,Grouping : bool = False,Value : str = "",Name : str = ""):
         #------------<Check Cache For Return Price>-------------
        if self.CacheManager and self.__is_cache_valid(Name):
            logging.info(f"Using cached data for {Name}") # Log Management
            Price = self.Cache[Name]["Price"]  # Get Crypto Price From Cache File
            return SEPARATION_OF_NUMBERS(Price) if Grouping else Price # Return Price
        #---------------------------------------

        #------------<Get Price (WebScrap)>-------------
        try:
            #------------<Send Request And Get Data From WebSite>-------------
            URL = f"https://www.tgju.org/profile/{Value.lower()}" # Generate URL For Send Requests
            logging.info(f"Fetching data from {URL}")                    # Log Management

            async with aiohttp.ClientSession() as session:
                async with session.get(URL, timeout=10) as response: # Send Requests
                    #------------<Request Error Handling>-------------
                    if response.status != 200:
                        logging.error(f"Failed to fetch data, status code: {response.status}")
                        raise Exception(f"Failed to fetch data, status code: {response.status}")
                    #---------------------------------------

                    #------------<Find And Get Price>-------------
                    Content = await response.text()
                    soup = BeautifulSoup(Content, "html.parser") # Send Request (Site) Content For BS4
                    Price = soup.find("span", {'data-col': 'info.last_trade.PDrCotVal'}).text.replace(",","").strip()
                    #---------------------------------------

            Price = float(Price) # Convert String To Float Variable
            #---------------------------------------

            #------------<Save Prices In Chache>-------------
            if self.CacheManager:
                self.Cache[Name] = {
                    "Method": "GET",
                    "Price": Price,
                    "Time": time.time(),
                    "Date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                }
                self.__save_cache()
            #---------------------------------------

            #------------<Return Price>-------------
            return SEPARATION_OF_NUMBERS(Price) if Grouping else Price # Return Price
            #---------------------------------------

            #------------<Error And Log Handling>-------------
        except Exception as e:
            logging.error(f"Error fetching data for {Name} : {e}") # Log Handling
            return "Error fetching data, please try again later." # Error Handling

        except AttributeError as e:
            logging.error(f"Parsing error for {Name} : {e}") # Log Handling
            return "Error parsing data, please try again later." # Error Handling
            #---------------------------------------
        #---------------------------------------

    async def GetCrudeOilWTI(self,Grouping : bool = False):
        return await self.__BaseGetPrice(Grouping=Grouping,Name="WTI_Oil",Value="energy-crude-oil")

    async def GetBrentOil(self,Grouping : bool = False):
        return await self.__BaseGetPrice(Grouping=Grouping,Name="BrentOil",Value="energy-brent-oil")

    async def GetNaturalGas(self,Grouping : bool = False):
        return await self.__BaseGetPrice(Grouping=Grouping,Name="NaturalGas",Value="energy-natural-gas")


class AsyncCalculator:
    def __init__(self):
        self.CryptoManagerObject = AsyncCryptoManager(Cache=False)
        self.MetalManagerObject = AsyncMetalManager(Cache=False)
        self.NaturalResourcesManagerObject = AsyncNaturalResourcesManager(Cache=False)

    async def CryptoValue2Currency(self, Value: int, CryptoName: str = "BTC", Currency: str = "USD", Grouping: bool = False):
        Response = Value * await self.CryptoManagerObject.GetCryptoPrice(CryptoName=CryptoName, Currency=Currency)
        return SEPARATION_OF_NUMBERS(Response) if Grouping else Response

    async def Currency2CryptoValue(self, Value: int, CryptoName: str = "BTC", Currency: str = "USD", Grouping: bool = False):
        Response = Value / await self.CryptoManagerObject.GetCryptoPrice(CryptoName=CryptoName, Currency=Currency)
        return SEPARATION_OF_NUMBERS(Response) if Grouping else Response

    async def CryptoValue2CryptoValue(self, CryptoValue: int, CryptoName1: str = "BTC", CryptoName2: str = "ETH", Grouping: bool = False):
        Price1 = await self.CryptoManagerObject.GetCryptoPrice(CryptoName=CryptoName1, Currency="USD")
        Price2 = await self.CryptoManagerObject.GetCryptoPrice(CryptoName=CryptoName2, Currency="USD")
        Response = (CryptoValue * Price1) / Price2
        return SEPARATION_OF_NUMBERS(Response) if Grouping else Response

    async def CryptoValue2GoldWeight(self, GoldCarat: int = 18, GoldWeight: str = "gram", CryptoName: str = "BTC"):
        crypto_price = await self.CryptoManagerObject.GetCryptoPrice(CryptoName=CryptoName, Currency="USD")
        gold_price = await self.MetalManagerObject.GetGoldPrice(Carat=GoldCarat, Weight=GoldWeight)
        return crypto_price / gold_price

    async def GoldWeight2CryptoValue(self, GoldCarat: int = 18, GoldWeight: str = "gram", GoldValue: int = 1, CryptoName: str = "BTC"):
        gold_price = await self.MetalManagerObject.GetGoldPrice(Carat=GoldCarat, Weight=GoldWeight) * GoldValue
        crypto_price = await self.CryptoManagerObject.GetCryptoPrice(CryptoName=CryptoName, Currency="USD")
        return gold_price / crypto_price

    async def GoldWeight2Currency(self, GoldCarat: int = 18, GoldWeight: str = "gram", GoldValue: int = 1, Currency: str = "USD"):
        gold_price = await self.MetalManagerObject.GetGoldPrice(Carat=GoldCarat, Weight=GoldWeight) * GoldValue
        return gold_price

    async def Currency2GoldWeight(self, GoldCarat: int = 18, GoldWeight: str = "gram", CurrencyValue : int = 5000000):
        gold_price = await self.MetalManagerObject.GetGoldPrice(Carat=GoldCarat, Weight=GoldWeight)
        return CurrencyValue / gold_price
