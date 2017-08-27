######################################
## SCRAPER FOR THE OFFICE SCRIPTS
## WRITTEN BY TIM KROCK
######################################

import unicodedata
#import the library used to query a website
import urllib2

eplist = [['01','02','03','04','05','06'],
	  ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22'],
	  ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23'],
	  ['01','02','03','04','05','06','08','09','10','11','12','13','14'],
	  ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'],
          ['01','02','03','04','05','06','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']]

for i in range(9):
	season = (i+1)
	season.__str__()
	for j in eplist[i]:
		ep = j
	

		wiki = 'http://officequotes.net/n' + season  + '-' +ep+ '.php'

		#Query the website and return the html to the variable 'page'
		page = urllib2.urlopen(wiki)

		#import the Beautiful soup functions to parse the data returned from the website
		from bs4 import BeautifulSoup

		#Parse the html in the 'page' variable, and store it in Beautiful Soup format
		soup = BeautifulSoup(page)
		#print soup.prettify()
		outfile = 'outputs/'+season+'-'+ep
		textfile = open(outfile, 'w')
		string = soup.get_text()[72605:-609]

		new_str = unicodedata.normalize('NFKD', string).encode('utf-8').decode('ascii', 'ignore')
		textfile.write(new_str)
		textfile.close()









