#!/usr/bin/env python3

import re


with open('link_list.txt') as f:
	puppets = f.read().split('\n')

puppets = list(filter(None, puppets))

#containerise_rules = open('containerise.txt', 'w')
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

#containerise_rules.write("@^.*\.nationstates\.net/(.*/)?nation=9003(/.*)?$ , 9003\n")
for k in puppets:
	canonical = k.lower().replace(" ", "_")
	escaped_canonical = re.escape(canonical)
	#containerise_rules.write("@^.*\.nationstates\.net/(.*/)?nation={}(/.*)?$ , {}\n".format(escaped_canonical, k))
	links.write("""<tr>""");
	#links.write("""<td><p><a target="_blank" href="https://www.nationstates.net/nation={}/page=dilemmas/template-overall=none">Issues</a></p></td>""".format(canonical))
	#links.write("""<td><p><a target="_blank" href="https://www.nationstates.net/nation={}/page=deck">Deck</a></p></td>""".format(canonical))
	#links.write("""<td><p><a target="_blank" href="https://www.nationstates.net/nation={}/page=deck/value_deck=1/template-overall=none">Value Deck (nostyle)</a></p></td>""".format(canonical))
	#links.write("""<td><p><a target="_blank" href="https://www.nationstates.net/nation={}/page=deck/value_deck=1">Value Deck</a></p></td>""".format(canonical))
	links.write("""<td><p><a target="_blank" href="{}/auto">Link to Card</a></p></td>""".format(canonical, canonical, canonical))
	#links.write("""<td><p><a target="_blank" href="https://www.nationstates.net/nation={}/page=telegrams">Telegrams</a></p></td>""".format(canonical))
	#links.write("""<td><p><a target="_blank" href="https://www.nationstates.net/nation={}/page=settings">Settings</a></p></td>""".format(canonical))
	#links.write("""<td><p><a target="_blank" href="https://www.nationstates.net/nation={}/page=tgsettings">TG settings</a></p></td>""".format(canonical))
	# links.write("""<td><p><a target="_blank" href="https://www.nationstates.net/nation={}/page=zombie_control">Zombie Control</a></p></td>""".format(canonical))
	#links.write("""<td class="createcol"><p><a target="_blank" href="https://www.nationstates.net/nation={}/page=blank/template-overall=none/x-ns-cp?x-nsh-nation={}">Create {}</a></p></td>""".format(canonical, k.replace(" ", "_"), canonical))	links.write("""</tr>\n""")
	links.write("""</tr>\n""")
links.write("""<td><p><a target="_blank" href="https://this-page-intentionally-left-blank.org/">Done!</a></p></td>""".format(canonical))
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
