import scrap_espace_fr
import scrap_espace_word
import export_to_xml
import my_mail
import sys
reload(sys)
sys.setdefaultencoding("utf-8")



def Scrap(mail,export_arg,keywords,databases):
	for i in databases : 
		if i=='f':
			print "googo"
			scrap_espace_fr.scrap_multi_keyword(keywords)
		elif i =='w':
			scrap_espace_word.scrap_multi_keyword(keywords)
	export_to_xml.export(export_arg)
	my_mail.send_mail(mail,keywords)

mail = "benedict.hanser@gmail.com"
export = "i"
keywords=["zob"]
databases = "p"

Scrap(mail,export,keywords,databases)

