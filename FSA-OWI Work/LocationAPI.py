import requests
import re
import csv
baseURL = "http://open.mapquestapi.com/geocoding/v1/address?key=tLdserEvNDI0HJa7yvC2vokC28zgEu6J&city="
stateURL = "&state=West%20Virginia"
regexLocation = re.compile(r'[a-zA-Z ]*$')
with open('APIcall.csv', 'r', encoding="UTF-8") as csvfile:
    filecontent = csv.reader(csvfile)
    filecontent = list(filecontent)
for i in range(len(filecontent)):
    if regexLocation.findall(filecontent[i][4]) != None:
        location = regexLocation.search(filecontent[i][4])
        r = requests.get(baseURL + str(location[0]) + stateURL)
        r = r.json()
        lat = (r['results'][0]['locations'][0]['latLng']['lat']) 
        lng = (r['results'][0]['locations'][0]['latLng']['lng'])
        location = [str(lat) + ", " + str(lng)]
        filecontent[i].append(location)
    else: 
        location = ["No location found"]
        filecontent[i].append(location)
with open('APIcalledits.csv', 'w', encoding="UTF-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(filecontent)
print("Done!")
