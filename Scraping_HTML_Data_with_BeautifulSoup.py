import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter : ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all the span tags
tags = soup('span')
numbers = list()
for tag in tags :
    numbers.append(int(tag.contents[0]))
# display the sum of all numbers in the table
print(sum(numbers))
