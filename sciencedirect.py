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
# driver.get(JOURNAL_URL)
# contents = driver.page_source

contents = '''
<div id="0-accordion-panel-7" class="accordion-panel-content u-padding-s-ver js-accordion-panel-content" aria-labelledby="0-accordion-tab-7"><section class="js-issue-list-content"><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/244/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 244, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 339-674 (16 July 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/244/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 244, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-338 (1 July 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/243/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 243, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 683-1028 (16 June 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/243/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 243, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 345-682 (1 June 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/243/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 243, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-344 (16 May 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/242/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 242, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 693-1038 (1 May 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/242/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 242, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 347-692 (16 April 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/242/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 242, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-346 (1 April 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/241/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 241, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 583-936 (16 March 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/241/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 241, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 283-582 (1 March 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/241/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 241, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-282 (16 February 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/240/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 240, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 603-912 (1 February 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/240/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 240, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 305-602 (16 January 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/240/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 240, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-304 (1 January 2015)</h3></span></div></section></div>
'''
# response = requests.get(JOURNAL_URL)
print("Parse is Ended")
soup = BeautifulSoup(contents, 'html.parser')

journal_name = 'European Journal of Operation Research'
# current_dir = os.getcwd()

current_dir = 'E://Book/Journals'
output_folder = current_dir + "/" + journal_name

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

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

    output_folder = current_dir + "/" + journal_name  + "/" + title

    output_folder = output_folder.strip()
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
