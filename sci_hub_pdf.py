import requests
from bs4 import BeautifulSoup
import os
from time import sleep
from win10toast import ToastNotifier
import urllib.request as urllib2

toaster = ToastNotifier()

# https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&highlight=true&returnType=SEARCH&matchPubs=true&ranges=2020._2022_Year&returnFacets=ALL&rowsPerPage=100

BASE_URL = "https://sci-hub.se/"

def download_pdf(doi, output_folder, title, driver=None):
    title = str(title)
    doi = str(doi)
    
    try:
        if '<' in title and '>' in title:
            title = doi
        # title = '<span class="smallCaps">M</span>'

        # check file path
        filepath = output_folder + '/' + title.replace('/', '-').replace(':', ' ').replace('?', '') + '.pdf'

        if os.path.exists(filepath):        
            filesize = os.path.getsize(filepath)
            if filesize > 3000:
                print("File Exists Skipped", filepath)
                return True

        doi = doi.strip()

        count = 0

        while True:
            if count > 200:
                return True

            contents = ""
            if driver is not None:
                driver.get(BASE_URL + doi)
                contents = driver.page_source
            else:
                response = requests.get(BASE_URL + doi)
                contents = response.content
            
            soup = BeautifulSoup(contents, 'html.parser')
            smile = soup.select_one('#smile')
            if smile is not None:
                print("PDF not exist", doi, title)
                return True

            # loading_ani = soup.select_one('#link-ddg')
            # if loading_ani is not None:
            #     print("PDF not exist", doi, title)
            #     return True

            content = soup.find('embed').get('src').replace('#navpanes=0&view=FitH', '').replace('//', '/')
            if content.startswith('/downloads'):
                pdf = BASE_URL + content
            elif content.startswith('/tree'):
                pdf = BASE_URL + content
            elif content.startswith('/uptodate'):
                pdf = BASE_URL + content
            else:
                pdf = 'https:/' + content

            r = requests.get(pdf, stream=True)
            
            if len(r.content) < 250:
                print("Cannot find file", len(r.content), title)

                return True
            
            if len(r.content) < 3000: # captch                
                toaster.show_toast("Sci-Hub Capcha", title, threaded=True,
                   icon_path=None, duration=10)

                print("Cannot solve captcha", len(r.content), title)

                count += 1
                sleep(120)
                continue

            try:
                with open(filepath, 'wb') as file:
                    file.write(r.content)

            except Exception as ex1:
                with open(output_folder + '/' + doi.replace('/', '-').replace(':', ' ').replace('?', '') + '.pdf', 'wb') as file:
                    file.write(r.content)

            return True

    except Exception as ex:
        print("Error", title, ex)

    return False

print("\n")
print("Writing pdf files.....")

current_dir = os.getcwd()
output_folder = current_dir + "/pdfs"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

doilist = open('dois.txt', 'r')
dois = doilist.readlines()

# for doi in dois:
#     doi = doi.strip()
#     download_pdf(doi, output_folder, doi)

#     sleep(1)

# download_pdf('10.1007/s10107-016-1028-0', output_folder, '<span class="InlineEquation" id="IEq1">\(L^{\infty }\)</span>')
# download_pdf('10.1007/s10107-018-1285-1', output_folder, 'Quadratic optimization with orthogonality constraint: explicit Łojasiewicz exponent and linear convergence of retraction-based line-search and stochastic variance-reduced gradient methods')