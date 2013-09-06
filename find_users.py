from re import findall
from subprocess import check_output
from pwd import getpwall

d = {}
filesearch = open("/etc/login.defs","r")

for line in filesearch:
	if findall("^UID_(MIN|MAX)",line):
		a = line.strip().split()
		d[str(a[0])] = str(a[1])

filesearch.close()

for p in getpwall():
	if int(p[2]) >= int(d['UID_MIN']) and int(p[2]) <= int(d['UID_MAX']):
		print p[0]