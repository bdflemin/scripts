#!/usr/bin/python
import pyinotify

class MyEventHandler(pyinotify.ProcessEvent):
	def process_IN_CREATE(self, event):
		print "CREATE event:", event.pathname
	def process_IN_DELETE(self, event):

def main():
	wm = pyinotify.WatchManager()
	wm.add_watch('/home/brya5376/test'), pyinotify.ALL_EVENTS, rec=True)

if __name__ == '__main__':
	main()

# http://www.saltycrane.com/blog/2010/04/monitoring-filesystem-python-and-pyinotify/