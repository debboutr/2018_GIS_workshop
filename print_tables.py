#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 22:42:25 2018

@author: rick
"""
    
import os
import pandas as pd
#os.getcwd()
folder = 'wsamarch2_2009'
all_tables = pd.DataFrame()
for f in os.listdir('./%s' % folder):
    if f.split('.')[-1] == 'csv' and f.split('.')[0] == 'verification':
        print '*************************'
        print f
        tbl = pd.read_csv('{}/{}'.format(folder,f))
        for col in tbl.columns.tolist():
            print col
