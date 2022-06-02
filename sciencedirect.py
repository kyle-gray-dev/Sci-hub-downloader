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
<div id="0-accordion-panel-1" class="accordion-panel-content u-padding-s-ver js-accordion-panel-content" aria-labelledby="0-accordion-tab-1"><section class="js-issue-list-content"><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/295/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 295, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 807-1226 (16 December 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/295/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 295, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 399-806 (1 December 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/295/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 295, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-398 (16 November 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/294/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 294, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 817-1212 (1 November 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/294/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 294, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 405-816 (16 October 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/294/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 294, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-404 (1 October 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/293/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 293, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 809-1206 (16 September 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/293/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 293, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 401-808 (1 September 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/293/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 293, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-400 (16 August 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/292/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 292, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 799-1210 (1 August 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/292/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 292, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 397-798 (16 July 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/292/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 292, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-396 (1 July 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/291/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 291, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 807-1212 (16 June 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/291/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 291, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 411-806 (1 June 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/291/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 291, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-410 (16 May 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/290/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 290, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 807-1206 (1 May 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/290/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 290, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 405-806 (16 April 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/290/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 290, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-404 (1 April 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/289/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 289, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 807-1222 (16 March 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/289/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 289, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 399-806 (1 March 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/289/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 289, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-398 (16 February 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/288/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 288, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 703-1084 (1 February 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/288/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 288, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 361-702 (16 January 2021)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/european-journal-of-operational-research/vol/288/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 288, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-360 (1 January 2021)</h3></span></div></section></div>
'''
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
