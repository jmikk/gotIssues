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
    event.widget.insert(END, text)

def generate_issues_list(user_agent, puppet_csv):
    if user_agent == '' or puppet_csv == '':
        text.insert(END, "Missing user agent or puppet list")
        root.update_idletasks()
        return

    text.delete("1.0", "end")
    root.update_idletasks()

    try:
        Version = "5.6"
        text.insert(END, "GotIssues version " + str(Version) + "\n")
        root.update_idletasks()
        
        puppet_csv = puppet_csv.rstrip()
        puppet_lines = puppet_csv.splitlines()
        NewListOfIssues = 'link_list.txt'
        NewListOfPacks = 'pack_list.txt'
        if os.path.exists(NewListOfIssues):
            os.remove(NewListOfIssues)

        if os.path.exists(NewListOfPacks):
            os.remove(NewListOfPacks)

        for line in puppet_lines:

            nation, password = line.split(',')
            index=0

            nation = nation.replace(" ", "_")
            r = requests.get('https://www.nationstates.net/cgi-bin/api.cgi/', headers={'User-Agent': user_agent, 'X-Password': password.replace(" ","_")}, params={'nation':nation, 'q':'issues+packs'})
            soup = BeautifulSoup(r.content, "xml")
            sleep(.7)
            text.insert(END, "Grabbing " + nation + "; this can take a while for the server hamsters to give it to the API Gnomes.")
            root.update_idletasks()
            with open(NewListOfPacks, "a+") as h:
                count=0
                for toOpenPACKS in soup.find_all('PACKS'):
                    while(count < int(toOpenPACKS.text)):
                        count= count+1
                        h.writelines(f"https://www.nationstates.net/page=deck/nation={nation}/?open_loot_box=1/autoclose=1\n")
                for ISSUEid in soup.find_all('ISSUE'):
                    with open(NewListOfIssues, 'a+') as f:
                        if(ISSUEid.get('id')=='407'):
                            f.writelines('https://www.nationstates.net/page=show_dilemma/dilemma=407/template-overall=none'+"/nation="+nation+"/container="+nation+"/template-overall=none/autoclose=1\n")
                        else:
                            f.writelines('https://www.nationstates.net/page=enact_dilemma/choice-'+ISSUEid.OPTION.get('id')+'=1/dilemma='+ISSUEid.get('id')+"/nation="+nation+"/container="+nation+"/template-overall=none/autoclose=1\n")
                index=index+1

        if not os.path.exists('link_list.txt'):
            with open('link_list.txt') as f:
                pass

        if not os.path.exists('pack_list.txt'):
            with open('pack_list.txt') as f:
                pass

        with open('link_list.txt') as f:
            puppets = f.read().split('\n')

        with open('pack_list.txt') as h:
            packs = h.read().split('\n')

        puppets = list(filter(None, puppets))
        totalcount = len(puppets)
        text.insert(END, 'The total count of issues is', totalcount, ' now generating html, this will take a bit...')
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
        text.insert(END, "Done, thanks for using GotIssues")
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        text.insert(END, error_msg + "\n")


root = Tk()
root.title("Got Issues GUI")
root.geometry("500x400")

frame = Frame(root, bg='grey', bd=1)
frame.pack(expand=True, fill=BOTH, padx=10, pady=10)

user_agent = Entry(frame, font=('', 10), width=40)
user_agent.grid(row=0, column=1, columnspan=2, pady=5)

user_agent_label = Label(frame, text="Enter your main nation's name:", font=(20))
user_agent_label.grid(row=1, column=0, sticky='w', padx=5)

puppet_csv = Text(frame, font=('', 10), width=40, height=5)
puppet_csv.grid(row=2, column=1, columnspan=2, pady=5)

puppet_info_label = Label(frame, text="Put your puppets in here with this format: name,password", font=(20))
puppet_info_label.grid(row=3, column=0, columnspan=2, pady=5)

button = Button(frame, text="Generate", font=40, command=lambda: generate_issues_list(user_agent.get(), puppet_csv.get("1.0", "end")))
button.grid(row=4, column=1, columnspan=2, pady=10)

text = Text(frame, font=('', 10), wrap=WORD, width=50, height=15)
text.grid(row=5, column=0, columnspan=3, pady=5)
text.bind("<Control-v>", on_paste)

filename = "puppet.csv"
try:
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            puppet_csv.insert(END, f"{row[0]},{row[1]}\n")
except FileNotFoundError:
    print(f"{filename} not found.")

root.mainloop()