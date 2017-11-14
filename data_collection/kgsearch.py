"""Example of Python client calling Knowledge Graph Search API."""
import json
import urllib
import csv
api_key = open('google_api_key').read()
query_list = []
with open("video_search_terms.csv", "rb") as infile:
    reader = csv.reader(infile)
    query_list = [ item[0][:-7] for item in reader ]
count = 1
for query in query_list:
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 1,
        'indent': True,
        'key': api_key,
    }
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())
    for element in response['itemListElement']:
        with open("./kg-search-results/"+query+".json", "wb") as jsonOutfile:
            json.dump(element['result'],jsonOutfile)
        print count, element['result']['name'] + ' (' + str(element['resultScore']) + ')'
        with open("profile.csv", "ab") as csvOutfile:
            writer = csv.writer(csvOutfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([str(query), element['result']['name'].encode('utf-8'), element['result']['@id'], str(element['resultScore'])])
    count += 1
