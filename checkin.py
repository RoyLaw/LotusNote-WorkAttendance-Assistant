#coding: utf-8

from datetime import *
import time
import urllib
import httplib
import sys
import os

#some server info needs to be modified

#login
username = u'用户名'
password = '密码'

#log file
logfile = '\logfile.dat'
logfile = sys.path[0]+logfile

def checkIn(username , password) :
	#params for login
	username = username.encode('gb2312')
	sub = u'提交查询内容'.encode('gb2312')
	params4login = urllib.urlencode({'Username' : username , 'Password': password, 'RedirectTo' : 'http://127.0.0.1/main/main.nsf/formIndex?Openform' , 'sub' : sub})

	#headers for login
	headers4login = {"Accept": "image/gif, image/jpeg, image/pjpeg, image/pjpeg, application/x-shockwave-flash, application/xaml+xml, application/vnd.ms-xpsdocument, application/x-ms-xbap, application/x-ms-application, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*" ,
	"Referer": "http://127.0.0.1:8080/jsp/load_sessionsk.jsp",
	"Accept-Language": "zh-cn",
	"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
	"Content-Type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "gzip, deflate",
	"Host": "127.0.0.1",
	"Proxy-Connection": "Keep-Alive",
	"Pragma": "no-cache"}

	#login request
	conn = httplib.HTTPConnection("127.0.0.1", 80)
	conn.request('POST', '/names.nsf?Login', params4login, headers4login)
	#print conn.getresponse().read()
	#print conn.getresponse().getheaders()
	DomAuth = conn.getresponse().getheader('Set-Cookie')
	DomAuth = DomAuth[14:46]

	#params for checkin
	today = date.today()
	year = today.year
	month = today.month
	params4checkin = urllib.urlencode({'Suser' : username , '__Click': '48256E4C0012D738.8d538fe28d969d2d48256c3b0043dd7f/$Body/0.1C2A', '%%Surrogate_CYear' : '1' , 'CYear' : year , '%%Surrogate_CMonth' : '1' , 'CMonth' : month})

	#headers for checkin
	headers4checkin = {"Accept": "image/gif, image/jpeg, image/pjpeg, image/pjpeg, application/x-shockwave-flash, application/xaml+xml, application/vnd.ms-xpsdocument, application/x-ms-xbap, application/x-ms-application, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*" ,
	"Referer": "http://127.0.0.1/checkin.nsf/bykqjl?openform",
	"Accept-Language": "zh-cn",
	"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
	"Content-Type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "gzip, deflate",
	"Host": "127.0.0.1",
	"Proxy-Connection": "Keep-Alive",
	"Pragma": "no-cache",
	"Cookie" : "DomAuthSessId="+DomAuth}

	#checkin request
	conn.request('GET', '/checkin.nsf/bykqjl?openform', headers = headers4checkin)
	conn.close()
	time.sleep(1)
	conn = httplib.HTTPConnection("127.0.0.1", 80)
	conn.request('POST', '/checkin.nsf/bykqjl?OpenForm&Seq=1', params4checkin, headers4checkin)
	conn.close()
	
try	:
	checkIn(username , password)
	f = open(logfile , 'a')
	print >> f , datetime.now() , 'STATUS: OK'
	f.close()
except :
	f = open(logfile , 'a')
	print >> f , datetime.now() , 'STATUS: ERR'
	f.close()

