# printa alla klämdagar i ett år givet av kommandoraden
# author: Robert Sebescen (pgrobban at gmail dot com)

import sys
import urllib.request
import json
import datetime
import locale

try: # check if locale exists
	locale.setlocale(locale.LC_ALL, "sv_SE.UTF-8")
except:
	pass

if len(sys.argv) < 2:
	year = datetime.date.today().year
else:
	year = sys.argv[1]

response = urllib.request.urlopen('http://api.dryg.net/dagar/v2.1/' + str(year))
data = json.loads(response.read().decode("utf-8"))   

print("\nKlämdagar för {0}:".format(year))
count = 0
for day in data["dagar"]:
	if "klämdag" in day:
		#print(calendar.month_name(day["datum"]))
		s = datetime.datetime.strptime(day["datum"], "%Y-%m-%d")
		print(s.strftime("%A %d %B"))
		count += 1

print("\n= Totalt {0} {1}\n".format(count, "dag" if count == 1 else "dagar"))

