#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:05:30 2019

@author: hp
"""

import pyshark

capture = pyshark.LiveCapture(interface='enp0s3')
capture.sniff(timeout=10)


List = []

for packet in capture.sniff_continuously(packet_count=100):
    d = {
            "tcpsrc":"",
            "tcpdst":"",
            "hdr_len":"",
            "seq":"",
            "window_size":"",
        }
    
    if("TCP" in str(packet.layers)): 
        d["tcpsrc"]=packet.tcp.srcport
        d["tcpdst"]=packet.tcp.dstport
        d["hdr_len"]=packet.tcp.hdr_len
        d["seq"]=packet.tcp.seq
        d["window_size"]=packet.tcp.window_size
        List.append(d);
    
    
with open("ftp.csv", "w") as fp: 
    fp.write("TCP SRC PORT"+","+"TCP DST PORT"+","+"HDR_LEN"+","+"SEQ"+","+"WINDOW_SIZE"+","+"LABEL"+"\n")
    for x in List:
        fp.write(x["tcpsrc"]+","+x["tcpdst"]+,"+x["hdr_len"]+","+x["seq"]+","+x["window_size"]+","+"FTP"+"\n")
        
    
