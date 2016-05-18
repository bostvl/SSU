#!/usr/bin/python
import os, sys, json
directory = sys.argv[1]
outfile = sys.argv[2]
files = filter(lambda x: x.endswith('.json'),os.listdir(directory))
data1 = []
maxnumber = -1
for file in files:
	import_file = open(directory+'/'+file)
	data = json.load(import_file)
	import_file.close()
	if (int(data['number']) > maxnumber) and (int(data['result']))>1:
		data1 = data
		maxnumber = int(data['number'])

json.dump(data1, open(outfile, 'w'))
