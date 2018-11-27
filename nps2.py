# python imports
import json
import xml.etree.ElementTree as ET
# external imports
import requests
from bs4 import BeautifulSoup

file_with_codes = 'data/nps_boundary.xml'
element_xpath = './/*attrplacekey/'
attr = 'placekey'
filename = 'nps_boundary.xml'




tree = ET.parse(file_with_codes)
root = tree.getroot()
#print(root)
#for child in root:
    #print(child.tag, child.attrib)
    #print(keywords.tag, keywords.attrib)
   # ids = keywords.find('ids').text
#print(root.findall('idinfo'))
idinfo = root.find('idinfo')
# print(idinfo)
key = idinfo.find('keywords')
#print(key)
place = key.findall('place')[1]
ids = place.findall('placekey')
all_ids = []
for element in ids:
    if element.text.isupper() and len(element.text) == 4:
        all_ids.append(element.text)

url_stub = 'https://irma.nps.gov'

nps_uri = '/Stats/MvcReportViewer.aspx?_id=6d4c57ec-773a-4be8-a7d7-4410daaa91ad&_m=Remote&_r=%2fNPS.Stats.Reports%2fPark+Specific+Reports%2fMonthly+Visitation+Comments+By+Park&_39=880px&Park='

#def build_url_list():
# main loop
data_dicts_comments = {}
for park in all_ids:
    full_url = f'{url_stub}{nps_uri}{park}'
    response = requests.get(full_url)
    html = response.content

    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', attrs={'cols':'2'})
    if table:
        list_of_dicts = []
        for dicts in table.findAll('tr'):
                list_of_comments = []
                if dicts.find('div') is not None:
                        for comments in dicts.findAll('div'):
                                list_of_comments.append(comments.text)
                                list_of_dicts.append(list_of_comments)
        print(list_of_dicts)

    #print(full_url)
    # build url

#get comments from each page
#write jsons for both things
#___________________________________

#code for the annual visitation rates


nps_uri_visit = '/Stats/MvcReportViewer.aspx?_id=f4ecfcf9-2129-46a0-90c2-0c38c4be0446&_m=Remote&_r=%2fNPS.Stats.Reports%2fPark+Specific+Reports%2fRecreation+Visitors+By+Month+(1979+-+Last+Calendar+Year)&_39=880px&Park='

data_dicts_visitors = {}
for park in all_ids:
    full_url_visit = f'{url_stub}{nps_uri_visit}{park}'
    #print(f'VISITING URL: {full_url_visit}')
    response = requests.get(full_url_visit)
    html = response.content
    #print(html)

    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', attrs={'cols':'14'})
    #print(soup)
    #print(table)
    if table:
        list_of_rows = []
        for row in table.findAll('tr'):
                list_of_cells = []
                if row.find('div') is not None:
                        for cell in row.findAll('div'):
                                # add it to the list of cells
                                list_of_cells.append(cell.text)
                        list_of_rows.append(list_of_cells)

        #print(list_of_rows)
        break
        # for row in list_of_rows:
        #     print(row)
        #     break




