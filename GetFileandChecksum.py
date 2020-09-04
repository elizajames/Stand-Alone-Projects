import os
import hashlib
import csv
path = 'C:\\Users\\eliza\\Code\\' # change this to relevant root
# This code grabs the file location, base file name, and checksum for files in a selected directory
files = []
newFileName = "XXXXXXDIRECTORY.csv" # change this to relevant location and final file name
newFile = open(newFileName,"w", newline="")
writer = csv.writer(newFile)
newFile.close()
# r=root, d=directories, f=files
for r, d, f in os.walk(path):
    for file in f:
        file_hash = hashlib.md5()
        openFile = open((os.path.join(r, file)),'rb')
        while chunk := openFile.read(8192):
            file_hash.update(chunk)
        fileDirList = [os.path.join(r, file),file,file_hash.hexdigest()]
        files.append(fileDirList)
        openFile.close()
        if len(files) % 10 == 0: 
            newFile = open(newFileName,"w", newline="")
            writer = csv.writer(newFile)               
            writer.writerows(files) 
            newFile.close()
newFile = open(newFileName,"w", newline="")
writer = csv.writer(newFile)               
writer.writerows(files) 
newFile.close()

