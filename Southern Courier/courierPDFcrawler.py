from bs4 import BeautifulSoup
import urllib.request
CourierPageURLs = ["http://www.southerncourier.org/archives.html","http://www.southerncourier.org/archives2.html","http://www.southerncourier.org/archives3.html","http://www.southerncourier.org/archives4.html"]
CourierBaseURL = "http://www.southerncourier.org/"
PDFurls = []
def getPDFs(CourierPageURLs):
    for URL in CourierPageURLs:
        linkopen = urllib.request.urlopen(URL)
        soup = BeautifulSoup(linkopen, "html.parser")
        results = soup.find_all("a")   
        for i in results: 
            if "hi-res" in i.get('href'): 
                PDFurls.append((CourierBaseURL + i.get('href')))
    return PDFurls
print(getPDFs(CourierPageURLs))


