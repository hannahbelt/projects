# python imports
import json
import xmletree.ElementTree at ET
tree = ET.parse('nps_boundary.xml')
root = tree.getroot()
# external imports
import requests
from bs4 import BeautifulSoup

list_of_ids = []
for id in something.findAll('placekey')
#build the urls using code from xml
# loop through the park codes
for full_url in 

#url components
url_stub = 'https://irma.nps.gov'

nps_uri = '/Stats/MvcReportViewer.aspx?_id=6d4c57ec-773a-4be8-a7d7-4410daaa91ad&_m=Remote&_r=%2fNPS.Stats.Reports%2fPark+Specific+Reports%2fMonthly+Visitation+Comments+By+Park&_39=880px&Park='

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