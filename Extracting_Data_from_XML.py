import urllib.request , urllib.parse , urllib.error
import xml.etree.ElementTree as ET
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
#retrieving XML file form url
xml_file = urllib.request.urlopen(url, context = ctx).read()
trees_list = ET.fromstring(xml_file)
trees = trees_list.findall('comments/comment')
count_val = []
for tree in trees :
    count_val.append(int(tree.find('count').text))
#printing the number of characters retrieved from XML file and the sum of count tag
print('Retrieving',url)
print('Retrieved' , len(xml_file))
print('Count: ',len(count_val))
print('Sum: ',sum(count_val))
