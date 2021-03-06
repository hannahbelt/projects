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
data_dicts = {}
for park in all_ids:
    full_url = f'{url_stub}{nps_uri}{park}'
    #print(full_url)
    # build url

#___________________________________

#code for the annual visitation rates


nps_uri_visit = '/Stats/MvcReportViewer.aspx?_id=f4ecfcf9-2129-46a0-90c2-0c38c4be0446&_m=Remote&_r=%2fNPS.Stats.Reports%2fPark+Specific+Reports%2fRecreation+Visitors+By+Month+(1979+-+Last+Calendar+Year)&_39=880px&Park='

data_dicts = {}
for park in all_ids:
    full_url_visit = f'{url_stub}{nps_uri_visit}{park}'
    print(full_url_visit)
    response = requests.get(full_url_visit)
    html = response.content
    #print(html)

    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', attrs={'cols':'4'})
    #print(soup)
    #print(table)
    break





