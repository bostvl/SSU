#!/usr/bin/python
import os,sys
path=sys.argv[1]
dir=sys.argv[2]
count=int(sys.argv[3])+1
rights=int(sys.argv[4],8)

for i in range(1,count):
	fld = os.path.join(path,dir+str(i))
	os.mkdir(fld)
	os.chmod(fld,rights)
