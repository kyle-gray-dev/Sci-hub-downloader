# from random import randint
# from time import sleep
# import requests
# from bs4 import BeautifulSoup as soup
# import pandas as pd

# import asyncio
# from pyppeteer import launch
# import time

# async def get_details(page, resturant_link):
#     print(resturant_link)
#     headers1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
#     # html1 = requests.get(resturant_link,headers=headers1)

#     await page.goto(resturant_link)
#     time.sleep(1000)
#     # await asyncio.sleep(2)


#     # lunch_chk = await page.waitForSelector('[data-automation="checkbox"] #checkbox_43')
#     # if lunch_chk:
#     #     lunch_chk.click()

#     # content = page.content()


#     # bsobj1 = soup(html1.text,"html.parser")
#     # bsobj1 = soup(response.text(), "html.parser")
    
#     # temp = bsobj1.find('div',string="PRICE RANGE")
#     # price_range = None
#     # if temp:
#     #     parent = temp.parent
#     #     price_range = parent.findAll('div')[1].text
#     # cuisines = None
#     # temp = bsobj1.find('div',string="CUISINES")
#     # if temp:
#     #     parent = temp.parent
#     #     cuisines = parent.findAll('div')[1].text
    
#     # address = None
#     # address = bsobj1.find('span',{'class':'yEWoV'})
#     # if address:
#     #     address = address.text

#     # print("address", address)
#     # return price_range, cuisines, address



# async def filter_by_category():
#     browser = await launch(
#     {
#         "headless": False,
#         'args':['--start-maximized'],
#         # 'executablePath':'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
#         # 'executablePath':'H:\\Work\\Sci-hub-downloader'
#     }
#     )

#     page = await browser.newPage()
#     await page.setViewport({'width': 1920, 'height': 1080})

#     abc = "https://www.tripadvisor.com.sg/Restaurants-g188590-Amsterdam_North_Holland_Province.html"
    

#     await get_details(page, abc)

# asyncio.get_event_loop().run_until_complete(filter_by_category())
    
# import requests

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

import requests
from bs4 import BeautifulSoup as soup

def get_details(resturant_link):        
    headers1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    html1 = requests.get(resturant_link,headers=headers1)

    bsobj1 = soup(html1.text,"html.parser")
    
    temp = bsobj1.find('div',string="PRICE RANGE")
    price_range = None
    if temp:
        parent = temp.parent
        price_range = parent.findAll('div')[1].text

    print("price_range", price_range)
    

    cuisines = None
    temp = bsobj1.find('div',string="CUISINES")
    if temp:
        parent = temp.parent
        cuisines = parent.findAll('div')[1].text

    print("cuisines", cuisines)
    
    address = None
    address = bsobj1.find('span',{'class':'yEWoV'})
    if address:
        address = address.text

    print("address", address)
    return price_range, cuisines, address

chrome_options = ChromiumOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(chrome_options=chrome_options, service=service)
# driver.maximize_window()

JOURNAL_URL = f"https://www.tripadvisor.com.sg/Restaurants-g188590-Amsterdam_North_Holland_Province.html"
print(JOURNAL_URL)

driver.get(JOURNAL_URL)
print("get finished")
time.sleep(5)

# lunch_checkbox = driver.find_element(By.CSS_SELECTOR, '#checkbox_43')
lunch_checkbox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkbox_43')))

driver.execute_script("arguments[0].click();", lunch_checkbox) 
print("end")

for i in range(5):
    print("page =", i + 1)
    time.sleep(5)

    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.Lwqic")))
    links = driver.find_elements(By.CSS_SELECTOR, "a.Lwqic")

    print("count =", len(links))


    for link in links:
        href = link.get_attribute("href")
        print(href)

        get_details(href)

    # go to next
    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.Lwqic")))
    next_a = driver.find_element(By.CSS_SELECTOR, "div.pagination a.next")
    next_a.click()

# get_details("https://www.tripadvisor.com.sg/Restaurant_Review-g188590-d25207519-Reviews-Mangia_Pasta_Bar-Amsterdam_North_Holland_Province.html")

time.sleep(1000)

