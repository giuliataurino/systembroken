import urllib3
import json
api_key = "fe328c60-46d7-11ea-a9bf-f57013651a17"
api_key = "5abc7900-3e6d-11ea-9384-e935c98ee037"

### FIELDS TO SELECT ON ###
fields = {
    'apikey': api_key,
    'fields': 'objectnumber,title,dated,color, seeAlso, Annotation', 
    'fields': "*", #'objectnumber,title,dated,color, seeAlso, Annotation', 
    "Object": '?',      #https://github.com/harvardartmuseums/api-docs/blob/master/sections/object.md
    "Person": "?",  #https://github.com/harvardartmuseums/api-docs/blob/master/sections/person.md
    "Exhibition": "?",
@@ -60,10 +61,34 @@ id_list = []
for item in records_list:
    id_list.append(item['id'])


urls = None

count = 0
while urls == None:
    try:
        urls = parsed_json["records"][count]["primaryimageurl"]
    except(KeyError):
        pass
    count += 1

desc_dic_full = parsed_json["records"][count-1]


descriptors = ["century", "classification", "commentary", "culture", "datebegin",
               "dated", "dateend", "description", "edition", "id", "images", "labeltext",
               "medium", "objectid", "objectnumber", "period", "places", "primaryimageurl",
               "provenance", "rank", "seeAlso", "signed", "standardreferencenumber", "state",
               "style", "technique", "techniqueid", "terms", "title", "titles", "url",
               "verificationlevel", "verificationleveldescription", "worktypes"]
desc_dic = {}
for key in descriptors:
    try:
        desc_dic[key] = desc_dic_full[key]
    except(KeyError):
        pass
"""
RANDOMIZER   --> could be replaced with AI
"""
random_pics_to_select = 1 #number of pictures to choose
sample_size = len(id_list)
random_numbers = []
@@ -81,17 +106,33 @@ for _ in range(random_pics_to_select):
for number in random_numbers:
    random_ids.append(id_list[number])

"""
"""
OPEN IMAGE
"""

from PIL import Image
import urllib.request
import io

URL = urls
#    URL = 'https://nrs.harvard.edu/urn-3:HUAM:' + str(112313)
#    urlopen(urls)
#    URL =  "https://nrs.harvard.edu/urn-3:huam:DDC112313_dynmc?width=1285&height=880"

with urllib.request.urlopen(URL) as url:
    f = io.BytesIO(url.read())

img = Image.open(f)

img.show()

#from urllib.request import urlopen
"""
for pic in random_ids:
    URL = 'https://nrs.harvard.edu/urn-3:HUAM:' + str(755710)
    URL = urls
#    URL = 'https://nrs.harvard.edu/urn-3:HUAM:' + str(112313)
#    urlopen(urls)
#    URL =  "https://nrs.harvard.edu/urn-3:huam:DDC112313_dynmc?width=1285&height=880"
    
    with urllib.request.urlopen(URL) as url:
@@ -100,3 +141,6 @@ for pic in random_ids:
    img = Image.open(f)
    
    img.show()
    
"""
print(desc_dic)
