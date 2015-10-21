#!/usr/bin/env python
#conding=utf-8
import re
import requests

f = open('text.txt', 'r')
html = f.read()
f.close()

pic_url = re.findall('img src="(.*?) alt=""', html, re.S)
i = 0
for each in pic_url:
    print "now download:" + each
    pic = requests.get(each)
    fp = open('/root/PycharmProjects/temp/pic/' + str(i) + '.png', 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1