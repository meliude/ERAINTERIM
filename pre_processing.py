#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:44:54 2019

@author: meliude
"""

import pygrib
import pandas as pd

years = ['1998.grib', '1999.grib', '2000.grib', '2001.grib', '2002.grib', '2003.grib', '2004.grib', '2005.grib', '2006.grib', '2007.grib', '2008.grib']
data = []
dp = [] #dewpoint
tp = [] #totalprecipitation

for i in range(0,11):
    data.append(pygrib.open(years[i]))
    dp.append(data[i].select(name = '2 metre dewpoint temperature'))
    tp.append(data[i].select(name = 'Total precipitation'))

#leapyears: 2000, 2004 and 2008
##jan(0,31),feb(31,60),mar(60,91),apr(91,121),may(121,152),jun(152,182),jul(182,213),aug(213,244)
##sep(244,274),oct(274,305),nov(305,335),dec(335,366)

#for dewpoint temperature
jan_dp,feb_dp,mar_dp,apr_dp,may_dp,jun_dp,jul_dp,aug_dp,sep_dp,oct_dp,nov_dp,dec_dp=[], [], [], [], [], [], [], [], [], [], [], []

#convert Kelvin to Celsius
def convert(x):
    return x-273.15

for i in range(0,11):
    if i==2:
        for j in range(0,31):
            jan_dp.append(convert(dp[i][j].values))
        for j in range(31,60):
            feb_dp.append(convert(dp[i][j].values))
        for j in range(60,91):
            mar_dp.append(convert(dp[i][j].values))
        for j in range(91,121):
            apr_dp.append(convert(dp[i][j].values))
        for j in range(121,152):
            may_dp.append(convert(dp[i][j].values))
        for j in range(152,182):
            jun_dp.append(convert(dp[i][j].values))
        for j in range(182,213):
            jul_dp.append(convert(dp[i][j].values))
        for j in range(213,244):
            aug_dp.append(convert(dp[i][j].values))
        for j in range(244,274):
            sep_dp.append(convert(dp[i][j].values))
        for j in range(274,305):
            oct_dp.append(convert(dp[i][j].values))
        for j in range(305,335):
            nov_dp.append(convert(dp[i][j].values))
        for j in range(335,366):
            dec_dp.append(convert(dp[i][j].values))
    elif i==6:
        for j in range(0,31):
            jan_dp.append(convert(dp[i][j].values))
        for j in range(31,60):
            feb_dp.append(convert(dp[i][j].values))
        for j in range(60,91):
            mar_dp.append(convert(dp[i][j].values))
        for j in range(91,121):
            apr_dp.append(convert(dp[i][j].values))
        for j in range(121,152):
            may_dp.append(convert(dp[i][j].values))
        for j in range(152,182):
            jun_dp.append(convert(dp[i][j].values))
        for j in range(182,213):
            jul_dp.append(convert(dp[i][j].values))
        for j in range(213,244):
            aug_dp.append(convert(dp[i][j].values))
        for j in range(244,274):
            sep_dp.append(convert(dp[i][j].values))
        for j in range(274,305):
            oct_dp.append(convert(dp[i][j].values))
        for j in range(305,335):
            nov_dp.append(convert(dp[i][j].values))
        for j in range(335,366):
            dec_dp.append(convert(dp[i][j].values))
    elif i==10:
        for j in range(0,31):
            jan_dp.append(convert(dp[i][j].values))
        for j in range(31,60):
            feb_dp.append(convert(dp[i][j].values))
        for j in range(60,91):
            mar_dp.append(convert(dp[i][j].values))
        for j in range(91,121):
            apr_dp.append(convert(dp[i][j].values))
        for j in range(121,152):
            may_dp.append(convert(dp[i][j].values))
        for j in range(152,182):
            jun_dp.append(convert(dp[i][j].values))
        for j in range(182,213):
            jul_dp.append(convert(dp[i][j].values))
        for j in range(213,244):
            aug_dp.append(convert(dp[i][j].values))
        for j in range(244,274):
            sep_dp.append(convert(dp[i][j].values))
        for j in range(274,305):
            oct_dp.append(convert(dp[i][j].values))
        for j in range(305,335):
            nov_dp.append(convert(dp[i][j].values))
        for j in range(335,366):
            dec_dp.append(convert(dp[i][j].values))
    else:
        for j in range(0,31):
            jan_dp.append(convert(dp[i][j].values))
        for j in range(31,59):
            feb_dp.append(convert(dp[i][j].values))
        for j in range(59,90):
            mar_dp.append(convert(dp[i][j].values))
        for j in range(90,120):
            apr_dp.append(convert(dp[i][j].values))
        for j in range(120,151):
            may_dp.append(convert(dp[i][j].values))
        for j in range(151,181):
            jun_dp.append(convert(dp[i][j].values))
        for j in range(181,212):
            jul_dp.append(convert(dp[i][j].values))
        for j in range(212,243):
            aug_dp.append(convert(dp[i][j].values))
        for j in range(243,273):
            sep_dp.append(convert(dp[i][j].values))
        for j in range(273,304):
            oct_dp.append(convert(dp[i][j].values))
        for j in range(304,334):
            nov_dp.append(convert(dp[i][j].values))
        for j in range(334,365):
            dec_dp.append(convert(dp[i][j].values))

#jan,mar,may,jul,aug,oct,dec

def totalsum(x,a=1,b=2):
    return sum(x[a],x[b])

##0,30,31,61,62,92,93,123,124,154,155,185,186,216,217,247,248,278,279,309,310,340
lb=[0,31,62,93,124,155,186,217,248,279,310]
up=[30,61,92,123,154,185,216,247,278,309,340]

jan_tdp, mar_tdp, may_tdp, jul_tdp, aug_tdp,oct_tdp,dec_tdp=[], [], [], [], [], [], []
for i,j in zip(lb,up):
    jan_tdp.append(totalsum(jan_dp,a=i,b=j))
    mar_tdp.append(totalsum(mar_dp,a=i,b=j))
    may_tdp.append(totalsum(may_dp,a=i,b=j))
    jul_tdp.append(totalsum(jul_dp,a=i,b=j))
    aug_tdp.append(totalsum(aug_dp,a=i,b=j))
    oct_tdp.append(totalsum(oct_dp,a=i,b=j))
    dec_tdp.append(totalsum(dec_dp,a=i,b=j))

jan_tdp, mar_tdp, may_tdp, jul_tdp, aug_tdp,oct_tdp,dec_tdp=sum(jan_tdp)/11, sum(mar_tdp)/11, sum(may_tdp)/11, sum(jul_tdp)/11, sum(aug_tdp)/11, sum(oct_tdp)/11, sum(dec_tdp)/11

pd.DataFrame(jan_tdp).to_csv('grid_jan.csv')
pd.DataFrame(mar_tdp).to_csv('grid_mar.csv')
pd.DataFrame(may_tdp).to_csv('grid_may.csv')
pd.DataFrame(jul_tdp).to_csv('grid_jul.csv')
pd.DataFrame(aug_tdp).to_csv('grid_aug.csv')
pd.DataFrame(oct_tdp).to_csv('grid_oct.csv')
pd.DataFrame(dec_tdp).to_csv('grid_dec.csv')

#apr,jun,sep,nov

##0,29,30,59,60,89,90,119,120,149,150,179,180,209,210,239,240,269,270,299,300,329
lb=[0,30,60,90,120,150,180,210,240,270,300]
ub=[29,59,89,119,149,179,209,239,269,299,329]
apr_tdp, jun_tdp, sep_tdp, nov_tdp=[], [], [], []
for i,j in zip(lb,ub):
    apr_tdp.append(totalsum(apr_dp,a=i,b=j))
    jun_tdp.append(totalsum(jun_dp,a=i,b=j))
    sep_tdp.append(totalsum(sep_dp,a=i,b=j))
    nov_tdp.append(totalsum(nov_dp,a=i,b=j))
    
apr_tdp, jun_tdp, sep_tdp, nov_tdp=sum(apr_tdp)/11, sum(jun_tdp)/11, sum(sep_tdp)/11, sum(nov_tdp)/11

pd.DataFrame(apr_tdp).to_csv('grid_apr.csv')
pd.DataFrame(jun_tdp).to_csv('grid_jun.csv')
pd.DataFrame(sep_tdp).to_csv('grid_sep.csv')
pd.DataFrame(nov_tdp).to_csv('grid_nov.csv')

#feb
##0,27,28,55,56,84,85,112,113,140,141,168,169,197,198,225,226,253,254,281,282,310
lb=[0,28,56,85,113,141,169,198,226,254,282]
ub=[27,55,84,112,140,168,197,225,253,281,310]
feb_tdp=[]
for i,j in zip(lb,ub):
    feb_tdp.append(totalsum(feb_dp,a=i,b=j))

feb_tdp=sum(feb_tdp)/11
pd.DataFrame(feb_tdp).to_csv('grid_feb.csv')

############################################################################################
#for total prepicipation

jan_tp,feb_tp,mar_tp,apr_tp,may_tp,jun_tp,jul_tp,aug_tp,sep_tp,oct_tp,nov_tp,dec_tp=[], [], [], [], [], [], [], [], [], [], [], []

for i in range(0,11):
    if i==2:
        for j in range(0,31):
            jan_tp.append(tp[i][j].values)
        for j in range(31,60):
            feb_tp.append(tp[i][j].values)
        for j in range(60,91):
            mar_tp.append(tp[i][j].values)
        for j in range(91,121):
            apr_tp.append(tp[i][j].values)
        for j in range(121,152):
            may_tp.append(tp[i][j].values)
        for j in range(152,182):
            jun_tp.append(tp[i][j].values)
        for j in range(182,213):
            jul_tp.append(tp[i][j].values)
        for j in range(213,244):
            aug_tp.append(tp[i][j].values)
        for j in range(244,274):
            sep_tp.append(tp[i][j].values)
        for j in range(274,305):
            oct_tp.append(tp[i][j].values)
        for j in range(305,335):
            nov_tp.append(tp[i][j].values)
        for j in range(335,366):
            dec_tp.append(tp[i][j].values)
    elif i==6:
        for j in range(0,31):
            jan_tp.append(tp[i][j].values)
        for j in range(31,60):
            feb_tp.append(tp[i][j].values)
        for j in range(60,91):
            mar_tp.append(tp[i][j].values)
        for j in range(91,121):
            apr_tp.append(tp[i][j].values)
        for j in range(121,152):
            may_tp.append(tp[i][j].values)
        for j in range(152,182):
            jun_tp.append(tp[i][j].values)
        for j in range(182,213):
            jul_tp.append(tp[i][j].values)
        for j in range(213,244):
            aug_tp.append(tp[i][j].values)
        for j in range(244,274):
            sep_tp.append(tp[i][j].values)
        for j in range(274,305):
            oct_tp.append(tp[i][j].values)
        for j in range(305,335):
            nov_tp.append(tp[i][j].values)
        for j in range(335,366):
            dec_tp.append(tp[i][j].values)
    elif i==10:
        for j in range(0,31):
            jan_tp.append(tp[i][j].values)
        for j in range(31,60):
            feb_tp.append(tp[i][j].values)
        for j in range(60,91):
            mar_tp.append(tp[i][j].values)
        for j in range(91,121):
            apr_tp.append(tp[i][j].values)
        for j in range(121,152):
            may_tp.append(tp[i][j].values)
        for j in range(152,182):
            jun_tp.append(tp[i][j].values)
        for j in range(182,213):
            jul_tp.append(tp[i][j].values)
        for j in range(213,244):
            aug_tp.append(tp[i][j].values)
        for j in range(244,274):
            sep_tp.append(tp[i][j].values)
        for j in range(274,305):
            oct_tp.append(tp[i][j].values)
        for j in range(305,335):
            nov_tp.append(tp[i][j].values)
        for j in range(335,366):
            dec_tp.append(tp[i][j].values)
    else:
        for j in range(0,31):
            jan_tp.append(tp[i][j].values)
        for j in range(31,59):
            feb_tp.append(tp[i][j].values)
        for j in range(59,90):
            mar_tp.append(tp[i][j].values)
        for j in range(90,120):
            apr_tp.append(tp[i][j].values)
        for j in range(120,151):
            may_tp.append(tp[i][j].values)
        for j in range(151,181):
            jun_tp.append(tp[i][j].values)
        for j in range(181,212):
            jul_tp.append(tp[i][j].values)
        for j in range(212,243):
            aug_tp.append(tp[i][j].values)
        for j in range(243,273):
            sep_tp.append(tp[i][j].values)
        for j in range(273,304):
            oct_tp.append(tp[i][j].values)
        for j in range(304,334):
            nov_tp.append(tp[i][j].values)
        for j in range(334,365):
            dec_tp.append(tp[i][j].values)

#jan,mar,may,jul,aug,oct,dec

jan_ttp, mar_ttp, may_ttp, jul_ttp, aug_ttp,oct_ttp,dec_ttp=[], [], [], [], [], [], []

for i,j in zip(lb,up):
    jan_ttp.append(totalsum(jan_tp,a=i,b=j))
    mar_ttp.append(totalsum(mar_tp,a=i,b=j))
    may_ttp.append(totalsum(may_tp,a=i,b=j))
    jul_ttp.append(totalsum(jul_tp,a=i,b=j))
    aug_ttp.append(totalsum(aug_tp,a=i,b=j))
    oct_ttp.append(totalsum(oct_tp,a=i,b=j))
    dec_ttp.append(totalsum(dec_tp,a=i,b=j))

jan_ttp, mar_ttp, may_ttp, jul_ttp, aug_ttp,oct_ttp,dec_ttp=sum(jan_ttp)/11, sum(mar_ttp)/11, sum(may_ttp)/11, sum(jul_ttp)/11, sum(aug_ttp)/11, sum(oct_ttp)/11, sum(dec_ttp)/11

pd.DataFrame(jan_ttp).to_csv('grid_jan_p.csv')
pd.DataFrame(mar_ttp).to_csv('grid_mar_p.csv')
pd.DataFrame(may_ttp).to_csv('grid_may_p.csv')
pd.DataFrame(jul_ttp).to_csv('grid_jul_p.csv')
pd.DataFrame(aug_ttp).to_csv('grid_aug_p.csv')
pd.DataFrame(oct_ttp).to_csv('grid_oct_p.csv')
pd.DataFrame(dec_ttp).to_csv('grid_dec_p.csv')

#apr,jun,sep,nov

apr_ttp, jun_ttp, sep_ttp, nov_ttp=[], [], [], []
for i,j in zip(lb,ub):
    apr_ttp.append(totalsum(apr_tp,a=i,b=j))
    jun_ttp.append(totalsum(jun_tp,a=i,b=j))
    sep_ttp.append(totalsum(sep_tp,a=i,b=j))
    nov_ttp.append(totalsum(nov_tp,a=i,b=j))
    
apr_ttp, jun_ttp, sep_ttp, nov_ttp=sum(apr_ttp)/11, sum(jun_ttp)/11, sum(sep_ttp)/11, sum(nov_ttp)/11

pd.DataFrame(apr_ttp).to_csv('grid_apr_p.csv')
pd.DataFrame(jun_ttp).to_csv('grid_jun_p.csv')
pd.DataFrame(sep_ttp).to_csv('grid_sep_p.csv')
pd.DataFrame(nov_ttp).to_csv('grid_nov_p.csv')

#feb

feb_ttp=[]
for i,j in zip(lb,ub):
    feb_ttp.append(totalsum(feb_tp,a=i,b=j))

feb_ttp=sum(feb_ttp)/11
pd.DataFrame(feb_ttp).to_csv('grid_feb_p.csv')