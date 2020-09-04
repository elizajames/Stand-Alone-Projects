import requests
import pprint
import re
import csv
import json
URLaddon = "?&fo=json&at=item"
bigDatalist = [["URL","Title","Date","Creator","Place","Subject Start"]]
with open('APIitemURLs.csv', 'r', encoding="UTF-8") as csvfile:
    filecontent = csv.reader(csvfile)
    filecontent = list(filecontent)
for i in range(len(filecontent)):
        listitem = str(filecontent[i])
        listitem = listitem.replace("[","")
        listitem = listitem.replace("]","")
        listitem = listitem.replace("'","")
        r = requests.get(listitem+URLaddon)
        r = r.json()
        print(r['item']['title'])
        print(r['item']['sort_date'])
        if len(r['item']['creators'])>0:
            creator = (r['item']['creators'][0]['title'])
        print(r['item']['place'][0]['title'])
        workingnum = [listitem,(r['item']['title']), (r['item']['sort_date']), creator, (r['item']['place'][0]['title'])]
        for i in range(len(r['item']['subjects'])):
            workingnum.append((r['item']['subjects'][i]['title']))
        bigDatalist.append(workingnum)
        if len(bigDatalist) % 5 == 0:
            with open('APIcall.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(bigDatalist)
print("Done!")