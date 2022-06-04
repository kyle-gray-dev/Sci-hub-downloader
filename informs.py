import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from time import sleep
from sci_hub_pdf import download_pdf

JOURNAL_BASE_URL = 'https://pubsonline.informs.org'

driver = webdriver.Chrome('./chromedriver.exe')
# driver.get(JOURNAL_URL)
# contents = driver.page_source

contents = '''
<ul role="tablist" class="rlist loi__list tab__nav swipe__list" style="width: 227.156px;"><li role="presentation" class="tab__nav__item active"><a href="/loi/moor/group/d2020.y2022" data-url="d2020.y2022" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2020-y2022" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2020-y2022" role="tab" data-toggle="tab" title="2022" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2020-y2022con" aria-selected="true" class="tab__nav__item__link" tabindex="0">2022</a></li><li role="presentation" class="tab__nav__item"><a href="/loi/moor/group/d2020.y2021" data-url="d2020.y2021" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2020-y2021" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2020-y2021" role="tab" data-toggle="tab" title="2021" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2020-y2021con" aria-selected="true" class="tab__nav__item__link" tabindex="0">2021</a></li><li role="presentation" class="tab__nav__item"><a href="/loi/moor/group/d2020.y2020" data-url="d2020.y2020" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2020-y2020" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2020-y2020" role="tab" data-toggle="tab" title="2020" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2020-y2020con" aria-selected="true" class="tab__nav__item__link" tabindex="0">2020</a></li></ul>
<ul role="tablist" class="rlist loi__list tab__nav swipe__list" style="width: 652.188px;"><li role="presentation" class="tab__nav__item active"><a href="/loi/moor/group/d2010.y2019" data-url="d2010.y2019" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2019" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2019" role="tab" data-toggle="tab" title="2019" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2019con" aria-selected="false" class="tab__nav__item__link" tabindex="-1">2019</a></li><li role="presentation" class="tab__nav__item"><a href="/loi/moor/group/d2010.y2018" data-url="d2010.y2018" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2018" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2018" role="tab" data-toggle="tab" title="2018" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2018con" aria-selected="false" class="tab__nav__item__link" tabindex="-1">2018</a></li><li role="presentation" class="tab__nav__item"><a href="/loi/moor/group/d2010.y2017" data-url="d2010.y2017" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2017" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2017" role="tab" data-toggle="tab" title="2017" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2017con" aria-selected="false" class="tab__nav__item__link" tabindex="-1">2017</a></li><li role="presentation" class="tab__nav__item"><a href="/loi/moor/group/d2010.y2016" data-url="d2010.y2016" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2016" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2016" role="tab" data-toggle="tab" title="2016" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2016con" aria-selected="false" class="tab__nav__item__link" tabindex="-1">2016</a></li><li role="presentation" class="tab__nav__item"><a href="/loi/moor/group/d2010.y2015" data-url="d2010.y2015" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2015" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2015" role="tab" data-toggle="tab" title="2015" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2015con" aria-selected="false" class="tab__nav__item__link" tabindex="-1">2015</a></li><li role="presentation" class="tab__nav__item"><a href="/loi/moor/group/d2010.y2014" data-url="d2010.y2014" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2014" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2014" role="tab" data-toggle="tab" title="2014" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2014con" aria-selected="false" class="tab__nav__item__link" tabindex="-1">2014</a></li><li role="presentation" class="tab__nav__item"><a href="/loi/moor/group/d2010.y2013" data-url="d2010.y2013" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2013" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2013" role="tab" data-toggle="tab" title="2013" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2013con" aria-selected="false" class="tab__nav__item__link" tabindex="-1">2013</a></li><li role="presentation" class="tab__nav__item"><a href="/loi/moor/group/d2010.y2012" data-url="d2010.y2012" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2012" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2012" role="tab" data-toggle="tab" title="2012" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2012con" aria-selected="false" class="tab__nav__item__link" tabindex="-1">2012</a></li><li role="presentation" class="tab__nav__item"><a href="/loi/moor/group/d2010.y2011" data-url="d2010.y2011" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2011" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2011" role="tab" data-toggle="tab" title="2011" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2011con" aria-selected="false" class="tab__nav__item__link" tabindex="-1">2011</a></li><li role="presentation" class="tab__nav__item"><a href="/loi/moor/group/d2010.y2010" data-url="d2010.y2010" data-target="#pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2010" aria-controls="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2010" role="tab" data-toggle="tab" title="2010" id="pane-7e0c2fff-3030-4398-9bd9-97267d30047c-d2010-y2010con" aria-selected="false" class="tab__nav__item__link" tabindex="-1">2010</a></li></ul>

'''
# response = requests.get(JOURNAL_URL)
print("Parse is Ended")
soup = BeautifulSoup(contents, 'html.parser')

current_dir = os.getcwd()
output_folder = current_dir + "/pdfs"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for link in soup.select('a.tab__nav__item__link'):
    href = link['href']

    if 'y2014' in href:
        break

    href = JOURNAL_BASE_URL + href
    print(href)


    driver.get(href)
    contents = driver.page_source
    soup = BeautifulSoup(contents, 'html.parser')

    for link in soup.select('.issue-info__vol-issue'):   
        href = link["href"] 
        title = link.contents[0]


        output_folder = current_dir + "/pdfs/" + title
        output_folder = output_folder.strip()
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

        sleep(0.1)

        href = JOURNAL_BASE_URL + href

        print(href, title)

        # response = requests.get(href)
        driver.get(href)
        contents = driver.page_source
        soup = BeautifulSoup(contents, 'html.parser')

        for link in soup.select(".issue-item__title a"):
            href  = link["href"]
            title = link.contents[0]

            # get doi
            doi = href.replace("/doi/abs/", "")
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
