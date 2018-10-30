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
   
