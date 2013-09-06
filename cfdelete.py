#!/usr/bin/python
import pyrax, time, sys, multiprocessing, argparse, os, __builtin__

parser = argparse.ArgumentParser(description='Remove Cloud Files Fast')
parser.add_argument('--container', nargs='?', dest='cont', required=True, help="The Cloud Contain To Remove Objects From")
parser.add_argument('--username', nargs='?', dest='username', help="Your Cloud Username")
parser.add_argument('--password', nargs='?', dest='password', help="Your Cloud API Key")
parser.add_argument('--file', nargs='?', dest='file', help="Your Cloud API Key File")
parser.add_argument('--region', nargs='?', dest='region', help="Set the Cloud File region")
args = parser.parse_args()

def authenticate(username='', passwd='', path=''):
	if username or passwd:
		pyrax.set_credentials(username,passwd)
	elif path:
		pyrax.set_credential_file(os.path.expanduser(path))
	else:
		print "Authentication Failed... please use username/password or file to authenticate"
		sys.exit()

def worker(num):
	try:
		global obj
		print "Deleting:", obj[num].name
		obj[num].delete()
		#time.sleep(1 + random.random()*5)
		#print num
	except:
		print "Unexpected error in worker:", sys.exc_info()
		raise

def pooling(length):
	try:
		pool = multiprocessing.Pool(processes=20)
		for num in xrange(length):
			pool.apply_async(worker, [num])
			#pool.apply(worker,[num])
			pool.apply_async(time.sleep, 5)
		pool.close()
		pool.join()
	except:
		print "Unexpected error in pooling:", sys.exc_info()[0]
		raise

if __name__ == "__main__":
	authenticate(username=args.username,passwd=args.password,path=args.file)
	cf = pyrax.connect_to_cloudfiles(region=args.region)
	limit = 10000
	marker = ""
	obj = cf.get_container(args.cont).get_objects(limit=limit, marker=marker)
	while obj:
		try:
			marker = obj.pop()
			length = len(obj)
			pooling(length)
			obj = cf.get_container(args.cont).get_objects(limit=limit, marker=marker.name)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise