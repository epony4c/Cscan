#coding=utf-8
# 收集工具，判断C段地址存活，是不是有web，端口扫描

import os
import socket
import sys
import subprocess
import nmap
import threading

# 获取ip
def makeip():
    try:
        putin = input("请输出IP的前三个段和.例: <192.168.1.> :")
        iplist = open('iplist.txt','w')
        for i in range(1,255):
            iplist.write(putin+(str(i))+"\n")
    except:
        print("生成失败")

# 判断web应用
def webscan():
    a = open('iplist.txt', 'r')
    for g in a.readlines():
        gv = g.strip('\r').strip('\n')
        s = socket.socket()
        try:
            s.connect((gv,80))
            x = open('webopen.txt','w')
            x.write(gv)
            print('WEB开启:' + gv)
        except:
                pass

# 判断连通,同时写到本地ping文件里了
def ipping():
    ip = open('iplist.txt','r')
    for s in ip.readlines():
        s = s.strip('\n')
        ret = subprocess.call("ping -w 5 %s" %s,shell=True,stdout=subprocess.PIPE)
        if ret == 0:
            str = '%s is alive' % s
            str1 = s
            print(str)
            wite = open('ping.txt', 'w')
            wite.write(str1)
        elif ret == 1:
            str = '%s is not alive' %s
            print(str)

# 定义端口扫描(ping)
ports = '1-65535'
arg = '-Pn -T4'
def portsscan():
    a1 = open('ping.txt', 'r')
    for i in a1.readlines():
        nm = nmap.PortScanner()
        nmer = nm.scan(hosts=i, ports=ports, arguments=arg)
        out = open('portslist.txt', 'w', encoding='utf-8')
        st = nmer['scan']
        print(st)
        out.write(str(st))

if __name__ == '__main__':
    makeip()
    jianceweb = input("检测web？确定选'Y'")
    if jianceweb == 'Y':
        webscan()
    else:
        pass

    jianceping = input("检测连通？确定选'Y'")
    if jianceping == 'Y':
        ipping()
    else:
        pass

    duankousaomiao = input("扫描端口？{根据ping的文本}")
    if duankousaomiao == 'Y':
        portsscan()
    else:
        pass