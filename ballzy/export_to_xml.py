#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom.minidom import Document 

import sqlite3
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#create database connection


#retrieve all database data



def add_item_to_xml (type_item):
	global current_n_id
	global current_e_id
	global cur
	global to_write_node
	global to_write_edge
	global f 
	global g

	request1 = "SELECT * from table_"+type_item+" ORDER BY NAME"
	cur.execute(request1)
	item =cur.fetchone()
	cmpt=0
	new_item_name=item[0]
	old_item_name=""
	cmpt_occurence = 1
	first = 1 ;
	while item:
		if first : 
			first=0
			old_item_name=item[1]
			to_write_edge+=str(current_n_id)+","+str(item[2])+",Undirected,"+str(current_e_id)+","+type_item+"_brevet\n"
			#g.write(to_write_edge)
			current_e_id+=1
		else :
			
			if old_item_name!=new_item_name:
				to_write_node+=old_item_name+","+str(current_n_id)+","+type_item+"_"+str(cmpt)+","+type_item+","+str(cmpt_occurence)+", , , , ,\n"
				#f.write(to_write_node)				
				current_n_id+=1
				cmpt+=1
				cmpt_occurence=1
				to_write_edge+=str(current_n_id)+","+str(item[2])+",Undirected,"+str(current_e_id)+","+type_item+"_brevet\n"
				#g.write(to_write_edge)
				current_e_id+=1
			else:
				cmpt_occurence+=1
				to_write_edge+=str(current_n_id)+","+str(item[2])+",Undirected,"+str(current_e_id)+","+type_item+"_brevet\n"
				#g.write(to_write_edge)
				current_e_id+=1
		old_item_name=item[1]
		item=cur.fetchone()
		if item:
			new_item_name=item[1]
	
	to_write_node+=old_item_name+","+str(current_n_id)+","+type_item+"_"+str(cmpt)+","+type_item+","+str(cmpt_occurence)+", , , , ,\n"
	current_n_id+=1
	#f.write(to_write_node)		 

def add_brevet_to_xml ():
	global current_n_id
	global cur
	global to_write_node
	global f
	global g
	cur.execute("SELECT * FROM table_brevet")
	item =cur.fetchone()
	while item:
		to_write_node+=item[1]+","+str(item[0])+","+"brevet_"+str(item[0])+",brevet"+",1,"+item[2]+","+item[3]+", ,"+item[6]+"\n"
		#print to_write_node
		#f.write(to_write_node)
		current_n_id = item[0]
		item=cur.fetchone()
	
		

to_write_node = "Signet,Id,Label,Type,Occured,Date,Num_demande,Num_priorite,link\n"
to_write_edge = "Source,Target,Type,Id,Type_edge\n"
f = open("temp_node.csv", 'wb')	
g = open("temp_edge.csv", 'wb')	

conn = sqlite3.connect("Base_brevet.db")
cur = conn.cursor()
current_n_id=0
current_e_id=0
add_brevet_to_xml()
add_item_to_xml ("inventeur")
add_item_to_xml ("demandeur")
add_item_to_xml ("classification_int")
add_item_to_xml ("abrege_pour")
add_item_to_xml ("keyword")

#show in console the final XML
g.write(to_write_edge)
f.write(to_write_node)


f.close()


g.close()

