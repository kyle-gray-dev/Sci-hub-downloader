import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from time import sleep
from sci_hub_pdf import download_pdf

JOURNAL_BASE_URL = 'https://onlinelibrary.wiley.com'
JOURNAL_URL = f"{JOURNAL_BASE_URL}/loi/10970037"
print(JOURNAL_URL)

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome('./chromedriver.exe', options=options)
# driver.get(JOURNAL_URL)
# contents = driver.page_source

contents = '''
<ul class="rlist loi__list"><li class=" active "><a href="/loi/10970037/year/2022" title="2022 - Volume 79 - 80"><span class="loi-tab-item">2022 - Volume 79 - 80</span></a></li><li><a href="/loi/10970037/year/2021" title="2021 - Volume 77 - 78"><span class="loi-tab-item">2021 - Volume 77 - 78</span></a></li><li><a href="/loi/10970037/year/2020" title="2020 - Volume 75 - 76"><span class="loi-tab-item">2020 - Volume 75 - 76</span></a></li><li class=" nested "><div class="expandable-list js--open"><a href="#" data-toggle="dropdown" aria-expanded="false" title="2010 - 2019" class="expandable-list__toggle"><i aria-hidden="true" class="icon-squared-minus"></i><span class="loi-tab-item">2010 - 2019</span></a><ul id="2010-2019" aria-hidden="false" class="rlist expandable-list__body" style=""><li><a href="/loi/10970037/year/2019" title="2019 - Volume 73 - 74"><span class="loi-tab-item">2019 - Volume 73 - 74</span></a></li><li><a href="/loi/10970037/year/2018" title="2018 - Volume 71 - 72"><span class="loi-tab-item">2018 - Volume 71 - 72</span></a></li><li><a href="/loi/10970037/year/2017" title="2017 - Volume 69 - 70"><span class="loi-tab-item">2017 - Volume 69 - 70</span></a></li><li><a href="/loi/10970037/year/2016" title="2016 - Volume 67 - 68"><span class="loi-tab-item">2016 - Volume 67 - 68</span></a></li><li><a href="/loi/10970037/year/2015" title="2015 - Volume 65 - 66"><span class="loi-tab-item">2015 - Volume 65 - 66</span></a></li><li><a href="/loi/10970037/year/2014" title="2014 - Volume 63 - 64"><span class="loi-tab-item">2014 - Volume 63 - 64</span></a></li><li><a href="/loi/10970037/year/2013" title="2013 - Volume 61 - 62"><span class="loi-tab-item">2013 - Volume 61 - 62</span></a></li><li><a href="/loi/10970037/year/2012" title="2012 - Volume 59 - 60"><span class="loi-tab-item">2012 - Volume 59 - 60</span></a></li><li><a href="/loi/10970037/year/2011" title="2011 - Volume 57 - 58"><span class="loi-tab-item">2011 - Volume 57 - 58</span></a></li><li><a href="/loi/10970037/year/2010" title="2010 - Volume 55 - 56"><span class="loi-tab-item">2010 - Volume 55 - 56</span></a></li></ul></div></li><li class=" nested "><div class="expandable-list"><a href="#" data-toggle="dropdown" aria-expanded="false" title="2000 - 2009" class="expandable-list__toggle"><i aria-hidden="true" class="icon-add_box"></i><span class="loi-tab-item">2000 - 2009</span></a><ul id="2000-2009" aria-hidden="true" class="rlist expandable-list__body" style="display: none;"><li><a href="/loi/10970037/year/2009" title="2009 - Volume 53 - 54"><span class="loi-tab-item">2009 - Volume 53 - 54</span></a></li><li><a href="/loi/10970037/year/2008" title="2008 - Volume 51 - 52"><span class="loi-tab-item">2008 - Volume 51 - 52</span></a></li><li><a href="/loi/10970037/year/2007" title="2007 - Volume 49 - 50"><span class="loi-tab-item">2007 - Volume 49 - 50</span></a></li><li><a href="/loi/10970037/year/2006" title="2006 - Volume 47 - 48"><span class="loi-tab-item">2006 - Volume 47 - 48</span></a></li><li><a href="/loi/10970037/year/2005" title="2005 - Volume 45 - 46"><span class="loi-tab-item">2005 - Volume 45 - 46</span></a></li><li><a href="/loi/10970037/year/2004" title="2004 - Volume 43 - 44"><span class="loi-tab-item">2004 - Volume 43 - 44</span></a></li><li><a href="/loi/10970037/year/2003" title="2003 - Volume 41 - 42"><span class="loi-tab-item">2003 - Volume 41 - 42</span></a></li><li><a href="/loi/10970037/year/2002" title="2002 - Volume 39 - 40"><span class="loi-tab-item">2002 - Volume 39 - 40</span></a></li><li><a href="/loi/10970037/year/2001" title="2001 - Volume 37 - 38"><span class="loi-tab-item">2001 - Volume 37 - 38</span></a></li><li><a href="/loi/10970037/year/2000" title="2000 - Volume 35 - 36"><span class="loi-tab-item">2000 - Volume 35 - 36</span></a></li></ul></div></li><li class=" nested "><div class="expandable-list"><a href="#" data-toggle="dropdown" aria-expanded="false" title="1990 - 1999" class="expandable-list__toggle"><i aria-hidden="true" class="icon-add_box"></i><span class="loi-tab-item">1990 - 1999</span></a><ul id="1990-1999" aria-hidden="true" class="rlist expandable-list__body" style="display: none;"><li><a href="/loi/10970037/year/1999" title="1999 - Volume 33 - 34"><span class="loi-tab-item">1999 - Volume 33 - 34</span></a></li><li><a href="/loi/10970037/year/1998" title="1998 - Volume 31 - 32"><span class="loi-tab-item">1998 - Volume 31 - 32</span></a></li><li><a href="/loi/10970037/year/1997" title="1997 - Volume 29 - 30"><span class="loi-tab-item">1997 - Volume 29 - 30</span></a></li><li><a href="/loi/10970037/year/1996" title="1996 - Volume 27 - 28"><span class="loi-tab-item">1996 - Volume 27 - 28</span></a></li><li><a href="/loi/10970037/year/1995" title="1995 - Volume 25 - 26"><span class="loi-tab-item">1995 - Volume 25 - 26</span></a></li><li><a href="/loi/10970037/year/1994" title="1994 - Volume 24"><span class="loi-tab-item">1994 - Volume 24</span></a></li><li><a href="/loi/10970037/year/1993" title="1993 - Volume 23"><span class="loi-tab-item">1993 - Volume 23</span></a></li><li><a href="/loi/10970037/year/1992" title="1992 - Volume 22"><span class="loi-tab-item">1992 - Volume 22</span></a></li><li><a href="/loi/10970037/year/1991" title="1991 - Volume 21"><span class="loi-tab-item">1991 - Volume 21</span></a></li><li><a href="/loi/10970037/year/1990" title="1990 - Volume 20"><span class="loi-tab-item">1990 - Volume 20</span></a></li></ul></div></li><li class=" nested "><div class="expandable-list"><a href="#" data-toggle="dropdown" aria-expanded="false" title="1980 - 1989" class="expandable-list__toggle"><i aria-hidden="true" class="icon-add_box"></i><span class="loi-tab-item">1980 - 1989</span></a><ul id="1980-1989" aria-hidden="true" class="rlist expandable-list__body" style="display: none;"><li><a href="/loi/10970037/year/1989" title="1989 - Volume 19"><span class="loi-tab-item">1989 - Volume 19</span></a></li><li><a href="/loi/10970037/year/1988" title="1988 - Volume 18"><span class="loi-tab-item">1988 - Volume 18</span></a></li><li><a href="/loi/10970037/year/1987" title="1987 - Volume 17"><span class="loi-tab-item">1987 - Volume 17</span></a></li><li><a href="/loi/10970037/year/1986" title="1986 - Volume 16"><span class="loi-tab-item">1986 - Volume 16</span></a></li><li><a href="/loi/10970037/year/1985" title="1985 - Volume 15"><span class="loi-tab-item">1985 - Volume 15</span></a></li><li><a href="/loi/10970037/year/1984" title="1984 - Volume 14"><span class="loi-tab-item">1984 - Volume 14</span></a></li><li><a href="/loi/10970037/year/1983" title="1983 - Volume 13"><span class="loi-tab-item">1983 - Volume 13</span></a></li><li><a href="/loi/10970037/year/1982" title="1982 - Volume 12"><span class="loi-tab-item">1982 - Volume 12</span></a></li><li><a href="/loi/10970037/year/1981" title="1981 - Volume 11"><span class="loi-tab-item">1981 - Volume 11</span></a></li><li><a href="/loi/10970037/year/1980" title="1980 - Volume 10"><span class="loi-tab-item">1980 - Volume 10</span></a></li></ul></div></li><li class=" nested "><div class="expandable-list"><a href="#" data-toggle="dropdown" aria-expanded="false" title="1970 - 1979" class="expandable-list__toggle"><i aria-hidden="true" class="icon-add_box"></i><span class="loi-tab-item">1970 - 1979</span></a><ul id="1970-1979" aria-hidden="true" class="rlist expandable-list__body" style="display: none;"><li><a href="/loi/10970037/year/1979" title="1979 - Volume 9"><span class="loi-tab-item">1979 - Volume 9</span></a></li><li><a href="/loi/10970037/year/1978" title="1978 - Volume 8"><span class="loi-tab-item">1978 - Volume 8</span></a></li><li><a href="/loi/10970037/year/1977" title="1977 - Volume 7"><span class="loi-tab-item">1977 - Volume 7</span></a></li><li><a href="/loi/10970037/year/1976" title="1976 - Volume 6"><span class="loi-tab-item">1976 - Volume 6</span></a></li><li><a href="/loi/10970037/year/1975" title="1975 - Volume 5"><span class="loi-tab-item">1975 - Volume 5</span></a></li><li><a href="/loi/10970037/year/1974" title="1974 - Volume 4"><span class="loi-tab-item">1974 - Volume 4</span></a></li><li><a href="/loi/10970037/year/1973" title="1973 - Volume 3"><span class="loi-tab-item">1973 - Volume 3</span></a></li><li><a href="/loi/10970037/year/1972" title="1972 - Volume 2"><span class="loi-tab-item">1972 - Volume 2</span></a></li><li><a href="/loi/10970037/year/1971" title="1971 - Volume 1"><span class="loi-tab-item">1971 - Volume 1</span></a></li></ul></div></li></ul>

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

for link in soup.select('ul > li > a'):
    href = link['href']

    if "2014" in href:
        break 

    href = JOURNAL_BASE_URL + href
    print(href)

    # response = requests.get(href)
    driver.get(href)
    contents = driver.page_source
    soup = BeautifulSoup(contents, 'html.parser')

    for link in soup.select(".parent-item a"):
        href = link['href']
        title = link.contents[0]

        output_folder = current_dir + "/" + journal_name  + "/" + title

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

        for link in soup.select(".issue-item__title"):
            href  = link["href"]
            title = link.select_one('h2').contents[0]
            
            # get doi
            doi = href.replace("/doi/", "")

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
