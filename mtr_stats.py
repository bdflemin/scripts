import sqlite3 as lite
import sys
import argparse
from time import strftime
from subprocess import check_output


def collect():
  # Grab information from mtr
  output = check_output(["mtr","-nr","-c5","50.56.142.146"])
  date = strftime('%Y%m%d %H%M')
  
  # split the data into an array and clean up array a bit
  a = output.split("\n")
  del a[0]
  del a[-1]

  # Connect to the sqlite3 server to place the information into it
  con = lite.connect('/root/icmp/data.db')
  cur = con.cursor()

  # loop through the data and store information into sqlite
  for i in a:
    array = i.replace("%","").split()
    del array[0]
    cur.execute("insert into netreport values ('%s','%s',%0.1f,%i,%0.1f,%0.1f,%0.1f,%0.1f,%0.1f);" % 
    (str(date), str(array[0]), float(array[1]), int(array[2]), float(array[3]), float(array[4]), float(array[5]), float(array[6]), float(array[7]),))
    con.commit()
  if con:
    con.close()

if __name__ == '__main__':
  collect()