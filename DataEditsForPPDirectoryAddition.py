import csv
import os

directory = "C:\\Users\\eliza\\Code\\PPFileProject\\Original Files\\"
directoryOutput = "C:\\Users\\eliza\\Code\\PPFileProject\\Output Files\\"
fileList = os.listdir('C:\\Users\\eliza\\Code\\PPFileProject\\Original Files')
newFileList = os.listdir('C:\\Users\\eliza\\Code\\PPFileProject\\Output Files')

def deleteblankcolumns(fileNames):
    for files in fileNames:
        csvfile = open((directory + files), newline='', encoding='utf-8')             # I open the file, read the file, and convert it to a list
        filecontent = csv.reader(csvfile)
        filecontent = list(filecontent)               # innerfilecontent stores the data without the header found in the file
        innerfilecontent = filecontent[1:]            # I establish defaultValues as a set of values to compare the content within columns to the values in the first row
        defaultValues = innerfilecontent[0]           # NullColumns will store the index for the columns that are null
        NullColumns = []                              # I use i to serve as the index for the columns
        for i in range(len(innerfilecontent[0])):     # I use isNullColumn to serve as an indicator of whether the column contains values. 
            isNullColumn = True                       # I then iterate through each line in the file and compare the index i for each row to the corresponding value in the default values list       
            for line in innerfilecontent:
                if line[i] != defaultValues[i]:
                    isNullColumn = False
            if isNullColumn == True: 
                NullColumns.append(i)                 # since nullcolumns stores the values for the columns that are null from smallest to largest, I can't use the data in the order it comes in without messing up the indexing 
        backwardsNullColumns = []                     # of the the filecontent variable's list of lists. I invert the order to act on the list from largest index to smallest to maintain integrity of the data
        for column in NullColumns: 
            backwardsNullColumns = [column] + backwardsNullColumns                                                 # this print statement lets me check how many columns we have before the delete statement is made
        print("The beginning number of metadata fields was " + str(len(filecontent[0])) + " for " + files)         # i use the outer for loop to iterate through each line in file content
        for i in range(len(filecontent)):                                                                          # the inner for loop iterates through the null column list and deletes each null column from every line
            for columns in backwardsNullColumns: 
                del filecontent[i][columns]                                                                        # this print statement lets me check how many columns are present after columns are deleted
        print("The end number of metadata fields was " + str(len(filecontent[0])) + " for " + files)               # these next commands create a new file name for the file, create and open a csv file, write 
        newFileName = "C:\\Users\\eliza\\Code\\PPFileProject\\Output Files\\" + files[:files.index(".")] + "Output.csv"
        newFile = open(newFileName,"w", newline="", encoding='utf-8')
        writer = csv.writer(newFile)
        writer.writerows(filecontent)    
        csvfile.close()


def findlowusecolumns(newfiles,defaultindex):
    csvfile = open((directoryOutput + newfiles), newline='', encoding='utf-8')             # I open the file, read the file, and convert it to a list
    filecontent = csv.reader(csvfile)
    filecontent = list(filecontent)
    counterForColumnUse = [0]*len(filecontent[0])
    defaultValues = filecontent[defaultindex]
    innerfilecontent = filecontent[1::]
    for rowindex in range(len(innerfilecontent)): 
        for columnindex in range(len(filecontent[0])): 
            if innerfilecontent[rowindex][columnindex] != defaultValues[columnindex]:
                counterForColumnUse[columnindex] += 1
    print(newfiles)
    lowusagelist = []
    for counter in range(len(counterForColumnUse)): 
        if counterForColumnUse[counter] < 20: 
            lowusagelist.append([counter,filecontent[0][counter],counterForColumnUse[counter]])
    print("The number of low usage columns is: " + str(len(lowusagelist)))
    print("The low usage columns are: " + str(lowusagelist))
    print("If these columns are merged, the file will have " + str(len(defaultValues) - len(lowusagelist)) + " columns.")
    csvfile.close()    
    return lowusagelist

def addresslowusecolumns(newfiles,indexesToReview,defaultindex): 
    csvfile = open((directoryOutput + newfiles), newline='', encoding='utf-8')             # I open the file, read the file, and convert it to a list
    filecontent = csv.reader(csvfile)
    filecontent = list(filecontent) 
    innerfilecontent = filecontent[1::]
    print()
    print(newfiles)
    for index in indexesToReview: 
        print("The problem values for column number",(int(index[0])+1),"/",index[1],"are:")
        for rowindex in range(len(innerfilecontent)):
            if innerfilecontent[rowindex][index[0]] != filecontent[defaultindex][index[0]]:
                print(innerfilecontent[rowindex][index[0]],end=" AND ")
        print()


deleteblankcolumns(fileList)   

for filename in newFileList: 
    if filename == "WebPPObjectsOutput.csv":
        defaultindex = 59
        lowusagelist = findlowusecolumns(filename,defaultindex)
        #addresslowusecolumns(filename,lowusagelist,defaultindex)
    if filename == "WebPPArchivesOutput.csv":
        defaultindex = 201
        lowusagelist = findlowusecolumns(filename,defaultindex)
        #addresslowusecolumns(filename,lowusagelist,defaultindex)
    if filename == "WebPPLibraryOutput.csv":
        defaultindex = 4
        lowusagelist = findlowusecolumns(filename,defaultindex)
        #addresslowusecolumns(filename,lowusagelist,defaultindex)
    if filename == "WebPPPhotosOutput.csv":
        defaultindex = 1
        lowusagelist = findlowusecolumns(filename,defaultindex)
        #addresslowusecolumns(filename,lowusagelist,defaultindex)
       
    

