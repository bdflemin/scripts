#!/bin/bash

# Complete a search on root directory (exclude root)
for i in $(find / -maxdepth 1 -type d | egrep -v "^/$"); 
do 
	#If the directory is /proc, skip
	[ "$i" == "/proc" ] && continue;
	#If the directory is /sys, skip
	[ "$i" == "/sys" ] && continue; 
	echo -ne "$i:\t\t\t"; find $i -type f | wc -l; echo "-------"; 
done

## One Liner
#for i in $(find / -maxdepth 1 -type d | egrep -v "^/$"); do [ "$i" == "/proc" ] && continue; [ "$i" == "/sys" ] && continue; echo -ne "$i:\t\t\t"; find $i -type f | wc -l; echo "-------"; done