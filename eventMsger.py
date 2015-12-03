#2524 final-proj python2.7
#version-0.1
#eventMsger.py  send txt when new events show up!
#--Muzi Ti

import smtplib

username = "timuzi2011@hotmail.com" #txt sent from
password = "tmz19901025"

atttext = "5409980101@txt.att.net" # user cell no. that you send to + @*** at&t gateway// @vtext.com --verizon gate way
message = "this is the message to be sent"

msg = """From: %s
To: %s
Subject: text-message
%s""" % (username, atttext, message)

server = smtplib.SMTP('smtp.live.com',587) #server
server.starttls()#start tls
server.login(username,password)
server.sendmail(username, atttext, msg)#finally send txt
