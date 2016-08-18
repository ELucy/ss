#coding:utf-8
import urllib
import urllib2
import sys
import os
import threading
from time import ctime,sleep
# i_headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
data = {'id' : '1150'}
url = 'http://summer12.dxsjy.com/index.php/Index/toupiao'
i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
req = urllib2.Request(url,data = urllib.urlencode(data),headers=i_headers)
def test1(url):
	for i in range(100):
		try:
			res = urllib2.urlopen(req)
			pageinfo = res.read() 
			print pageinfo
		except urllib2.URLError:
			print 'url Error'
threads = []
t1 = threading.Thread(target=test1,args=('one',))
threads.append(t1)
t2 = threading.Thread(target=test1,args=('two',))
threads.append(t2)
t3 = threading.Thread(target=test1,args=('three',))
threads.append(t3)
t4 = threading.Thread(target=test1,args=('one',))
threads.append(t4)
t5 = threading.Thread(target=test1,args=('two',))
threads.append(t5)
t6 = threading.Thread(target=test1,args=('three',))
threads.append(t6)
t7 = threading.Thread(target=test1,args=('one',))
threads.append(t7)
t8 = threading.Thread(target=test1,args=('two',))
threads.append(t8)
t9 = threading.Thread(target=test1,args=('three',))
threads.append(t9)
t10 = threading.Thread(target=test1,args=('one',))
threads.append(t10)
t11 = threading.Thread(target=test1,args=('two',))
threads.append(t11)
t12 = threading.Thread(target=test1,args=('three',))
threads.append(t12)
t13 = threading.Thread(target=test1,args=('three',))
threads.append(t13)
t14 = threading.Thread(target=test1,args=('one',))
threads.append(t14)
t15 = threading.Thread(target=test1,args=('two',))
threads.append(t15)
t16 = threading.Thread(target=test1,args=('three',))
threads.append(t16)
t17 = threading.Thread(target=test1,args=('one',))
threads.append(t17)
t18 = threading.Thread(target=test1,args=('two',))
threads.append(t18)
t19 = threading.Thread(target=test1,args=('three',))
threads.append(t19)
t20 = threading.Thread(target=test1,args=('one',))
threads.append(t20)
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print "all over %s" %ctime()
