import numpy as np
import pandas as pd
import requests
from selenium import webdriver
from datetime import date 

browser = webdriver.Chrome("C:\chromedriver.exe")
browser.get('https://www.moneycontrol.com/indian-indices/nifty-50-9.html')
oprice = browser.find_element_by_id('sp_open').text
previous_price = browser.find_element_by_id('sp_previousclose').text
day_low = browser.find_element_by_id('sp_Low').text
day_high = browser.find_element_by_id('sp_High').text
yr_low = browser.find_element_by_id('sp_yrlow').text
yr_high = browser.find_element_by_id('sp_yrhigh').text

df = pd.DataFrame({'Date':date.today(),
    'Open price':oprice,
    'Previous price': previous_price,
    'DayLow':day_low,'DayHigh':day_high,
    '52WeekLow':yr_low,'52WeekHigh':yr_high
    },
    index = [0] 
)

df.to_csv("NSE_details.csv",mode = 'a',header= False)  