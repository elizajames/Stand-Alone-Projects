import re
import csv
recordlist = [["Record Number","Oral History Number","Date","Interviewee (authority)", "Interviewee (plain text)","Interviewer (plain text)", "Title","Length","Summary","Subject Start"]]
txtfile = open("export.txt","r", encoding="UTF-8")

regexrecordnum = re.compile(r'Record (\d+)')
regexOHnum = re.compile(r'1 > Special Collections/Ora OH 64-(\d*)')
regexdate = re.compile(r'TITLE        .*(\d\d\d\d)')
regexintervieweeAuthority = re.compile(r'^AUTHOR       (.*)[^.]')
regexintervieweePlain = re.compile(r'TITLE        (.*) oral history interview')
regexinterviewerPlain = re.compile(r'TITLE        .* conducted by (.*).')
regextitle = re.compile(r'^TITLE        (.*)')
regexlength = re.compile(r'DESCRIPT     Transcript *: *(\d*)')
regexsummary = re.compile(r'NOTE         (.*)')
regexsubjectstart = re.compile(r'SUBJECT      (.*)')
regexmultiline = re.compile(r'               (.*)')
for i in range(666): 
    recordlist.append(["","","","","","","","",""])
txtfiletext = []
index = 0
for i in txtfile:
    txtfiletext.append(i)
for i in range(len(txtfiletext)):
    if "\n" in txtfiletext[i]:
        txtfiletext[i] = txtfiletext[i].replace("\n","")
while index in range(len(txtfiletext)):
    if "               " in txtfiletext[index]:
        txtfiletext[index] = txtfiletext[index].replace("               "," ")
        txtfiletext[index-1] = txtfiletext[index-1] + txtfiletext[index]
        txtfiletext.pop(index)
    else:
        index += 1
recordnum = None 
OHnum = None
date = None
intervieweeAuth = None
intervieweePlain = None
interviewerPlain = None
title = None
length = None
summary = None
subjectstart = None
index = 1
for i in txtfiletext:
    if regexrecordnum.search(i) != None:
        recordnum = regexrecordnum.search(i)
    if regexOHnum.search(i) != None:
        OHnum = regexOHnum.search(i)   
    if regexdate.search(i) != None:
        date = regexdate.search(i)   
    if regexintervieweeAuthority.search(i) != None:
        intervieweeAuth = regexintervieweeAuthority.search(i)    
    if regexintervieweePlain.search(i) != None:
        intervieweePlain = regexintervieweePlain.search(i)
    if regexinterviewerPlain.search(i) != None:
        interviewerPlain = regexinterviewerPlain.search(i)     
    if regextitle.search(i)  != None:
        title = regextitle.search(i)      
    if regexlength.search(i) != None:
        length = regexlength.search(i)        
    if regexsummary.search(i) != None:
        if summary == None:
            summary = regexsummary.search(i)
            summary = summary.group(1)
        else:
            summary2 = regexsummary.search(i)
            summary2 = summary2.group(1)
            summary = summary + " " + summary2
    if regexsubjectstart.search(i) != None:
        subjectstart = regexsubjectstart.search(i)       
        recordlist[index].append(subjectstart.group(1))  
    if OHnum != None:
        if recordnum != None:
            recordlist[index][0]=recordnum.group(1)
        else:
            recordlist[index][0]="No data found"
        if OHnum != None:
            recordlist[index][1]=OHnum.group(1)
        else:
            recordlist[index][1]="No data found"        
        if date != None:
            recordlist[index][2]=date.group(1)
        else:
            recordlist[index][2]="No data found"        
        if intervieweeAuth != None:
            recordlist[index][3]=intervieweeAuth.group(1)
        else:
            recordlist[index][3]="No data found"        
        if intervieweePlain != None:
            recordlist[index][4]=intervieweePlain.group(1)
        else:
            recordlist[index][4]="No data found"        
        if interviewerPlain != None:
            recordlist[index][5]=interviewerPlain.group(1)
        else:
            recordlist[index][5]="No data found"        
        if title != None:
            recordlist[index][6]=title.group(1)
        else:
            recordlist[index][6]="No data found"        
        if length != None:
            recordlist[index][7]=length.group(1)
        else:
            recordlist[index][7]="No data found"        
        if summary != None:
            recordlist[index][8]= summary
        else:
            recordlist[index][8]="No data found"                
        index += 1 
        recordnum = None 
        OHnum = None
        date = None
        intervieweeAuth = None
        intervieweePlain = None
        interviewerPlain = None
        title = None
        length = None
        summary = None
        subjectstart = None
with open('MARCParsing.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(recordlist)
print("Done!")
