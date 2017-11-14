import requests
import csv

term_list=[]
q_list = []
with open("video_search_terms.csv", "r") as infile:
    reader = csv.reader(infile)
    term_list = [item[0][:-7] for item in reader ]

for item in term_list:
    r = requests.get(url='https://www.wikidata.org/w/api.php?action=query&list=wbsearch&wbssearch='+item+'&wbslanguage=en&format=json')
    jsonObject = r.json()
    print jsonObject
    path_to_wbsearch = ["query", "wbsearch"]
    for part in path_to_wbsearch:
        if part in jsonObject:
            jsonObject = jsonObject[part]
    if isinstance(jsonObject, (list)):
        if len(jsonObject)>0:
            print item, jsonObject[0]['title']
            with open("wikidata_search_Q_terms.csv", "ab") as csvfile:
                writer = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([item, jsonObject[0]['title'],jsonObject[0]['displaytext'].encode('utf-8').strip()])

# item = "sdhsagbdhsajdbsajdhwdebsjkd"
# r = requests.get(url='https://www.wikidata.org/w/api.php?action=query&list=wbsearch&wbssearch='+item+'&wbslanguage=en&format=json')
# jsonObject = r.json()
# print jsonObject
# path_to_wbsearch = ["query", "wbsearch"]
# for part in path_to_wbsearch:
#     if part in jsonObject:
#         jsonObject = jsonObject[part]
# if isinstance(jsonObject, (list)):
#     if len(jsonObject)>0:
#         print jsonObject[0]['title']
