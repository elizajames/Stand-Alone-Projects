import re
import csv
recordlist = [["Subject Type","Subject Start"]]
txtfile = open("C:\\Users\\eliza\\Code\\MARC Parsing\\MARC Records.txt","r", encoding="UTF-8")
index = 1
for i in txtfile:
    if "600" in i[:4]:
        recordlist.append(["Personal Name",i[7::]])
        if "\n" in recordlist[-1][1]: 
            interim = recordlist[-1][1]
            interim = interim.replace(" \n","")
            recordlist[-1][1] = interim
    if "610" in i[:4]:
        recordlist.append(["Corporate Name",i[7::]])
        if "\n" in recordlist[-1][1]: 
            interim = recordlist[-1][1]
            interim = interim.replace(" \n","")
            recordlist[-1][1] = interim       
    if "630" in i[:4]:
        recordlist.append(["Uniform Title",i[7::]])
        if "\n" in recordlist[-1][1]: 
            interim = recordlist[-1][1]
            interim = interim.replace(" \n","")
            recordlist[-1][1] = interim        
    if "650" in i[:4]:
        recordlist.append(["Topical Term",i[7::]])
        if "\n" in recordlist[-1][1]: 
            interim = recordlist[-1][1]
            interim = interim.replace(" \n","")
            recordlist[-1][1] = interim        
    if "651" in i[:4]:
        recordlist.append(["Geographic Name",i[7::]])
        if "\n" in recordlist[-1][1]: 
            interim = recordlist[-1][1]
            interim = interim.replace(" \n","")
            recordlist[-1][1] = interim        
    if "655" in i[:4]:
        recordlist.append(["Genre/Form",i[7::]])
        if "\n" in recordlist[-1][1]: 
            interim = recordlist[-1][1]
            interim = interim.replace(" \n","")
            recordlist[-1][1] = interim        
    if "690" in i[:4]:
        recordlist.append(["Local Subject Field",i[7::]])
        if "\n" in recordlist[-1][1]: 
            interim = recordlist[-1][1]
            interim = interim.replace(" \n","")
            recordlist[-1][1] = interim       
with open('MARCSubjectParsing.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(recordlist)
print("Done!")
