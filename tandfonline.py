import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from time import sleep
from sci_hub_pdf import download_pdf

JOURNAL_BASE_URL = 'https://www.tandfonline.com'
JOURNAL_URL = f"{JOURNAL_BASE_URL}/loi/tjor20"
print(JOURNAL_URL)

driver = webdriver.Chrome('./chromedriver.exe')
# driver.get(JOURNAL_URL)
# contents = driver.page_source

contents = '''
<ul>
<li>
<a class="issue-link" href="/toc/tjor20/73/6?nav=tocList">
<div class="issue-num ">Issue 6</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2022
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1181-1422
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/73/5?nav=tocList">
<div class="issue-num ">Issue 5</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2022
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 937-1180
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/73/4?nav=tocList">
<div class="issue-num ">Issue 4</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2022
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 693-935
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/73/3?nav=tocList">
<div class="issue-num ">Issue 3</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2022
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 455-691
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/73/2?nav=tocList">
<div class="issue-num ">Issue 2</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2022
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 207-453
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/73/1?nav=tocList">
<div class="issue-num special">Issue 1</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2022
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1-206
</span>
</p>
<p>
Special Issue on Credit Risk Modelling
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
</ul>
<ul>
<li>
<a class="issue-link" href="/toc/tjor20/72/12?nav=tocList">
<div class="issue-num ">Issue 12</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 2611-2828
</span>

</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/72/11?nav=tocList">
<div class="issue-num ">Issue 11</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 2381-2610
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/72/10?nav=tocList">
<div class="issue-num ">Issue 10</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 2161-2379
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/72/9?nav=tocList">
<div class="issue-num ">Issue 9</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1929-2159
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/72/8?nav=tocList">
<div class="issue-num ">Issue 8</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1689-1927
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/72/7?nav=tocList">
<div class="issue-num ">Issue 7</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1447-1687
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/72/6?nav=tocList">
<div class="issue-num ">Issue 6</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1207-1446
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/72/5?nav=tocList">
<div class="issue-num special">Issue 5</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 971-1206
</span>
</p>
<p>
Special Issue Data Science for Better Productivity
</p>
<span class="access-icon free" role="img" aria-label="You have Free Access"></span><span class="part-tooltip">Free Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/72/4?nav=tocList">
<div class="issue-num ">Issue 4</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 727-970
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/72/3?nav=tocList">
<div class="issue-num ">Issue 3</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 485-725
</span>
 </p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/72/2?nav=tocList">
<div class="issue-num ">Issue 2</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 247-484
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/72/1?nav=tocList">
<div class="issue-num ">Issue 1</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2021
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1-245
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
</ul>
<ul>
<li>
<a class="issue-link" href="/toc/tjor20/71/12?nav=tocList">
<div class="issue-num ">Issue 12</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1873-2052
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/71/11?nav=tocList">
<div class="issue-num ">Issue 11</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1691-1872
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/71/10?nav=tocList">
<div class="issue-num ">Issue 10</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1511-1690
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/71/9?nav=tocList">
<div class="issue-num ">Issue 9</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1327-1509
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/71/8?nav=tocList">
<div class="issue-num ">Issue 8</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1145-1325
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/71/7?nav=tocList">
<div class="issue-num ">Issue 7</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1053-1144
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/71/6?nav=tocList">
<div class="issue-num ">Issue 6</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 867-1052
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/71/5?nav=tocList">
<div class="issue-num ">Issue 5</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 687-865
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/71/4?nav=tocList">
<div class="issue-num ">Issue 4</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 543-686
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/71/3?nav=tocList">
<div class="issue-num ">Issue 3</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 363-542
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/71/2?nav=tocList">
<div class="issue-num ">Issue 2</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 183-361
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/71/1?nav=tocList">
<div class="issue-num ">Issue 1</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2020
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1-181
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
</ul>
<ul>
<li>
<a class="issue-link" href="/toc/tjor20/70/12?nav=tocList">
<div class="issue-num ">Issue 12</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 2019-2168
</span>
 </p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/70/11?nav=tocList">

<div class="issue-num ">Issue 11</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1869-2018
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/70/10?nav=tocList">
<div class="issue-num special">Issue 10</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1579-1868
</span>
</p>
<p>
Computational Approaches and Data Analytics in Financial Services
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/70/9?nav=tocList">
<div class="issue-num ">Issue 9</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1399-1578
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/70/8?nav=tocList">
<div class="issue-num ">Issue 8</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1219-1397
 </span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/70/7?nav=tocList">
<div class="issue-num ">Issue 7</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1039-1218
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/70/6?nav=tocList">
<div class="issue-num ">Issue 6</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 873-1037
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/70/5?nav=tocList">
<div class="issue-num ">Issue 5</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages ii-871
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/70/4?nav=tocList">
<div class="issue-num ">Issue 4</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 531-706
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/70/3?nav=tocList">
<div class="issue-num ">Issue 3</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 353-529
</span>

</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/70/2?nav=tocList">
<div class="issue-num ">Issue 2</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 177-352
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/70/1?nav=tocList">
<div class="issue-num ">Issue 1</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2019
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1-176
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
</ul>
<ul>
<li>
<a class="issue-link" href="/toc/tjor20/69/12?nav=tocList">
<div class="issue-num ">Issue 12</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1877-2033
</span>
 </p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/69/11?nav=tocList">
<div class="issue-num ">Issue 11</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
 </span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1701-1875
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/69/10?nav=tocList">
<div class="issue-num special">Issue 10</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1525-1699
</span>
</p>
<p>
Special issue - Multicriteria Decision Making in Finance
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/69/9?nav=tocList">
<div class="issue-num ">Issue 9</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1345-1523
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/69/8?nav=tocList">
<div class="issue-num ">Issue 8</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1167-1343
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/69/7?nav=tocList">
<div class="issue-num ">Issue 7</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
</span>
<span id="loiIssuePages" class="loiIssuePages">
 pages 987-1165
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/69/6?nav=tocList">
<div class="issue-num ">Issue 6</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 811-985
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/69/5?nav=tocList">
<div class="issue-num ">Issue 5</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 645-810
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/69/4?nav=tocList">
<div class="issue-num ">Issue 4</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 487-644
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/69/3?nav=tocList">
<div class="issue-num ">Issue 3</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 319-486
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/69/2?nav=tocList">
<div class="issue-num ">Issue 2</div>
<p class="meta">

<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 157-318
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/69/1?nav=tocList">
<div class="issue-num ">Issue 1</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2018
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1-155
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
</ul>
<ul>
<li>
<a class="issue-link" href="/toc/tjor20/68/12?nav=tocList">
<div class="issue-num ">Issue 12</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1483-1669
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/68/11?nav=tocList">

<div class="issue-num ">Issue 11</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1307-1481
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/68/10?nav=tocList">
<div class="issue-num ">Issue 10</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1131-1305
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/68/9?nav=tocList">
<div class="issue-num ">Issue 9</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 985-1130
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/68/8?nav=tocList">
<div class="issue-num ">Issue 8</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 861-983
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/68/7?nav=tocList">
<div class="issue-num ">Issue 7</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 741-860
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/68/6?nav=tocList">
<div class="issue-num ">Issue 6</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 605-740
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/68/5?nav=tocList">
<div class="issue-num ">Issue 5</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 469-604
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/68/4?nav=tocList">
<div class="issue-num special">Issue 4</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
 2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 331-468
</span>
</p>
<p>
Efficiency in Education
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/68/3?nav=tocList">
<div class="issue-num ">Issue 3</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 221-330
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/68/2?nav=tocList">
<div class="issue-num ">Issue 2</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 111-220
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/68/1?nav=tocList">
<div class="issue-num ">Issue 1</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2017
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1-110
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
</ul>
<ul>
<li>
<a class="issue-link" href="/toc/tjor20/67/12?nav=tocList">
<div class="issue-num ">Issue 12</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1439-1540
</span>
 </p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/67/11?nav=tocList">

<div class="issue-num ">Issue 11</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1341-1437
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/67/10?nav=tocList">
<div class="issue-num ">Issue 10</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1239-1339
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/67/9?nav=tocList">
<div class="issue-num ">Issue 9</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1212-1237
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/67/8?nav=tocList">
<div class="issue-num ">Issue 8</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1025-1134
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/67/7?nav=tocList">
<div class="issue-num ">Issue 7</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 911-1024
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/67/6?nav=tocList">
<div class="issue-num ">Issue 6</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 801-896
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/67/5?nav=tocList">
<div class="issue-num ">Issue 5</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 691-800
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/67/4?nav=tocList">
<div class="issue-num ">Issue 4</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 537-689
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/67/3?nav=tocList">
<div class="issue-num ">Issue 3</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
 2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 377-535
 </span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/67/2?nav=tocList">
<div class="issue-num special">Issue 2</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 159-376
</span>
</p>
<p>
Special Issue: Risk Management and Coordination in Service Supply Chains: Information, Logistics and Outsourcing
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/67/1?nav=tocList">
<div class="issue-num ">Issue 1</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2016
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1-158
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
</ul>
<ul>
<li>
<a class="issue-link" href="/toc/tjor20/66/12?nav=tocList">
<div class="issue-num ">Issue 12</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1949-2119
</span>
 </p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/66/11?nav=tocList">

<div class="issue-num ">Issue 11</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1769-1948
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/66/10?nav=tocList">
<div class="issue-num special">Issue 10</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1589-1767
</span>
</p>
<p>
Feature Cluster: In Memory of DJ White
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/66/9?nav=tocList">
<div class="issue-num ">Issue 9</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1413-1588
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/66/8?nav=tocList">
<div class="issue-num ">Issue 8</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1237-1412
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/66/7?nav=tocList">
<div class="issue-num ">Issue 7</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1061-1236
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/66/6?nav=tocList">
<div class="issue-num ">Issue 6</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 885-1060
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/66/5?nav=tocList">
<div class="issue-num ">Issue 5</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 709-884
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/66/4?nav=tocList">
<div class="issue-num ">Issue 4</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 529-707
</span>
</p>
<span class="access-icon part" role="img" aria-label="You have Partial Access"></span><span class="part-tooltip">Partial Access</span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/66/3?nav=tocList">
<div class="issue-num ">Issue 3</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
 <span id="loiIssuePages" class="loiIssuePages">
pages 353-528
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/66/2?nav=tocList">
<div class="issue-num ">Issue 2</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 177-352
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
<li>
<a class="issue-link" href="/toc/tjor20/66/1?nav=tocList">
<div class="issue-num ">Issue 1</div>
<p class="meta">
<span id="loiIssueCoverDateText" class="loiIssueCoverDateText">
2015
</span>
<span id="loiIssuePages" class="loiIssuePages">
pages 1-176
</span>
</p>
<span class="access-icon no"></span>
</a>
</li>
</ul>
'''
# response = requests.get(JOURNAL_URL)
print("Parse is Ended")
soup = BeautifulSoup(contents, 'html.parser')

journal_name = 'Journal of the Operational Research Society'
# current_dir = os.getcwd()

current_dir = 'E://Book/Journals'
output_folder = current_dir + "/" + journal_name

if not os.path.exists(output_folder):
    os.mkdir(output_folder)


for link in soup.select('.issue-link'):
    href = link['href']

    vol_issue = href.replace('/toc/tjor20/', '').replace('?nav=tocList', '')
    items = vol_issue.split("/")

    volume = items[0]
    issue = items[1]

    title = f"Volume {volume} - Issue {issue}"
    href = JOURNAL_BASE_URL + href
    print(href, title)

    driver.get(href)
    contents = driver.page_source
    soup = BeautifulSoup(contents, 'html.parser')
    
    output_folder = current_dir + "/" + journal_name  + "/" + title
    
    output_folder = output_folder.strip()
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    sleep(0.1)

    for link in soup.select('.art_title a'):
        href = link['href']
        title  = link.select_one("span.hlFld-Title").contents[0]

        # get doi
        doi = href.replace("/doi/full/", "")
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

    
