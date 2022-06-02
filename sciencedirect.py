import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from time import sleep
from sci_hub_pdf import download_pdf

JOURNAL_BASE_URL = 'https://www.sciencedirect.com'
JOURNAL_URL = f"{JOURNAL_BASE_URL}/journal/european-journal-of-operational-research/issues"
print(JOURNAL_URL)

driver = webdriver.Chrome('./chromedriver.exe')
driver.get(JOURNAL_URL)
contents = driver.page_source
# response = requests.get(JOURNAL_URL)
print("Parse is Ended")
soup = BeautifulSoup(contents, 'html.parser')

current_dir = os.getcwd()
output_folder = current_dir + "/pdfs"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

if 'js-issue-item-link' in contents:
    print("exists")

for link in soup.select('a.js-issue-item-link'):
    href = link['href']
    if "240" in href:
        break 

    href = JOURNAL_BASE_URL + href
    print(href)

    # response = requests.get(href)
    driver.get(href)
    contents = driver.page_source
    soup = BeautifulSoup(contents, 'html.parser')
    
    title = soup.select_one('.js-vol-issue').contents[0]
    print(title)


    output_folder = current_dir + "/pdfs/" + title
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    sleep(0.1)

    for link in soup.select('a.article-content-title'):
        href = link['href']

        title  = link.select_one('.js-article-title').contents[0]

        href = JOURNAL_BASE_URL + href

        # response = requests.get(href)
        driver.get(href)
        contents = driver.page_source
        soup = BeautifulSoup(contents, 'html.parser')

        href  = soup.select_one('a.doi').contents[0]

        # get doi
        doi = href.replace("https://doi.org/", "")
        doi = doi.strip()
        print(doi, title)

        count = 0
        while True:
            if download_pdf(doi, output_folder, title):
                break

            count = count + 1
            sleep(30)
            if count > 20:
                break

        sleep(0.5)

    # break
