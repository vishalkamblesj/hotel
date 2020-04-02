from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("C:/webdrivers/chromedriver")
products=[]
prices=[]
driver.get("https://www.makemytrip.com/hotels/hotel-listing/?checkin=04012020&checkout=04022020&locusId=CTXDB&locusType=city&city=CTXDB&country=IN&searchText=Hubli%2C%20India&roomStayQualifier=2e0e&_uCurrency=INR&reference=hotel&type=city")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('div', attrs={'class':'makeFlex spaceBetween'}):
    name=a.find('p', attrs={'class':'latoBlack font22 blackText appendBottom12'})
    #price=a.find('div', attrs={'class':'latoBlack font26 blackText appendBottom5'})
    products.append(name.text)
    #prices.append(price.text)
for a in soup.findAll('div', attrs={'class':'padding20 makeFlex column'}):
    #name=a.find('div', attrs={'class':'latoBlack font22 blackText appendBottom12'})
    price=a.find('p', attrs={'class':'latoBlack font26 blackText appendBottom5'})
    #products.append(name.text)
    prices.append(price.text)
df = pd.DataFrame({'Hotel Name':products,'Price':prices}) 
df.to_csv('Hotels.csv', index=False, encoding='utf-8')
