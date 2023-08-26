import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import os
import sys
import re

Version = "6.2"
print("GotIssues version "+str(Version))

UserAgent=input("Please enter your main nation's name: ")+"Gotissues Written by 9003, Email NSWA9002@gmail.com,discord: 9003, NSNation 9003"
filename="puppet.csv"
Pulleventmode="no"
Pulleventmode=Pulleventmode.lower().replace(" ","_")


if(Pulleventmode=='y'):
	Pulleventmode='yes';


names=[]
password=[]
NewListOfIssues = 'link_list.txt'
NewListOfPacks = 'pack_list.txt'
with open("puppet.csv") as csv_file:
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		names.append(row[0])
		password.append(row[1])
index=0
if os.path.exists(NewListOfIssues):
  os.remove(NewListOfIssues)

if os.path.exists(NewListOfPacks):
  os.remove(NewListOfPacks)

for every in names:
	every=every.replace(" ", "_")
#	print(every)
#	print(password[index])
	
	r = requests.get('https://www.nationstates.net/cgi-bin/api.cgi/', headers={'User-Agent': UserAgent, 'X-Password': password[index].replace(" ","_")}, params={'nation':every, 'q':'issues+packs'})
	sleep(.7)
	print("Grabbing " + every + "; this can take a while for the server hamsters to give it to the API Gnomes.")
	soup = BeautifulSoup(r.content, "xml")
	with open(NewListOfPacks, "a+") as h:
		count=0
		for toOpenPACKS in soup.find_all('PACKS'):
			#input(toOpenPACKS.text)
			while(count < int(toOpenPACKS.text)):
				count= count+1
				h.writelines(f"https://www.nationstates.net/page=deck/nation={every}/?open_loot_box=1/User_agent={UserAgent}/Script=Gotissues/Author_Email=NSWA9002@gmail.com/Author_discord=9003/Author_main_nation=9003/autoclose=1\n")
		for ISSUEid in soup.find_all('ISSUE'):
			print(every)
			with open(NewListOfIssues, 'a+') as f:
				print(ISSUEid.get('id'))
				f.writelines(f"https://www.nationstates.net/page=show_dilemma/dilemma={ISSUEid.get('id')}/template-overall=none/nation={every}/container={every}/template-overall=none/User_agent={UserAgent}/Author_Email=NSWA9002@gmail.com/Author_discord=9003/Author_main_nation=9003/autoclose=1\n")     
		index=index+1
	
print("Done, thanks for using GotIssues")
