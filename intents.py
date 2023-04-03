from bs4 import BeautifulSoup
import requests
import json

url021="https://www.google.com/finance/quote/RELIANCE:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
Reliance=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


#TCS=TATA CONSULTANCY SERVICES
url022="https://www.google.com/finance/quote/TCS:NSE"
htmltext022=requests.get(url022)
soup007=BeautifulSoup(htmltext022.text,"html.parser")
TCS=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


#HDFCN HDFC BANK
url023="https://www.google.com/finance/quote/HDFC:NSE"
htmltext023=requests.get(url023)
soup007=BeautifulSoup(htmltext023.text,"html.parser")
HDFC=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


#INFY=INFOSYS
url024="https://www.google.com/finance/quote/INFY:NSE"
htmltext024=requests.get(url024)
soup007=BeautifulSoup(htmltext024.text,"html.parser")
INFY=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


#HINDUNILVR=HINDUSTAN UNILEVER
url025="https://www.google.com/finance/quote/HINDUNILVR:NSE"
htmltext025=requests.get(url025)
soup007=BeautifulSoup(htmltext025.text,"html.parser")
HINDUNILVR=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


#LICI=LIFE INSURANCE CORPORATION OF INDIA
url026="https://www.google.com/finance/quote/LICI:NSE"
htmltext026=requests.get(url026)
soup007=BeautifulSoup(htmltext026.text,"html.parser")
LICI=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


#HDFCNSE=HOUSING DEVELOPMENT CORPORATION LIMITED
url027="https://www.google.com/finance/quote/HDFC:NSE"
htmltext027=requests.get(url027)
soup007=BeautifulSoup(htmltext027.text,"html.parser")
HDFCNSE=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url028="https://www.google.com/finance/quote/ICICIBANK:NSE"
htmltext028=requests.get(url028)
soup007=BeautifulSoup(htmltext028.text,"html.parser")
ICICI=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url029="https://www.google.com/finance/quote/BAJFINANCE:NSE"
htmltext029=requests.get(url029)
soup007=BeautifulSoup(htmltext029.text,"html.parser")
BAJAJFINANCE=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/MRF:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
MRF=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/ONGC:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
ONGC=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/ITC:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
ITC=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/IOC:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
IOC=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/TVSMOTOR:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
TVS=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/HINDALCO:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
HINDALCO=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/TATAMOTORS:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
TATAM=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/TATASTEEL:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
TATAS=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/JSWSTEEL:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
JSW=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/HCLTECH:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
HCL=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/SAIL:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
SAIL=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/BPCL:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
BPCL=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/HEROMOTOCO:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
HERO=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/WIPRO:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
WIPRO=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/CIPLA:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
CIPLA=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/BHARTIARTL:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
AIRTEL=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/TITAN:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
TITAN=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/KOTAKBANK:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
KOTAK=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/LT:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
LT=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/TSLA:NASDAQ"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
TESLA=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/ADANIPOWER:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
ADANI=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/QSR:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
BURG=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/MCD:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
MCD=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/YUM:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
YUM=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/DPZ:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
PHUT=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/PZZA:NASDAQ"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
PAPA=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/SBUX:NASDAQ"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
STAR=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/NKE:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
NIKE=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/AMD:NASDAQ"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
AMD=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/TSM:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
TSM=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/V:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
V=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/MANU:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
MANU=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/NESTLEIND:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
NESTLE=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/BIOCON:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
BIOCON=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/MA:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
MASTERCARD=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/XOM:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
EXXON=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/UNH:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
UNH=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/JPM:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
JPM=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/CVX:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
CVX=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/BEL:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
BEL=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/DLF:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
DLF=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/INDUSINDBK:NSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
INDUS=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/JNJ:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
JNJ=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


url021="https://www.google.com/finance/quote/PG:NYSE"
htmltext021=requests.get(url021)
soup007=BeautifulSoup(htmltext021.text,"html.parser")
PG=soup007.find("div",{"class":"YMlKec fxKbKc"}).text


#SBI=STATE BANK OF INDIA
url030="https://www.google.com/finance/quote/SBIN:NSE"
htmltext030=requests.get(url030)
soup007=BeautifulSoup(htmltext030.text,"html.parser")
SBI=soup007.find("div",{"class":"YMlKec fxKbKc"}).text

#APPLE
url= "https://finance.yahoo.com/quote/AAPL"
htmltext001=requests.get(url)
soup=BeautifulSoup(htmltext001.text,"html.parser")
Apple=soup.find("fin-streamer",{"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
AppleChange=soup.find_all("span", {"class":"C($negativeColor)"})[6].text
ApplePercentage=soup.find_all("span", {"class":"C($negativeColor)"})[7].text

#NETFLIX
url002="https://finance.yahoo.com/quote/NFLX"
htmltext002=requests.get(url002)
soup002=BeautifulSoup(htmltext002.text,"html.parser")
Netflix=soup002.find("fin-streamer",{"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
NetflixChange=soup.find_all("span", {"class":"C($negativeColor)"})[12].text
NetflixPercentage=soup.find_all("span", {"class":"C($negativeColor)"})[13].text

#AMAZON
url004="https://finance.yahoo.com/quote/AMZN"
htmltext004=requests.get(url004)
soup004=BeautifulSoup(htmltext004.text,"html.parser")
Amazon=soup004.find("fin-streamer",{"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
AmazonChange=soup.find_all("span", {"class":"C($negativeColor)"})[8].text
AmazonPercentage=soup.find_all("span", {"class":"C($negativeColor)"})[9].text

#MICROSOFT
url007="https://finance.yahoo.com/quote/MSFT"
htmltext007=requests.get(url007)
soup007=BeautifulSoup(htmltext007.text,"html.parser")
Microsoft=soup007.find("fin-streamer",{"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
MicrosoftChange=soup.find_all("span", {"class":"C($negativeColor)"})[13].text
MicrosoftPercentage=soup.find_all("span", {"class":"C($negativeColor)"})[14].text

#GOOGLE
url008="https://finance.yahoo.com/quote/GOOG"
htmltext008=requests.get(url008)
soup008=BeautifulSoup(htmltext008.text,"html.parser")
Alphabet=soup008.find("fin-streamer",{"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
AlphabetChange=soup.find_all("span", {"class":"C($negativeColor)"})[10].text
AlphabetPercentage=soup.find_all("span", {"class":"C($negativeColor)"})[11].text

#META
url010="https://finance.yahoo.com/quote/META"
htmltext010=requests.get(url010)
soup010=BeautifulSoup(htmltext010.text,"html.parser")
Meta=soup010.find("fin-streamer",{"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
MetaChange=soup.find_all("span", {"class":"C($negativeColor)"})[10].text
MetaPercentage=soup.find_all("span", {"class":"C($negativeColor)"})[11].text

#NVIDIA
url010="https://finance.yahoo.com/quote/NVDA"
htmltext010=requests.get(url010)
soup010=BeautifulSoup(htmltext010.text,"html.parser")
Nvidia=soup010.find("fin-streamer",{"class":"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
NvidiaChange=soup.find_all("span", {"class":"C($negativeColor)"})[10].text
NvidiaPercentage=soup.find_all("span", {"class":"C($negativeColor)"})[11].text




dict={"intents":[ {"tag" :"greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day"
      ],
      "responses": [
        "Hey :-)",
        "Hi there, how can I help?"
      ]
    },
                  {
                      "tag": "goodbye",
                      "patterns": ["Bye", "See you later", "Goodbye"],
                      "responses": [
                          "See you later",
                          "Have a nice day",
                          "Bye!"
                      ]
                  },
                  {
                      "tag": "Reliance stock",
                      "patterns": ["RELIANCE STOCK PRICE", "Reliance stock price",
                                   "What is the stock price of Reliance?"],
                      "responses": [Reliance]
                  },

{
                      "tag": "TCS stock",
                      "patterns": ["TCS STOCK PRICE", "TCS stock price",
                                   "What is the stock price of TCS?"],
                      "responses": [TCS]
                  },
{
                      "tag": "HDFC stock",
                      "patterns": ["HDFC STOCK PRICE", "HDFC stock price",
                                   "What is the stock price of HDFC?"],
                      "responses": [HDFC]
                  },
{
                      "tag": "Infosys stock",
                      "patterns": ["INFOSYS STOCK PRICE", "Infosys stock price",
                                   "What is the stock price of Reliance?"],
                      "responses": [INFY]
                  },
{
                      "tag": "Hindustan Unilever stock",
                      "patterns": ["HINDUSTAN UNILEVER STOCK PRICE", "Hindustan Unilever stock price",
                                   "What is the stock price of Hindustan Unilever?"],
                      "responses": [HINDUNILVR]
                  },
{
                      "tag": "LIC stock",
                      "patterns": ["LIC STOCK PRICE", "LIC stock price",
                                   "What is the stock price of LIC?"],
                      "responses": [LICI]
                  },
{
                      "tag": "ICICI stock",
                      "patterns": ["ICICI STOCK PRICE", "ICICI stock price",
                                   "What is the stock price of ICICI?"],
                      "responses": [ICICI]
                  },
{
                      "tag": "Bajaj Finance stock",
                      "patterns": ["BAJAJ FINANCE STOCK PRICE", "Bajaj Finance stock price",
                                   "What is the stock price of Bajaj Finance?"],
                      "responses": [BAJAJFINANCE]
                  },
{
                      "tag": "MRF stock",
                      "patterns": ["MRF STOCK PRICE", "MRF stock price",
                                   "What is the stock price of MRF?"],
                      "responses": [MRF]
                  },
{
                      "tag": "ONGC stock",
                      "patterns": ["ONGC PRICE", "ONGC stock price",
                                   "What is the stock price of ONGC?"],
                      "responses": [ONGC]
                  },
{
                      "tag": "ITC stock",
                      "patterns": ["ITC STOCK PRICE", "ITC stock price",
                                   "What is the stock price of ITC?"],
                      "responses": [ITC]
                  },
{
                      "tag": "IOC stock",
                      "patterns": ["IOC PRICE", "IOC stock price",
                                   "What is the stock price of IOC?"],
                      "responses": [IOC]
                  },
{
                      "tag": "TVS stock",
                      "patterns": ["TVS STOCK PRICE", "TVS stock price",
                                   "What is the stock price of TVS?"],
                      "responses": [TVS]
                  },
{
                      "tag": "Hindalco stock",
                      "patterns": ["HINDALCO STOCK PRICE", "Hindalco stock price",
                                   "What is the stock price of HINDALCO?"],
                      "responses": [HINDALCO]
                  },
{
                      "tag": "TATA MOTORS stock",
                      "patterns": ["TATA MOTORS STOCK PRICE", "TATA Motors stock price",
                                   "What is the stock price of TATA Motors?"],
                      "responses": [TATAM]
                  },
{
                      "tag": "TATA STEEL",
                      "patterns": ["TATA STEEL PRICE", "TATA Steel stock price",
                                   "What is the stock price of TATA STEEL?"],
                      "responses": [TATAS]
                  },
{
                      "tag": "JSW stock",
                      "patterns": ["JSW STOCK PRICE", "JSW stock price",
                                   "What is the stock price of JSW?"],
                      "responses": [JSW]
                  },
{
                      "tag": "HCL stock",
                      "patterns": ["HCL STOCK PRICE", "HCL stock price",
                                   "What is the stock price of HCL?"],
                      "responses": [HCL]
                  },
{
                      "tag": "SAIL stock",
                      "patterns": ["SAIL STOCK PRICE", "SAIL stock price",
                                   "What is the stock price of SAIL?"],
                      "responses": [SAIL]
                  },
{
                      "tag": "BPCL stock",
                      "patterns": ["BPCL STOCK PRICE", "BPCL stock price",
                                   "What is the stock price of BPCL?"],
                      "responses": [BPCL]
                  },
{
                      "tag": "HERO stock",
                      "patterns": ["HERO MOTORS STOCK PRICE", "Hero Motors stock price",
                                   "What is the stock price of Hero Motors?"],
                      "responses": [HERO]
                  },
{
                      "tag": "WIPRO stock",
                      "patterns": ["WIPRO STOCK PRICE", "WIPRO stock price",
                                   "What is the stock price of WIPRO?"],
                      "responses": [WIPRO]
                  },
{
                      "tag": "CIPLA stock",
                      "patterns": ["CIPLA STOCK PRICE", "CIPLA stock price",
                                   "What is the stock price of CIPLA?"],
                      "responses": [CIPLA]
                  },
{
                      "tag": "AIRTEL stock",
                      "patterns": ["AIRTEL STOCK PRICE", "AIRTEL stock price",
                                   "What is the stock price of AIRTEL?"],
                      "responses": [AIRTEL]
                  },
{
                      "tag": "TITAN stock",
                      "patterns": ["TITAN STOCK PRICE", "TITAN stock price",
                                   "What is the stock price of TITAN?"],
                      "responses": [TITAN]
                  },
{
                      "tag": "KOTAK stock",
                      "patterns": ["KOTAK STOCK PRICE", "KOTAK stock price",
                                   "What is the stock price of KOTAK?"],
                      "responses": [KOTAK]
                  },
{
                      "tag": "L&T stock",
                      "patterns": ["L&T STOCK PRICE", "L&T stock price",
                                   "What is the stock price of L&T?"],
                      "responses": [LT]
                  },
{
                      "tag": "TESLA stock",
                      "patterns": ["TESLA STOCK PRICE", "TESLA stock price",
                                   "What is the stock price of TESLA?"],
                      "responses": [TESLA]
                  },
{
                      "tag": "ADANI stock",
                      "patterns": ["ADANI POWER STOCK PRICE", "ADANI Power stock price",
                                   "What is the stock price of ADANI Power?"],
                      "responses": [ADANI]
                  },
{
                      "tag": "Restaurant Brands International stock",
                      "patterns": ["RESTAURANT BRANDS INTERNATIONAL STOCK PRICE", "Restaurant Brands International stock price",
                                   "What is the stock price of Restaurant Brands International?"],
                      "responses": [BURG]
                  },
{
                      "tag": "McDonalds stock",
                      "patterns": ["MCDONALDS STOCK PRICE", "McDonalds stock price",
                                   "What is the stock price of McDonalds?"],
                      "responses": [MCD]
                  },
{
                      "tag": "YUM Foods stock",
                      "patterns": ["YUM FOODS STOCK PRICE", "YUM Foods stock price",
                                   "What is the stock price of YUM Foods?"],
                      "responses": [YUM]
                  },
{
                      "tag": "Dominos stock",
                      "patterns": ["DOMINOS STOCK PRICE", "Dominos stock price",
                                   "What is the stock price of Dominos?"],
                      "responses": [PHUT]
                  },
{
                      "tag": "Papa Johns stock",
                      "patterns": ["PAPA JOHNS STOCK PRICE", "Papa Johns stock price",
                                   "What is the stock price of Papa Johns?"],
                      "responses": [PAPA]
                  },
{
                      "tag": "Starbucks stock",
                      "patterns": ["STARBUCKS STOCK PRICE", "Starbucks stock price",
                                   "What is the stock price of Starbucks?"],
                      "responses": [STAR]
                  },
{
                      "tag": "NIKE stock",
                      "patterns": ["NIKE STOCK PRICE", "NIKE stock price",
                                   "What is the stock price of NIKE?"],
                      "responses": [NIKE]
                  },
{
                      "tag": "Manchester United stock",
                      "patterns": ["MANCHESTER UNITED STOCK PRICE", "Manchester United stock price",
                                   "What is the stock price of Manchester United?"],
                      "responses": [MANU]
                  },
{
                      "tag": "AMD stock",
                      "patterns": ["AMD STOCK PRICE", "AMD stock price",
                                   "What is the stock price of AMD?"],
                      "responses": [AMD]
                  },
{
                      "tag": "TSM stock",
                      "patterns": ["TSM PRICE", "TSM price",
                                   "What is the stock price of TSM?"],
                      "responses": [TSM]
                  },
{
                      "tag": "VISA stock",
                      "patterns": ["VISA STOCK PRICE", "VISA stock price",
                                   "What is the stock price of VISA?"],
                      "responses": [V]
                  },
{
                      "tag": "BIOCON stock",
                      "patterns": ["BIOCON STOCK PRICE", "BIOCON stock price",
                                   "What is the stock price of BIOCON?"],
                      "responses": [BIOCON]
                  },
{
                      "tag": "NESTLE stock",
                      "patterns": ["NESTLE STOCK PRICE", "NESTLE stock price",
                                   "What is the stock price of NESTLE?"],
                      "responses": [NESTLE]
                  },
{
                      "tag": "MASTERCARD stock",
                      "patterns": ["MASTERCARD STOCK PRICE", "MASTERCARD stock price",
                                   "What is the stock price of MASTERCARD?"],
                      "responses": [MASTERCARD]
                  },
{
                      "tag": "EXXON MOBIL stock",
                      "patterns": ["EXXON MOBIL STOCK PRICE", "EXXON MOBIL stock price",
                                   "What is the stock price of EXXON MOBIL?"],
                      "responses": [EXXON]
                  },
{
                      "tag": "United Health Group stock",
                      "patterns": ["United Health Group STOCK PRICE", "United Health Group stock price",
                                   "What is the stock price of United Health Group?"],
                      "responses": [UNH]
                  },
{
                      "tag": "JP Morgan Chase stock",
                      "patterns": ["JP Morgan Chase STOCK PRICE", "JP Morgan Chase stock price",
                                   "What is the stock price of JP Morgan Chase?"],
                      "responses": [JPM]
                  },
{
                      "tag": "CHEVRON stock",
                      "patterns": ["CHEVRON STOCK PRICE", "CHEVRON stock price",
                                   "What is the stock price of CHEVRON?"],
                      "responses": [CVX]
                  },
{
                      "tag": "BEL stock",
                      "patterns": ["BEL STOCK PRICE", "BEL stock price",
                                   "What is the stock price of BEL?"],
                      "responses": [BEL]
                  },
{
                      "tag": "DLF stock",
                      "patterns": ["DLF STOCK PRICE", "DLF stock price",
                                   "What is the stock price of DLF?"],
                      "responses": [DLF]
                  },
{
                      "tag": "JOHNSON&JOHNSON stock",
                      "patterns": ["JOHNSON&JOHNSON STOCK PRICE", "JOHNSON&JOHNSON stock price",
                                   "What is the stock price of JOHNSON&JOHNSON?"],
                      "responses": [JNJ]
                  },
{
                      "tag": "PROCTER AND GAMBLE stock",
                      "patterns": ["PROCTER AND GAMBLE STOCK PRICE", "PROCTER AND GAMBLE stock price",
                                   "What is the stock price of PROCTER AND GAMBLE?"],
                      "responses": [PG]
                  },
{
                      "tag": "CHEVRON stock",
                      "patterns": ["CHEVRON STOCK PRICE", "CHEVRON stock price",
                                   "What is the stock price of CHEVRON?"],
                      "responses": [CVX]
                  },
{
                      "tag": "SBI stock",
                      "patterns": ["SBI STOCK PRICE", "SBI stock price",
                                   "What is the stock price of SBI?"],
                      "responses": [SBI]
                  },
{
                      "tag": "Apple stock",
                      "patterns": ["APPLE STOCK PRICE", "Apple stock price",
                                   "What is the stock price of Apple?"],
                      "responses": [Apple]
                  },
{
                      "tag": "Apple change",
                      "patterns": ["CHANGE IN APPLE PRICE", "Change in Apple price",
                                   "What is the change in Apple price?"],
                      "responses": [AppleChange]
                  },
{
                      "tag": "Apple Percentage",
                      "patterns": ["Percentage change in Apple",
                                   "What is the percentage change in Apple?"],
                      "responses": [ApplePercentage]
                  },
{
                      "tag": "Netflix stock",
                      "patterns": ["NETFLIX STOCK PRICE", "Netflix stock price",
                                   "What is the stock price of Netflix?"],
                      "responses": [Netflix]
                  },
{
                      "tag": "Netflix change",
                      "patterns": ["CHANGE IN NETFLIX PRICE", "Change in Netflix price",
                                   "What is the change in Netflix price?"],
                      "responses": [NetflixChange]
                  },
{
                      "tag": "Netflix Percentage",
                      "patterns": ["Percentage change in Netflix",
                                   "What is the percentage change in Netflix?"],
                      "responses": [NetflixPercentage]
                  },
{
                      "tag": "Amazon stock",
                      "patterns": ["AMAZON STOCK PRICE", "Amazon stock price",
                                   "What is the stock price of Amazon?"],
                      "responses": [Amazon]
                  },
{
                      "tag": "Amazon change",
                      "patterns": [ "Change in Amazon price",
                                   "What is the change in Amazon price?"],
                      "responses": [AmazonChange]
                  },
{
                      "tag": "Amazon Percentage",
                      "patterns": ["Percentage change in Amazon",
                                   "What is the percentage change in Amazon?"],
                      "responses": [AmazonPercentage]
                  },
{
                      "tag": "Microsoft stock",
                      "patterns": ["MICROSOFT STOCK PRICE", "Microsoft stock price",
                                   "What is the stock price of Microsoft?"],
                      "responses": [Microsoft]
                  },
{
                      "tag": "Microsoft change",
                      "patterns": [ "Change in Microsoft price",
                                   "What is the change in Microsoft price?"],
                      "responses": [MicrosoftChange]
                  },
{
                      "tag": "Microsoft Percentage",
                      "patterns": ["Percentage change in Microsoft",
                                   "What is the percentage change in Microsoft?"],
                      "responses": [MicrosoftPercentage]
                  },
{
                      "tag": "Alphabet stock",
                      "patterns": ["ALPHABET STOCK PRICE", "Alphabet stock price",
                                   "What is the stock price of Alphabet?"],
                      "responses": [Alphabet]
                  },
{
                      "tag": "Alphabet change",
                      "patterns": [ "Change in Alphabet price",
                                   "What is the change in Alphabet price?"],
                      "responses": [AlphabetChange]
                  },
{
                      "tag": "Alphabet Percentage",
                      "patterns": ["Percentage change in Alphabet",
                                   "What is the percentage change in Alphabet?"],
                      "responses": [AlphabetPercentage]
                  },
{
                      "tag": "Meta stock",
                      "patterns": ["META STOCK PRICE", "Meta stock price",
                                   "What is the stock price of Meta?"],
                      "responses": [Meta]
                  },
{
                      "tag": "Meta change",
                      "patterns": [ "Change in Meta price",
                                   "What is the change in Meta price?"],
                      "responses": [MetaChange]
                  },
{
                      "tag": "Meta Percentage",
                      "patterns": ["Percentage change in Meta",
                                   "What is the percentage change in Meta?"],
                      "responses": [MetaPercentage]
                  },
{
                      "tag": "NVIDIA stock",
                      "patterns": ["NVIDIA STOCK PRICE", "NVIDIA stock price",
                                   "What is the stock price of NVIDIA?"],
                      "responses": [Nvidia]
                  },
{
                      "tag": "NVIDIA change",
                      "patterns": [ "Change in NVIDIA price",
                                   "What is the change in NVIDIA price?"],
                      "responses": [NvidiaChange]
                  },
{
                      "tag": "NVIDIA Percentage",
                      "patterns": ["Percentage change in NVIDIA",
                                   "What is the percentage change in NVIDIA?"],
                      "responses": [NvidiaPercentage]
                  }
                  ]}


with open('intents.json','w') as _f:
    json.dump(dict,_f)

