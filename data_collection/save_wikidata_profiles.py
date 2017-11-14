import requests
DEBUG = True
q_list = []
wikidata_list = []
with open("wikidata_search_Q_terms.csv", "rb") as infile:
    reader = csv.reader(infile)
    wikidata_list = list(reader)
q_list = [wikidata_list[i][1] for i in range(len(wikidata_list))]
if DEBUG :
    print q_list

for i in range(0, len(q_list)):
    try:
        r = requests.get(url='https://www.wikidata.org/wiki/Special:EntityData/'+ q_list[i] +'.json')
        jsonObject = r.json()
        if DEBUG:
            print jsonObject
        with open('./wikidata-search-results/'+ q_list[i]+'.json','wb') as outfile:
            json.dump(jsonObject, outfile)
        print i ,": Created file ", q_list[i],".json for ", wikidata[i][2]
    except e:
        print i, ": sorry not found for "+ q_list[i]
