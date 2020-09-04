import csv
import re
from urllib import request
from bs4 import BeautifulSoup as bs

root_url='https://marshall.pastperfectonline.com'
search_url='/search?utf8=%E2%9C%93&search_criteria=*&page='

output_list = [["Image URL","Record URL","Image File Name","Object ID"]]
# This code grabs the URLs and other info for all records with images in PP
p = 1
while True:
	search_page = request.urlopen(root_url + search_url + str(p))
	search_soup = bs(search_page, 'html.parser')
	search_results = search_soup.find_all(class_="indvImage")
	if len(search_results) < 1: 
		break
	for i in search_results: 
		imageURL = i.select("img")
		recordURL = i.select("a")
		if len(imageURL) < 1 or len(recordURL) < 1:
			continue
		imageURL = imageURL[0]["src"]
		recordURL = recordURL[0]["href"]
		search_record_page = request.urlopen(root_url + recordURL)
		search_record_soup = bs(search_record_page, 'html.parser')
		search_record_results = search_record_soup.find_all(class_="fancybox_record_images")
		image_source = search_record_results[0]["image_src"]
		catalog_number = search_record_results[0]["objectid"]
		if "/thumbs" in imageURL: 
			imageURL = imageURL.replace("/thumbs","")
		output_list.append([imageURL,root_url + recordURL,image_source,catalog_number])
		print(output_list)
	p += 1

with open('ppscraper_output.csv', 'w', newline='') as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerows(output_list)
