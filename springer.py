import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import os
from time import sleep
from sci_hub_pdf import download_pdf


JOURNAL_BASE_URL = 'https://link.springer.com'
JOURNAL_URL = f"{JOURNAL_BASE_URL}/journal/10288/volumes-and-issues"
response = requests.get(JOURNAL_URL)

driver = webdriver.Chrome('./chromedriver.exe')
soup = BeautifulSoup(response.content, 'html.parser')

journal_name = '4OR'
# current_dir = os.getcwd()

current_dir = 'E://Book/Journals'
output_folder = current_dir + "/" + journal_name

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# print(soup)
for link in soup.select('li.app-section .c-list-group__item a'):
    href = link['href']
    if "59" in href:
        break 

    href = JOURNAL_BASE_URL + href
    print(href)

    sleep(0.1)

    response = requests.get(href)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.select_one('.app-volumes-and-issues__info h1').contents[0]
    print(title)

    output_folder = current_dir + "/" + journal_name  + "/" + title
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    sleep(0.1)

    for link in soup.select('h3.c-card__title a'):
        href = link['href']
        title = link.contents[0]

        # get doi
        doi = href.replace("https://link.springer.com/article/", "")
        doi = doi.strip()
        print(doi, title)

        count = 0
        while True:
            if download_pdf(doi, output_folder, title, driver):
                break

            count = count + 1
            sleep(30)
            if count > 5:
                break

        sleep(0.5)


    