import requests
from bs4 import BeautifulSoup
import os
from time import sleep

# https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&highlight=true&returnType=SEARCH&matchPubs=true&ranges=2020._2022_Year&returnFacets=ALL&rowsPerPage=100

BASE_URL = "https://sci-hub.se/"

def download_pdf(doi, output_folder, title):
    try:
        doi = doi.strip()
        response = requests.get(BASE_URL + doi)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        smile = soup.select_one('#smile')
        if smile is not None:
            print("PDF not exist", doi, title)
            return True

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
        try:
            with open(output_folder + '/' + title.replace('/', '-').replace(':', ' ').replace('?', '') + '.pdf', 'wb') as file:
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