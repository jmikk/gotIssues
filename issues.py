import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import os
import sys

Version = 1.2
print("This is Version: "+str(Version))

UserAgent=input("Please enter your main nations name: ")
filename="puppet.csv"

names=[]
password=[]
NewListOfIssues = 'link_list.txt'
with open("puppet.csv") as csv_file:
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		names.append(row[0])
		password.append(row[1])
index=0

if os.path.exists(NewListOfIssues):
  os.remove(NewListOfIssues)

for every in names:
	every=every.replace(" ", "_")
#	print(every)
#	print(password[index])		
	r = requests.get('https://www.nationstates.net/cgi-bin/api.cgi/', headers={'User-Agent': UserAgent, 'X-Password': password[index].replace(" ","_")}, params={'nation':every, 'q':'issues'})
	sleep(.8)
	print("grabing " + every + " this can take up to a secound depending on if the server hamsters are playing nice with the API Gnome.")
	soup = BeautifulSoup(r.content, "xml")
	for ISSUEid in soup.find_all('ISSUE'):
		print(every)
		print(ISSUEid.get('id'))
		print(ISSUEid.OPTION.get('id'))
		with open(NewListOfIssues, 'a+') as f:
			# https://www.nationstates.net/nation=PUPPET/page=enact_dilemma/choice-1=1/dilemma=26
			if(ISSUEid.get('id')=='407'):
				f.writelines('https://www.nationstates.net/page=show_dilemma/dilemma=407/')
			else:
				f.writelines('https://www.nationstates.net/page=enact_dilemma/choice-'+ISSUEid.OPTION.get('id')+'=1/dilemma='+ISSUEid.get('id')+"/nation="+every+"/container"+every+"\n")
		#print('{}'.format(options.get('id')))
		#print('{}'.format(ISSUEid.get('id')))           
	index=index+1

print("Done thanks for running this with CMD")

