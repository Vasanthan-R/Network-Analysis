#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 21:30:10 2019

@author: hp
"""
import pyshark
import pickle
import pandas as pd

capture = pyshark.LiveCapture(interface='enp0s3')

# Use the loaded pickled model to make predictions 
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
 

for packet in capture.sniff_continuously():
    # collect all the packet information
    if("TCP" in str(packet.layers)): 
        srcport = packet.tcp.srcport
        dstport = packet.tcp.dstport
        hdr_len = packet.tcp.hdr_len
        seq = packet.tcp.seq
        window_size = packet.tcp.window_size     

    	# construct test data
        p = [srcport, dstport, hdr_len, seq, window_size]

    	# predict
        result = loaded_model.predict([p])
    
        print(result)
     
