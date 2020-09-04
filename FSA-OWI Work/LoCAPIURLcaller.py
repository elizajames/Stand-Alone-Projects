import requests
import pprint
import re
import csv
baseURL = "https://www.loc.gov/collections/fsa-owi-black-and-white-negatives/?c=150&fa=location:west+virginia&fo=json"
pageNumber = "&sp="
bigURLlist = []
regexOGstring = "http://www.loc.gov/pictures/collection/fsa/item/"
regexrecordURL = re.compile(r'http:\/\/www.loc.gov\/pictures\/collection\/fsa\/item\/\d+\/')
for i in range(1,18):
    if i == 1:
        r = requests.get(baseURL)
        r = r.json()
        r = str(r)
        recordURL = regexrecordURL.findall(r)
        bigURLlist.append(recordURL[:150])       
    if i > 1 and i < 17:
        r = requests.get(baseURL + pageNumber + str(i))
        r = r.json()
        r = str(r)
        recordURL = regexrecordURL.findall(r)
        bigURLlist.append(recordURL[:150]) 
    if i == 17: 
        r = requests.get(baseURL + pageNumber + str(i))
        r = r.json()
        r = str(r)
        recordURL = regexrecordURL.findall(r)
        indexy = (len(recordURL))/3
        bigURLlist.append(recordURL[:int(indexy)])
singlecolumn = []

for i in range(len(bigURLlist)): 
    for j in range(len(bigURLlist[i])):
        singlecolumn.append([bigURLlist[i][j]])
with open('APIitemURLs.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(singlecolumn)
print("Done!")