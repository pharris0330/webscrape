#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 08:19:04 2019

@author: michelleharris
"""

import bs4 as bs
import urllib.request
import pandas as pd
import numpy as np

#link to the Climate Data website to obtain temperature data
source = urllib.request.urlopen('https://www.usclimatedata.com/climate/kingsville/texas/united-states/ustx0697/2016/11').read()
soup = bs.BeautifulSoup(source,'lxml')

#select class in HTML
glo = soup.select("td[class^=align_right]")

#strip temperature text from the HTML class
var0 = glo[1].text.strip()
var1 = glo[61].text.strip()
var2 = glo[65].text.strip()
var3 = glo[66].text.strip()
var4 = glo[70].text.strip()
var5 = glo[71].text.strip()
var6 = glo[75].text.strip()
var7 = glo[76].text.strip()
var8 = glo[80].text.strip()
var9 = glo[81].text.strip()
var10 = glo[85].text.strip()
var11 = glo[86].text.strip()
var12 = glo[90].text.strip()
var13 = glo[91].text.strip()
var14 = glo[95].text.strip()
var15 = glo[96].text.strip()
var16 = glo[100].text.strip()
var17 = glo[101].text.strip()
var18 = glo[105].text.strip()
var19 = glo[106].text.strip()
var20 = glo[110].text.strip()
var21 = glo[111].text.strip()
var22 = glo[115].text.strip()
var23 = glo[116].text.strip()
var24 = glo[120].text.strip()
var25 = glo[121].text.strip()
var26 = glo[125].text.strip()
var27 = glo[126].text.strip()
var28 = glo[130].text.strip()
var29 = glo[131].text.strip()
var30 = glo[135].text.strip()
var31 = glo[136].text.strip()
var32 = glo[140].text.strip()
var33 = glo[141].text.strip()
var34 = glo[145].text.strip()
var35 = glo[146].text.strip()
var36 = glo[150].text.strip()
var37 = glo[151].text.strip()
var38 = glo[155].text.strip()
var39 = glo[156].text.strip()
var40 = glo[160].text.strip()
var41 = glo[161].text.strip()
var42 = glo[165].text.strip()
var43 = glo[166].text.strip()
var44 = glo[170].text.strip()
var45 = glo[171].text.strip()
var46 = glo[175].text.strip()
var47 = glo[176].text.strip()
var48 = glo[180].text.strip()
var49 = glo[181].text.strip()
var50 = glo[185].text.strip()
var51 = glo[186].text.strip()
var52 = glo[190].text.strip()
var53 = glo[191].text.strip()
var54 = glo[195].text.strip()
var55 = glo[196].text.strip()
var56 = glo[200].text.strip()
var57 = glo[201].text.strip()
var58 = glo[205].text.strip()
var59 = glo[206].text.strip()
#var60 = glo[210].text.strip()
#var61 = glo[211].text.strip()


#create list to organize the temperature data
my_list = []
my_list.extend([var0,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,
var19,
var20,
var21,
var22,
var23,
var24,
var25,
var26,
var27,
var28,
var29,
var30,
var31,
var32,
var33,
var34,
var35,
var36,
var37,
var38,
var39,
var40,
var41,
var42,
var43,
var44,
var45,
var46,
var47,
var48,
var49,
var50,
var51,
var52,
var53,
var54,
var55,
var56,
var57,
var58,
var59])
#var60,
#var61])


