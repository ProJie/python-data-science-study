import codecs
import json
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup

# tree=et.ElementTree(file='weather.xml')
# print(tree.getroot().tag)
wea_xml = codecs.open('weather.xml', 'r')
bsObj = BeautifulSoup(wea_xml.read(), 'lxml')
