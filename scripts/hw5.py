#!/usr/bin/python
import os,sys
import sqlite3
dbname = sys.argv[1]
db = os.path.join(os.path.dirname(__file__), dbname)
sql = '''
	UPDATE ServerPorts 
	SET port_number = 443   
	WHERE ServerPorts.servers_id  in   
	(SELECT Servers.id FROM Servers
        INNER JOIN ServerTypes
        ON Servers.servertypes_id=ServerTypes.id
        WHERE ServerTypes.type_name='apache' 
        AND Servers.id in (
		SELECT Servers_id FROM ServerProjects
	        INNER JOIN Projects
	        ON ServerProjects.projects_id=Projects.id
	        WHERE Projects.proj_name='Project3'
		)
	) 
	  ;'''
 
conn = sqlite3.connect(db)
result = conn.execute(sql)
conn.close()
