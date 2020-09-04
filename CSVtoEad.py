import csv
import os
'''
Things to solve: 
Test output against valid EAD from AS output
Test output when uploaded into AS

'''

inputDirectory = "C:\\Users\\eliza\\Code\\CSVtoEAD\\InputCSV\\"
outputDirectory = "C:\\Users\\eliza\\Code\\CSVtoEAD\\OutputEAD\\"
inputFileList = os.listdir('C:\\Users\\eliza\\Code\\CSVtoEAD\\InputCSV')
outputFileList = os.listdir('C:\\Users\\eliza\\Code\\CSVtoEAD\\OutputEAD')

eaddocstart = r"""<?xml version="1.0" encoding="utf-8"?>
<ead xmlns="urn:isbn:1-931666-22-9"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="urn:isbn:1-931666-22-9 http://www.loc.gov/ead/ead.xsd">
    <eadheader countryencoding="iso3166-1"
            dateencoding="iso8601"
            langencoding="iso639-2b"
            repositoryencoding="iso15511">"""
eaddocend = r"</dsc></archdesc></ead>"

def csvtoead(filename):
    csvfile = open((inputDirectory + filename), newline='', encoding='utf-8')             
    filecontent = csv.reader(csvfile)
    filecontent = list(filecontent)
    eadid = r'<eadid>' + filecontent[0][1].strip() + r'</eadid>'
    filedesc = r"<filedesc><titlestmt><titleproper>" + filecontent[3][1].strip() + r"</titleproper><author>" + filecontent[6][1].strip() + r'</author></titlestmt><publicationstmt><publisher>' + "Marshall University Archives and Special Collections" + r"</publisher><date>" + filecontent[7][1].strip() + r'</date></publicationstmt></filedesc><profiledesc><langusage><language encodinganalog="Language" langcode="eng">English</language></langusage></profiledesc></eadheader>'
    eadheader = eadid + filedesc
    if len(filecontent[1][1].strip()) <= 4: 
        addzeroes = 4 - len(filecontent[1][1].strip())
        unitid = ("0"*addzeroes) + filecontent[1][1].strip()
    collectiondescription = r'<archdesc level="collection"><did><repository><corpname>Marshall University Archives and Special Collections</corpname></repository><unittitle>' + \
    filecontent[3][1].strip() + r'</unittitle><origination label="Creator"><persname>' + \
    filecontent[5][1].strip() + r'</persname></origination><unitid>' + \
    unitid + r'</unitid><physdesc><extent>' + \
    filecontent[11][1].strip() + " linear feet" + r'</extent></physdesc><unitdate type="inclusive">' + \
    filecontent[4][1].strip() + r'</unitdate><langmaterial>' + \
    filecontent[10][1].strip() + r'</langmaterial></did><bioghist>' + \
    filecontent[8][1].strip() + r'</bioghist><scopecontent><p>' + \
    filecontent[9][1].strip() + r'</p></scopecontent><prefercite>' + \
    filecontent[12][1].strip() + r'</prefercite><acqinfo>' + \
    filecontent[13][1].strip() + r'</acqinfo><processinfo>' + \
    filecontent[15][1].strip() + r'</processinfo><accessrestrict>' + \
    filecontent[16][1].strip() + r'</accessrestrict><accruals><p>The following collections have been merged into and are part of this collection:</p><p>' + \
    filecontent[14][1].strip() + r'</p></accruals><note><p>The full accession number for this collection is:</p><p>' + \
    filecontent[2][1].strip() + r'</p></note><dsc>'
        
    doneWithContainers = False
    rowcounter = 18 # initialize wherever container data starts --row number minus one 
    finalIndex = len(filecontent) - 1
    containerContent = ""
    workingSeries = ""
    while doneWithContainers == False:       
        if "Series" in filecontent[rowcounter][0] and workingSeries == "" and filecontent[rowcounter][1].strip() != "": 
            containerContent = r'<c01 level="series"><did><unittitle>' + \
	    filecontent[rowcounter][1].strip() + r'</unittitle></did>'
            workingSeries = filecontent[rowcounter][1].strip()
        elif "Series" in filecontent[rowcounter][0] and filecontent[rowcounter][1].strip() != workingSeries: 
            containerContent = containerContent + r'</c01><c01 level="series"><did><unittitle>' + \
	    filecontent[rowcounter][1].strip() + r'</unittitle></did>'
            workingSeries = filecontent[rowcounter][1].strip()
        elif "Box" in filecontent[rowcounter][0]:
            workingBox = filecontent[rowcounter][1].strip()
        else:
            if filecontent[rowcounter][0].strip() == "" and filecontent[rowcounter][1].strip() != "": 
                if workingSeries == "": 
                    containerContent = containerContent + r'<c01 level="item"><did><unittitle>' + \
                    filecontent[rowcounter][1].strip() + r'</unittitle><container type="Box">' + \
                    workingBox + r'</container></did></c01>'                                
                elif workingSeries != "":
                    containerContent = containerContent + r'<c02 level="item"><did><unittitle>' + \
                    filecontent[rowcounter][1].strip() + r'</unittitle><container type="Box">' + \
                    workingBox + r'</container></did></c02>'    
            elif filecontent[rowcounter][0].strip().isdigit(): 
                if workingSeries == "": 
                    containerContent = containerContent + r'<c01 level="file"><did><unittitle>Folder ' + \
                    filecontent[rowcounter][0].strip() + " - " + filecontent[rowcounter][1].strip() + r'</unittitle><container type="Box">' + \
                    workingBox + r'</container></did>' 
                    if (rowcounter + 1) > finalIndex or len(filecontent[rowcounter+1]) < 3 or filecontent[rowcounter+1][2].strip() == "": 
                        containerContent = containerContent + r'</c01>'
                    elif (rowcounter + 1) > finalIndex or len(filecontent[rowcounter+1]) >= 3 or filecontent[rowcounter+1][2].strip() != "": 
                        rowcounter += 1
                        while filecontent[rowcounter][2] != "":
                            containerContent = containerContent + r'<c02 level="item"><did><unittitle>' + \
                            filecontent[rowcounter][2].strip() + r'</unittitle><container type="Box">' + \
                            workingBox + r'</container></did></c02>'                            
                            if filecontent[rowcounter+1][2].strip() == "":
                                containerContent = containerContent + r'</c01>'
                                break
                            else: 
                                rowcounter += 1                                 
                if workingSeries != "":
                    containerContent = containerContent + r'<c02 level="file"><did><unittitle>Folder ' + \
                    filecontent[rowcounter][0].strip() + " - " + filecontent[rowcounter][1].strip() + r'</unittitle><container type="Box">' + \
                    workingBox + r'</container></did>'
                    if (rowcounter + 1) > finalIndex or len(filecontent[rowcounter+1]) < 3 or filecontent[rowcounter+1][2].strip() == "": 
                        containerContent = containerContent + r'</c02>'
                    elif (rowcounter + 1) > finalIndex or len(filecontent[rowcounter+1]) >= 3 or filecontent[rowcounter+1][2].strip() != "": 
                        rowcounter += 1
                        while filecontent[rowcounter][2] != "":
                            containerContent = containerContent + r'<c03 level="item"><did><unittitle>' + \
                            filecontent[rowcounter][2].strip() + r'</unittitle><container type="Box">' + \
                            workingBox + r'</container></did></c03>'                            
                            if len(filecontent[rowcounter+1]) < 3 or filecontent[rowcounter+1][2].strip() == "":
                                containerContent = containerContent + r'</c02>'
                                break
                            else: 
                                rowcounter += 1                                          
        rowcounter += 1
        if rowcounter > finalIndex: 
            if workingSeries != "": 
                containerContent = containerContent + r"</c01>"
            doneWithContainers = True 
    eaddoc = eaddocstart + eadheader + collectiondescription + containerContent + eaddocend 
    eaddoc = eaddoc.replace("&","and")
    csvfile.close()
    newFileName = outputDirectory + filecontent[0][1] + ".xml"
    newFile = open(newFileName,"w", encoding="utf-8")
    newFile.write(eaddoc)  
    newFile.close()    
for file in inputFileList: 
    csvtoead(file)
