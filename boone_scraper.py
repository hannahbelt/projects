#

# python imports
import csv
# external imports
import requests
from bs4 import BeautifulSoup

# get
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
response = requests.get(url)
# print(response)
html = response.content
# print(html)

# parse
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
table = soup.find('tbody', attrs= {'class': 'stripe'})
# print(table)

# extract
list_of_rows = []
for row in table.findAll('tr'):
    # print(row.prettify())
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)

    #print(list_of_cells)
   # print(list_of_cells[:-1])
    list_of_rows.append(list_of_cells[:-1])

# write
outfile = open('data/inmates.csv', 'w+')
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)
