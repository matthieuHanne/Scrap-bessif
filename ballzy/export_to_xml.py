#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom.minidom import Document 

import sqlite3

#create database connection

conn = sqlite3.connect("Base_brevet.db")

cur = conn.cursor()

#retrieve all database data

cur.execute("SELECT * FROM table_brevet")

#create a new XML object


doc = Document()
allNodes = doc.createElement("tablebrevet")

doc.appendChild(allNodes)


#popolate XML with database data

brevet= cur.fetchone()

while brevet:

	entity_descriptor = doc.createElement("brevet")
	entity_descriptor.setAttribute('date',str(brevet[2]))
	entity_descriptor.setAttribute('id',str(brevet[0]))
	#entity_descriptor.setAttribute('signet',brevet[1])
	#entity_descriptor.setAttribute('numdemande',str(brevet[3]))
	#entity_descriptor.setAttribute('numpriorite',str(brevet[4]))
	#entity_descriptor.setAttribute('contenu', brevet[5])
	allNodes.appendChild(entity_descriptor)
	brevet=cur.fetchone()



#show in console the final XML
f = open("temp_xml.xml", 'wb')	
u = doc.toprettyxml()
f.write(u)
f.close()


