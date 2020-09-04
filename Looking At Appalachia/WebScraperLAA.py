'''
Explanation of broad goal for this code: 
This code seeks to gather metadata for photographs on the site https://lookingatappalachia.org/, which collects photos taken throughout the Appalachian region. Metadata will include photographer, date, county, and state.
The metadata will then be exported to a CSV file, the number of entries for each county calculated, and county information connected to FIPS geographic codes.
The resulting data set will be used to create a data visualization to map the number of photo contributions at the county level as well as the counties represented in the Looking at Appalachia project.
Prior to beginning this project I analyzed the format/structure of existing metadata to determine what information existed consistently for every photograph as well as how the metadata is encoded in the HTML. 
I am intentionally pulling more information than is strictly needed for the data visualization to provide flexibility on future projects.

Explanations of variables used: 
stateslist is a variable for storing the URLs I want to search - the website has photographs broken down by state
statelist is a variable for storing the "pretty" version of stateslist
metadata is a list of lists of data for each photograph
metadataitem is a list of data for an individual photograph
county/state/photographer/date are variables for the four pieces of metadata represented in each photograph. They are collected in metadataitem which is appended to metadata.
regexname/regexcounty/regexdate are regular expressions to locate the relevant metadata
'''
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import time
stateslist = ["alabama","georgia","kentucky","maryland","mississippi","new-york","north-carolina","ohio","pennsylvania","south-carolina","tennessee","virginia","west-virginia"]
metadata = []
county = ""
state = ""
photographer = ""
date = ""
regexname = re.compile(r'[A-Z][a-z]* [A-Z][a-z]*[A-Z]*[a-z]*')
regexdate = re.compile(r'\d{4}')
regexcounty = re.compile(r'[A-Z][a-z]*[A-Z]*[a-z]* County')
statelist = ["Alabama","Georgia","Kentucky","Maryland","Mississippi","New York","North Carolina","Ohio","Pennsylvania","South Carolina","Tennessee","Virginia","West Virginia"]
# this for loop iterates through the thirteen URLs whose data I wish to scrape
for i in range(len(stateslist)):
    linkopen = urllib.request.urlopen("https://lookingatappalachia.org/" + stateslist[i])
    soup = BeautifulSoup(linkopen, "html.parser")
    results = soup.find_all("div","image-description")
    urlresults = soup.find_all("div","slide")

    '''
    The variable "results" saves a list of matches for the HTML source code I supplied. This particular HTML tag stores the metadata for images. 
    It stores data like this: "<div class="image-description"><p><a href="http://robculpepper.com/">Rob Culpepper</a>. October 3, 2015. Sandy at the fiddlers convention in Athens, Limestone County, Alabama.</p></div>"
    '''    
    # this loop iterates through each item in the list of matches from the original URL. it uses regular expressions to find metadata for photograph, date, and county. the data for state is pulled from the URL.
    for j in range(len(results)):
        workingData = results[j].text
        workingURL = urlresults[j]
        metadataitem = []
        name = regexname.search(workingData)
        name = name.group(0)
        date = regexdate.search(workingData)
        if date:
            date = date.group(0)
        else: 
            date = "no date value found"
        if "County" in workingData: 
            lastindex = workingData.rindex("County")
            county = regexcounty.findall(workingData[lastindex-20:])
        else: 
            county = ["county data not present"]
        state = statelist[i]        
        if workingURL.has_attr("data-slide-url"):
            url = workingURL["data-slide-url"]
            url = "https://lookingatappalachia.org/" + stateslist[i] + "/" + url
        # each piece of metadata for a photograph is added the the list "metadataitem"
        metadataitem = metadataitem + [name]
        metadataitem = metadataitem + [date]
        metadataitem = metadataitem + county
        metadataitem = metadataitem + [state]
        metadataitem = metadataitem + [url]
        # the resulting "metadataitem" list for one photograph is then added to a list of lists containing metadata for all of the other photographs
        metadata.append(metadataitem)
    time.sleep(10)
print(metadata)
with open("output.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(metadata)
 
