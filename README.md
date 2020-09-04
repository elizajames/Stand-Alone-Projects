# Stand-Alone-Programming-Projects-And-Files
This repository contains code from miscellaneous standalone projects including API data harvesting, web scraping, digital preservation, and general digital content management mini-projects. Some of the web scraping code is no longer functional because the base website was updated, but it serves as a representative sample of some of the work I've done in these areas.

Brief overview of directories in this repo: 

EAD Authoring: 
What it says on the tin--I needed an easy way to leverage student/non-technically minded archivists to help convert physical or Word document finding aids into CSVs that could be easily converted into EAD without manual encoding by someone who knew EAD/XML.

FSA-OWI Work
This code gets the URLs, specific metadata, and location coordinate data using the Library of Congress and Mapquest APIs for West Virginia photos in the FSA-OWI collection for data visualization and exploration purposes.

File Deduplication: 
The shared network drive for my institution was overcrowded with a significant number of duplicate files. I needed a way for me to see the locations and checksums for files to easily detect duplicates and get an overview of the number and structure of files in the drive. 

Looking At Appalachia: 
The Looking at Appalachia project is composed of more than 800 photos contributed from individuals throughout the Appalachian region to demonstrate the diversity and complexity of the Appalachian experience. On the project website, the photos are housed in an image carousel and organized by state of origin and feature only plain text unstandardized metadata about each photo. This code harvests and processes the plain text metadata into discrete fields for use in data visualization.

MARC->CSV: 
This project recovered data about individual oral histories that only existed in the library catalog. The catalog could only export records as .txt files and I wrote this script to convert the .txt file to a CSV with fields for the data. I then used the data for data visualization and patron discovery purposes. 

PastPerfect Data Cleanup: 
As a software that focuses on collection management and museum work, PastPerfect has significantly more metadata fields than are often used in an archive. This code detects low use metadata fields and deletes columns/fields that are entirely empty to assist in automating metadata cleanup. 

PastPerfect Web Scraping: 
PastPerfect does not have robust export options for information other than metadata, such as record URLs, URLs for files, and original file names. This code harvests that data for all items in a PastPerfect instance that allowed me to determine what digital files did not have a preservation copy and only existed via the PastPerfect access copy.

Pierpont Telegrams: 
I wanted to explore a collection of digitized Civil War telegrams at West Virginia University that had unique data that would lend itself well to data visualization and study. Because WVU does not have an API endpoint, I had to write code that would scrape the metadata for each item in a systematic way. 

Southern Courier:
WIP-Code to scrape data about 13,000 photographs and 177 newspapers from the Civil Rights Era to explore discovery and data visualization/computational analysis options for the data.
