import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


def LinkGenerator(link):
  return ('https://www.infoqik.com/'+link) 

# company name extractor based on state
def StateWiseCompany(soup):
  CompanyList = soup.find_all('div',{'class':'my-3 p-3 bg-white rounded shadow-sm'})
  data =  CompanyList[1].find_all('a')

  Cname =[]
  Clink =[]
  for detail in data:
      Cname.append(detail.text.strip())
      Clink.append(detail.get('href'))
  return (Cname,Clink)

# Input dataframe of company name and link for company page discription
def CompanyEmailExtractor(df):
  email = []    
  for i in range(0,25): # 25 no of company list on single page
      ProperLink = LinkGenerator(df.iloc[i,1])
      browser.get(ProperLink)
      soup = BeautifulSoup(browser.page_source,'lxml')
      ComDiscription = soup.find('div',{'class':'my-3 p-3 bg-white rounded shadow-sm'}).text.strip()
      try:
        reg= '[a-z0-9]+[@]\w+[.]\w+'
        Email = re.search(reg,ComDiscription).group()
        email.append(Email)
      except AttributeError:
        Email = re.match("^.*(?=(\())", ComDiscription)
  return email


#============Main Program ======================================
browser = webdriver.Chrome("C:\chromedriver.exe")
for i in range(1,2):
  browser.get('https://www.infoqik.com/companies/tamil-nadu/registered-list-'+str(i)+'.html')
  soup = BeautifulSoup(browser.page_source,'lxml')  
  Cname,Clink = StateWiseCompany(soup)
  df= pd.DataFrame({'Company Name ':Cname, 'Link':Clink})
  email = CompanyEmailExtractor(df)
  d = {'Company Name':Cname,'Email':email}    
  df1 = pd.DataFrame({key:pd.Series(value) for key,value in d.items()})    
  df1.to_csv("Sample.csv",mode = 'a',header= False) # mode ='a' to append excel
 
