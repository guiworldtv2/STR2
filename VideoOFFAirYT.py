#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:27:18 2017

@author: hakandemirel
"""

import requests
import subprocess 
import shutil
import re
#import time
import sys
#import os

f = open('temp.txt', 'w')
f.write("#EXTM3U\n") 
f.close()

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben
    
def linksolver( url ):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Connection':'keep-alive',}
        req = requests.get(url, headers=headers)
        test = req.text
        lhs, rhs = test.split("source: \'",1)
        source , newrhs = rhs.split("\',\n",1)
        return source

def trlinksolver( url ):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Connection':'keep-alive',}
        req = requests.get(url, headers=headers)
        test = req.text
        lhs, rhs = test.split("source: \'",1)
        source , newrhs = rhs.split("\',\n",1)
        return source    
    
def ecanlisolver( url ): 
    #url = "https://tviplayer.iol.pt/direto/TVI_REALITY/"
    out = subprocess.getoutput("streamlink --stream-url "+url+" best")
    return out 
def write2file( names_n , channels_n  ):
    for i in range(0,len(names_n)):
        with open("temp.txt", "a") as myfile:
                myfile.write("#EXTINF:0,"+str(names_n[i])+" \n")
                #myfile.write("h"+test19+" \n")
                myfile.write(channels_n[i])
def ecanliget(url):
    #url = "https://tviplayer.iol.pt/direto/TVI_REALITY"
    name=[]
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Connection':'keep-alive',}
    req = requests.get(url, headers=headers)
    test = req.text
    lhs, newrhs = test.split('<ul class="kanallar">',1)
    #<div class="div_ekran_alti">
    lhs, newrhs = newrhs.split('<footer>',1)
    r = re.compile('(?<=<a href=").*?(?=" title)')
    n = re.compile('(?<=title=").*?(?=")')
    liste = r.findall(lhs)
    name = n.findall(lhs)
    number = 0   
    channels =[]
    names = []
    for i in liste:
        #print(str(i))
        progress(ii+number,9+len(name))
        nameget = name[number].encode('ascii', 'ignore').decode('ascii')
        print(nameget)
        names.append(nameget)
        channels.append( ecanlisolver(str(i)))
        number = number +1
    indices = [i for i, elem in enumerate(channels) if 'error:' not in elem]
    names_n =[]
    channels_n =[]
    for i in indices:
        names_n.append(names[i])
        channels_n.append(channels[i])
    return names_n,channels_n

#%% 
jj = 0 
ii = 1         
                              

shutil.move('temp.txt', 'live.m3u8')
#print("Turkish Channels from https://tviplayer.iol.pt/direto/TVI_REALITY")                    
#ecanliget("https://tviplayer.iol.pt/direto/TVI_REALITY")
print("\n\n\n")
print("############################################")
print("\n")
print(" DONE! Your live.m3u8 File is ready to use  ")
print("\n")
print("############################################")
print("\n\n\n")
