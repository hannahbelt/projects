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

if element.text == 'National Park System Unit Code Thesaurus':
    places = element.findall('place')
    the_right_places = places[1]



    for place in places:
        # do something with place.text


        tree = ET.parse('nps_boundary.xml')
        root = tree.getroot()
print(root)
#build the urls using code from xml
# loop through the park codes
park_nodes = root.findall(el_path)

nat_park_ids = {}
for park in park_nodes:
    try:
        park_name = park.find(attr).text
        
    except AttributeError:
        continue

    
codes = get_park_codes(file_with_codes,element_xpath, park_name)

#url components
url_stub = 'https://irma.nps.gov'

nps_uri = '/Stats/MvcReportViewer.aspx?_id=6d4c57ec-773a-4be8-a7d7-4410daaa91ad&_m=Remote&_r=%2fNPS.Stats.Reports%2fPark+Specific+Reports%2fMonthly+Visitation+Comments+By+Park&_39=880px&Park='

full_url = f'{url_stub}{nps_uri}{nat_park_ids}'

# build loop for comments
# skip over comments that dont have errors in them
# common "errors" are recorded

# get page content

#parse html

#extract data

# build dictionary for comments

# write

#call all functions

# if name = main stuff here?