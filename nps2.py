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
idinfo = root.findall('idinfo')
key = root.findall('keywords')
ids = root.findall('place'[1])
print(ids)



# find within idinfo a variable element called 'keywords'

# find with that variable, the place elements, use index [1] and save to variable

#define an empty list variable


#print(root[1][5][4].findall)





#idinfo then keywords then place then placekey