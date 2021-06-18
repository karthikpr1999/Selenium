import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

def LinkGenerator(link):
  return (link) 
    
def CompanyList(soup):
    company = soup.find('tbody').find_all('a')
    Cname =[]
    Clink =[]
    for detail in company:
        Cname.append(detail.text.strip())
        Clink.append(detail.get('href'))
    return (Cname,Clink)

browser = webdriver.Chrome(r"C:\chromedriver.exe")
for i in range(551,679):
    browser.get('https://www.zaubacorp.com/company-list/age-A/roc-RoC-Kanpur/p-'+str(i)+'-company.html')
    soup = BeautifulSoup(browser.page_source,'lxml')
    Cname,Clink = CompanyList(soup) 
    df= pd.DataFrame({'Company Name ':Cname, 'Link':Clink})
    d1= pd.DataFrame({'Company Name ':Cname})
    df0 = pd.DataFrame({key:pd.Series(value) for key,value in d1.items()})  
    df0.to_csv('Company_name.csv',mode = 'a',header= False)
    for i in range(0,30):
        ProperLink = LinkGenerator(df.iloc[i,1])
        browser.get(ProperLink)
        soup = BeautifulSoup(browser.page_source,'lxml')
        des = soup.text
        email = []
        try:
            reg= '[a-z0-9]+[@]\w+[.]\w+'
            Email = re.search(reg,des).group()
            email.append(Email)
        except AttributeError:
            Email = re.match("^.*(?=(\())",des)
        d = {'Email': email}  
        df1 = pd.DataFrame({key:pd.Series(value) for key,value in d.items()})
        df1.to_csv("Company_email.csv",mode = 'a',header = False)


csv1 = pd.read_csv('Company_name.csv',)
csv2 = pd.read_csv('Company_email.csv')

merged = csv1.merge(csv2, on = 'Company Name')

merged.to_excel('Company_name_email-1.xlsx',index = False)