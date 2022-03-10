import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import os
import sys
import re

Version = "6.0"
print("GotIssues version "+str(Version))

UserAgent=input("Please enter your main nation's name: ")
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
	every=every.replace(" ", "_").lower()
#	print(every)
#	print(password[index])
	
	r = requests.get('https://www.nationstates.net/cgi-bin/api.cgi/', headers={'User-Agent': UserAgent, 'X-Password': password[index].replace(" ","_")}, params={'nation':every, 'q':'issuesummary'})
	sleep(.7)
	print("Grabbing " + every + "; this can take a while for the server hamsters to give it to the API Gnomes.")
	soup = BeautifulSoup(r.content, "xml")
	for ISSUEid in soup.find_all('ISSUE'):
		print(every)
		with open(NewListOfIssues, 'a+') as f:
			f.write("https://www.nationstates.net/container={}/nation={}/page=show_dilemma/dilemma={}/template-overall=none/x-enabled-by=gotIssues\n".format(every, every, ISSUEid.get('id')))
	index=index+1
	
print("Done, thanks for using GotIssues")
