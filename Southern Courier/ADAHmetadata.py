from bs4 import BeautifulSoup
import urllib.request
import csv
ADAHBaseURL = "http://digital.archives.alabama.gov/cdm/singleitem/collection/peppler/id/"
allMetadata = [["URL","File Name","Title","Description","Creator","Date","Time Period","Subject"]]
def getMetadata(numberPagesStart,numberPagesStop):
    for i in range(numberPagesStart,numberPagesStop):
        print(i)
        linkopen = urllib.request.Request(ADAHBaseURL+str(i))
        try: 
            linkopen = urllib.request.urlopen(linkopen)        
        except urllib.error.URLError as e: 
            print(e.reason)
            continue
        if linkopen:
            workingMetadata = []

            soup = BeautifulSoup(linkopen, "html.parser")
            resultsSubject = soup.select("#metadata_subjec > a")  
            resultsFile = soup.select("#metadata_fila > a")
            resultsTitle = soup.find("h1")
            resultsCreator = soup.select("#metadata_photog")
            resultsDescription = soup.select("#metadata_descri")
            resultsDate = soup.select("#metadata_date > a")
            resultsTimePeriod = soup.select("#metadata_time > a")
          
            if resultsFile != None and resultsFile != []:
                workingMetadata.append(resultsFile[0].get_text())
            else: 
                workingMetadata.append("None")
            if resultsTitle != None and resultsTitle != []:
                workingMetadata.append(resultsTitle.get_text())
            else: 
                workingMetadata.append("None")  
            if resultsDescription != None and resultsDescription != []:
                workingMetadata.append(resultsDescription[0].get_text().strip())
                
            else: 
                workingMetadata.append("None")
            if resultsCreator != None and resultsCreator != []:
                workingMetadata.append(resultsCreator[0].get_text().strip())
            else: 
                workingMetadata.append("None")            
            if resultsDate != None and resultsDate != []:
                workingMetadata.append(resultsDate[0].get_text())
            else: 
                workingMetadata.append("None")            
            if resultsTimePeriod != None and resultsTimePeriod != []: 
                workingMetadata.append(resultsTimePeriod[0].get_text())
            else: 
                workingMetadata.append("None")            
            if resultsSubject != None and resultsSubject != []: 
                for i in resultsSubject: 
                    workingMetadata.append((i.get_text()))
            else: 
                workingMetadata.append("None") 
       
            allMetadata.append(workingMetadata)
            if (len(allMetadata)%100) == 0: 
                with open('ADAHmetadata.csv', 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerows(allMetadata)  
    return allMetadata
allMetadata = getMetadata(0,14412)
with open('ADAHmetadata.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(allMetadata) 
print("You did it!")


