import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import os
import sys
import re

Version = "5.5"
print("GotIssues version "+str(Version))

UserAgent=input("Please enter your main nation's name: ")
filename="puppet.csv"
Pulleventmode=input("Would you like to open packs in line while you answer issues (yes or no): ")
Pulleventmode=Pulleventmode.lower().replace(" ","_")

if(Pulleventmode=='y'):
	Pulleventmode='yes';


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
	sleep(.7)
	print("Grabbing " + every + "; this can take a while for the server hamsters to give it to the API Gnomes.")
	soup = BeautifulSoup(r.content, "xml")
	for ISSUEid in soup.find_all('ISSUE'):
		print(every)
		with open(NewListOfIssues, 'a+') as f:
			if(ISSUEid.get('id')=='407'):
				if(Pulleventmode != "yes"):
					f.writelines('https://www.nationstates.net/page=show_dilemma/dilemma=407/template-overall=none'+"/nation="+every+"/container="+every+"/template-overall=none/pulleventmode=true\n")
					print("issue 407")
				else:
					print("issue 407")
					f.writelines('https://www.nationstates.net/page=show_dilemma/dilemma=407/template-overall=none'+"/nation="+every+"/container="+every+"/template-overall=none\n")
			else:
				if(Pulleventmode != "yes"):
					print(ISSUEid.get('id'))
					print(ISSUEid.OPTION.get('id'))
					f.writelines('https://www.nationstates.net/page=enact_dilemma/choice-'+ISSUEid.OPTION.get('id')+'=1/dilemma='+ISSUEid.get('id')+"/nation="+every+"/container="+every+"/template-overall=none\n")
				else:
					print(ISSUEid.get('id'))
					print(ISSUEid.OPTION.get('id'))
					f.writelines('https://www.nationstates.net/page=enact_dilemma/choice-'+ISSUEid.OPTION.get('id')+'=1/dilemma='+ISSUEid.get('id')+"/nation="+every+"/container="+every+"/template-overall=none/pulleventmode=true\n")
		#print('{}'.format(options.get('id')))
		#print('{}'.format(ISSUEid.get('id')))           
	index=index+1
	
print("Done, thanks for using GotIssues")
