#!/bin/bash

usage() {
	echo "Please use process as root.. exiting"
	exit 1
}

[[ `id -u` -ne 0 ]] && usage

echo "-------";
# Complete a search on root directory (exclude root)
for i in $(find / -maxdepth 1 -type d | egrep -v "^/$" | sort); 
do 
	#If the directory is /proc, skip
	[[ "$i" == "/proc" ]] && continue;
	#If the directory is /sys, skip
	[[ "$i" == "/sys" ]] && continue;
	#If the directory 
	echo -ne "$i:\t\t\t"; find $i -type f | wc -l; echo "-------"; 
done
echo -ne "/:\t\t\t"; find / -type f | wc -l;
echo "-------";

## One Liner (run as root) ##
#for i in $(find / -maxdepth 1 -type d | egrep -v "^/$" | sort); do [ "$i" == "/proc" ] && continue; [ "$i" == "/sys" ] && continue; echo -ne "$i:\t\t\t"; find $i -type f | wc -l; echo "-------"; done echo -ne "/:\t\t\t"; find / -type f | wc -l; echo "-------";