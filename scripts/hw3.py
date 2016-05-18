#!/usr/bin/python
import sys
import paramiko

host = sys.argv[1]
port = int(sys.argv[2])
uname = sys.argv[3]
path = sys.argv[4]
prefix = sys.argv[5]
counts = int(sys.argv[6])
mode = sys.argv[7]

passwd = raw_input("Please input password: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=uname, password=passwd) 

for i in range(1,counts+1):
  dir = path+'/'+prefix+str(i)
  ssh.exec_command("mkdir -p "+dir)
  ssh.exec_command("chmod "+mode+" "+dir)
ssh.close()
