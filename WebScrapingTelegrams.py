from bs4 import BeautifulSoup
import urllib.request
import requests
import csv
baseURL = "https://civilwarwv.lib.wvu.edu/catalog/ptp_"
metadata = [["Link to Telegram","Sender","Sender Location","Recipient","Recipient Location","Date","Transcript"]]
for i in range(1,1060): 
    if len(str(i)) <= 4:
        numZeroes = 4 - len(str(i))
        URLnumber = "0"*numZeroes + str(i)    
    linkopen = urllib.request.urlopen(baseURL + URLnumber)
    soup = BeautifulSoup(linkopen, "html.parser")
    results = soup.find_all(class_="metedata") 
    workingdata = ["","","","","","",""]
    for index in range(len(results)): 
        data = results[index].text.strip()
        workingdata[0] = baseURL + URLnumber
        if index == 0: 
            workingdata[5] = data
        if index == 1: 
            workingdata[3] = data
        if index == 2: 
            workingdata[6] = data
        if index == 3: 
            workingdata[1] = data
        if index == 5: 
            workingdata[2] = data
        if index == 6: 
            workingdata[4] = data
    metadata.append(workingdata)
with open("telegramoutput.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(metadata)
    f.close()


