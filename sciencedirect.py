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
<div id="0-accordion-panel-6" class="accordion-panel-content u-padding-s-ver js-accordion-panel-content" aria-labelledby="0-accordion-tab-6"><section class="js-issue-list-content"><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/76/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 76&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-238 (December 2016)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/75/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 75&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-230 (November 2016)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/74/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 74&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-228 (October 2016)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/73/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 73&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-174 (September 2016)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/72/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 72&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-214 (August 2016)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/71/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 71&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-164 (July 2016)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/70/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 70&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-180 (June 2016)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/69/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 69&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-126 (May 2016)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/68/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 68&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-134 (April 2016)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/67/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 67&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-216 (March 2016)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/66/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 66&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-444 (February 2016)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/65/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 65&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-200 (January 2016)</h3></span></div></section></div>
<div id="0-accordion-panel-7" class="accordion-panel-content u-padding-s-ver js-accordion-panel-content" aria-labelledby="0-accordion-tab-7"><section class="js-issue-list-content"><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/64/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 64&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-304 (December 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/63/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 63&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-186 (November 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/62/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 62&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-356 (October 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/61/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 61&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-178 (September 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/60/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 60&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-170 (August 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/59/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 59&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-144 (July 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/58/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 58&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-100 (June 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/57/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 57&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-138 (May 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/56/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 56&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-150 (April 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/55/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 55&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-240 (March 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/54/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 54&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-302 (February 2015)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m" href="/journal/computers-and-operations-research/vol/53/suppl/C" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 53&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-364 (January 2015)</h3></span></div></section></div>

'''
# response = requests.get(JOURNAL_URL)
print("Parse is Ended")
soup = BeautifulSoup(contents, 'html.parser')

journal_name = 'Computational Optimization and Applications'
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
