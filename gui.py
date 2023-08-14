from tkinter import *
import requests
import pathlib
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import os
import sys
import re

# with pyinstaller
# pyinstaller --windowed --icon=memo.ico --name=GotIssues --onefile gui.py

counter = 0
fileLocation = pathlib.Path(__file__).parent.resolve()

def on_paste(event):
    text = event.widget.selection_get(selection="CLIPBOARD")
    event.widget.insert("end", text)

def generate_issues_list(user_agent, puppet_csv):
    if user_agent == '' or puppet_csv == '':
        text.insert("end", "Missing user agent or puppet list")
        root.update_idletasks()
        return

    text.delete("1.0", "end")
    root.update_idletasks()

    try:
        Version = "6.1"
        text.insert("end", "GotIssues version " + str(Version) + "\n")
        root.update_idletasks()
        
        puppet_csv = puppet_csv.rstrip()
        puppet_lines = puppet_csv.splitlines()
        NewListOfIssues = 'link_list.txt'
        NewListOfPacks = 'pack_list.txt'
        if os.path.exists('link_list.txt'):
            os.remove(NewListOfIssues)

        if os.path.exists('pack_list.txt'):
            os.remove(NewListOfPacks)

        for line in puppet_lines:

            nation, password = line.split(',')
            index=0

            nation = nation.replace(" ", "_")
            r = requests.get('https://www.nationstates.net/cgi-bin/api.cgi/', headers={'User-Agent': user_agent, 'X-Password': password}, params={'nation':nation, 'q':'issues+packs'})
            soup = BeautifulSoup(r.content, "xml")
            sleep(.7)
            text.insert("end", "Grabbing " + nation + "; this can take a while for the server hamsters to give it to the API Gnomes.\n")
            root.update_idletasks()
            with open(NewListOfPacks, "a+") as h:
                count=0
                for toOpenPACKS in soup.find_all('PACKS'):
                    while(count < int(toOpenPACKS.text)):
                        count= count+1
                        h.writelines(f"https://www.nationstates.net/page=deck/nation={nation}/?open_loot_box=1/User_agent={UserAgent}/Script=GotissuesGUI/Author_Email=NSWA9002@gmail.com/Author_discord=9003/Author_main_nation=9003/autoclose=1\n")
            with open(NewListOfIssues, 'a+') as f:
                for ISSUEid in soup.find_all('ISSUE'):
                    if(ISSUEid.get('id')=='407'):
                        f.writelines('https://www.nationstates.net/page=show_dilemma/dilemma=407/template-overall=none'+"/nation="+nation+"/container="+nation+"/template-overall=none/User_agent="+UserAgent+"/Script=GotissuesGUI/Author_Email=NSWA9002@gmail.com/Author_discord=9003/Author_main_nation=9003/autoclose=1\n")
                    else:
                        f.writelines('https://www.nationstates.net/page=enact_dilemma/choice-'+ISSUEid.OPTION.get('id')+'=1/dilemma='+ISSUEid.get('id')+"/nation="+nation+"/container="+nation+"/template-overall=none/User_agent=+"UserAgent+"/Script=GotissuesGUI/Author_Email=NSWA9002@gmail.com/Author_discord=9003/Author_main_nation=9003/autoclose=1\n")
            index=index+1

        with open('link_list.txt') as f:
            puppets = f.read().split('\n')

        with open('pack_list.txt') as h:
            packs = h.read().split('\n')

        puppets = list(filter(None, puppets))
        totalcount = len(puppets)
        text.insert("end", 'The total count of issues is', totalcount, ' now generating html, this will take a bit...\n')
        root.update_idletasks()
        links = open('9003samazinglistofcards.html', 'w')

        links.write("""
        <html>
        <head>
        <style>
        td.createcol p {
            padding-left: 10em;
        }

        a {
            text-decoration: none;
            color: black;
        }

        a:visited {
            color: grey;
        }

        table {
            border-collapse: collapse;
            display: table-cell;
            max-width: 100%;
            border: 1px solid darkorange;
        }

        tr, td {
            border-bottom: 1px solid darkorange;
        }

        td p {
            padding: 0.5em;
        }

        tr:hover {
            background-color: lightgrey;
        }

        </style>
        </head>
        <body>
        <table>
        """)

        for idx, k in enumerate(puppets):
            canonical = k.lower().replace(" ", "_")
            escaped_canonical = re.escape(canonical)
            links.write("""<tr>""");
            links.write("""<td>{} of {}</td>""".format(idx+1, totalcount));
            links.write("""<td><p><a target="_blank" href="{}">Link to Card</a></p></td>""".format(canonical, canonical, canonical))
            links.write("""</tr>\n""")

        for each in packs:
            each = each.lower().replace(" ", "_")
            links.write("""<tr>""");
            links.write("""<td>X of X</td>""")
            links.write(f'<td><p><a target="_blank" href="{each}">Link to Card</a></p></td>')
            links.write("""</tr>\n""")

        links.write("""<td><p><a target="_blank" href="https://this-page-intentionally-left-blank.org/">Done!</a></p></td><td><p><a target="_blank" href="https://this-page-intentionally-left-blank.org/">Done!</a></p></td>""")
        links.write("""
        </table>
        <script>
        document.querySelectorAll("td").forEach(function(el) {
            el.addEventListener("click", function() {
                let myidx = 0;
                const row = el.parentNode;
                let child = el;
                while((child = child.previousElementSibling) != null) {
                    myidx++;
                }
                row.nextElementSibling.childNodes[myidx].querySelector("p > a").focus();
                row.parentNode.removeChild(row);
            });
        });
        </script>
        </body>
        """)
        text.insert("end", "Done, thanks for using GotIssues")
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        text.insert("end", error_msg + "\n")


root = Tk()
root.title("Got Issues GUI")
root.geometry("500x500")

frame = Frame(root, bg='grey', bd=1)
frame.pack(expand=True, fill=BOTH, padx=10, pady=10)

user_agent_label = Label(frame, text="Enter your main nation's name:", font=(20))
user_agent_label.pack(fill="x")

user_agent = Entry(frame, font=('', 10), width=40)
user_agent = user_agent + "GotIssuesGUI, Written by 9003 and Scramble, Email: NSWA9002@gmail.com,Discord 9003"
user_agent.pack(fill="x", pady=5)

puppet_info_label = Label(frame, text="Put your puppets in here with this format: name,password", font=(20))
puppet_info_label.pack(fill="x")

puppet_csv = Text(frame, font=('', 10), width=40, height=10)
puppet_csv.pack(fill="both", expand=True)

button = Button(frame, text="Generate", font=40, command=lambda: generate_issues_list(user_agent.get(), puppet_csv.get("1.0", "end")))
button.pack(fill="x")

text_frame = Frame(frame, bg='grey', bd=1)
text_frame.pack(expand=True, fill=BOTH, pady=5)

text_label = Label(text_frame, text="Output:", font=(20))
text_label.pack(fill="x")

text = Text(text_frame, font=('', 8), wrap=WORD, width=50, height=5)
text.pack(fill="both", expand=True)

puppet_csv.bind("<Control-v>", on_paste)

root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(3, weight=0)

text.config(font=('', 8))

filename = "puppet.csv"
try:
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            puppet_csv.insert("end", f"{row[0]},{row[1]}\n")
except FileNotFoundError:
    print(f"{filename} not found.")

root.mainloop()
