import requests
q = 'Q9570'
r = requests.get(url='https://www.wikidata.org/wiki/Special:EntityData/'+ q +'.json')
# print r.json()
jsonObject = r.json()
# Refer https://www.wikidata.org/wiki/Wikidata:List_of_properties/Person for description of propoerties
name_of_properties = ['sex or gender', 'date of birth','place of birth','occupation','field of work', 'country of residence', 'religion', 'voice_type', 'ethnic group']
list_of_properties = ['P21', 'P569','P19', 'P106', 'P101', 'P27', 'P140', 'P412', 'P172']
# list_of_properties = ['P21', 'P569','P19']
list_path = ['entities',q, 'claims']
for part_of_path in list_path:
    if part_of_path in jsonObject:
        jsonObject = jsonObject[part_of_path]
# print jsonObject

for index in range(len(list_of_properties)):
    # list_path = ['entities',q, 'claims', list_of_properties[index]]
    print index
    property_path = None
    success = True
    if list_of_properties[index] in jsonObject:
        property_path = jsonObject[list_of_properties[index]]
        # print property_path
            # print jsonObject['entities'][q]['claims']['P569'][0]['mainsnak']['datavalue']['value']['id']
    else:
        print "Sorry, no property as ", name_of_properties[index]
        success = False
    if success:
        property_path = property_path[0]
        list_path_to_value = ['mainsnak','datavalue','value']
        for part in list_path_to_value:
            if part in property_path:
                property_path = property_path[part]
                # print "Part:", part, "\n", property_path
            else:
                print "Check the array again"
        if list_of_properties[index] == 'P569':
            value = property_path['time']
            print property_path['time']
        else:
            qid = property_path['id']
            print qid
            # Finding
            r = requests.get(url='https://www.wikidata.org/wiki/Special:EntityData/'+ qid +'.json')
            value = r.json().get('entities').get(qid).get('labels').get('en').get('value')

        print list_of_properties[index], name_of_properties[index], ":", value
