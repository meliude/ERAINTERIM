import pygrib
import pandas as pd

from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "date": "1998-01-01/to/2008-12-31",
    "expver": "1",
    "grid": "0.1/0.1",
    "area": "-3/-41.5/-8/-37.5",
    "levtype": "sfc",
    "param": "168.128/228.128",
    "step": "12",
    "stream": "oper",
    "time": "00:00:00",
    "type": "fc",
    "target": "output",
})

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
    if i == (2,6,10):
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
    if i != (2,6,10):
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
pd.DataFrame(may_tdp).to_csv('grid_may.csv')
pd.DataFrame(jul_tdp).to_csv('grid_jul.csv')
pd.DataFrame(aug_tdp).to_csv('grid_aug.csv')
pd.DataFrame(oct_tdp).to_csv('grid_oct.csv')
pd.DataFrame(dec_tdp).to_csv('grid_dec.csv')

