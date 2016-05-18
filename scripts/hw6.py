#!/usr/bin/python
import os,sys,dockermap.api

docker_url = 'unix://var/run/docker.sock'

if len(sys.argv) == 1:
	print "Please enter tag name as argument"
	sys.exit(1)
else:
	tag_name = sys.argv[1]

docker_conn = dockermap.api.DockerClientWrapper(docker_url)
docker_file = dockermap.api.DockerFile('centos7/hw', maintainer='bostvl@gmail.com')
docker_file.run_all(' echo "Homework6!">/index.html')
docker_conn.build_from_file(docker_file, tag_name)
container_id = docker_conn.create_container(image=tag_name, command='python -m  SimpleHTTPServer 80').get('Id')
docker_conn.start(container=container_id)

