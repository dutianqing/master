#!/usr/bin/env python
#coding=utf-8
import requests
import time
from multiprocessing.dummy import Pool as ThreadPool

def getsource(url):
    html = requests.get(url)

urls = []

for i in range(1, 21):
    newpage = "http://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=" + str(i)
    urls.append(newpage)

time1 = time.time()

for i in urls:
    print i
    getsource(i)

time2 = time.time()

print u'单线程耗时：' + str(time2 - time1)

pool = ThreadPool(2)

time3 = time.time()

results = pool.map(getsource, urls)

pool.close()

pool.join()

time4 = time.time()

print u'并行耗时：' + str(time4 - time3)


