#!/usr/bin/python
import os, xml.sax

class Rez:
	id = ''
	number = ''
	committer_name = '' 
	committer_email = '' 

class MyContentHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.currentdata = name
        if name == 'user':
            User.uname = attrs.get('name')

    def endElement(self, name):
        if name == 'user':
            if User.utype=='system':
                User.utype = '--system'
            else:
                User.utype = ''
            
            os.system('useradd ' + User.uname + ' ' + User.utype + ' ' + '--comment "' + User.udescr +'"')
        self.currentdata = ''

    def characters(self, content):
        if self.currentdata == "description":
            User.udescr = content
        elif self.currentdata == "type":
            User.utype = content


input_file = open('users2.xml')
xml.sax.parse(input_file, MyContentHandler())
input_file.close()
