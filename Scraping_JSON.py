import json
import urllib.request , urllib.parse , urllib.error

Json_file = "http://py4e-data.dr-chuck.net/comments_92591.json"

open_JS = urllib.request.urlopen(Json_file)
read_JS = open_JS.read().decode()
Json_data = json.loads(read_JS)

print("Retrieving ",Json_file)
print("Retrieved ", len(read_JS)," characters")

count_lst = list()
for value in Json_data['comments'] :
    count_val = value['count']
    count_lst.append(int(count_val))

print("Count: ",len(count_lst))
print("Sum: ",sum(count_lst))
