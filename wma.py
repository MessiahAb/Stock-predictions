#!/usr/bin/py
from __future__ import division
from math import sqrt
from operator import add
from heapq import heappush, heappop
import numpy as np
import pandas as pd 
def printTransactions(m, k, d, name, owned, prices):
    #In thist function the difference between short time and long term average is computed  
    def info(price):
        df_data=pd.DataFrame(price)
        short=df_data.ewm(span=3, adjust=False).mean()
        long=df_data.ewm(span=5, adjust=False).mean()
        return short[0][4]-long[0][4]
    res = []

    drop = []
    
    for i in range(k):
        cur_info = info(prices[i])
        #If the difference is greater than zero it will be sold 
        if cur_info > 0 and owned[i] > 0:
            res.append((name[i], 'SELL', str(owned[i])))
        #If the difference is less  than zero it will be appended to a heap and will be bought by prioritizing 
        elif cur_info < 0:
            heappush(drop, (cur_info, i, name[i]))
    
    while m > 0.0 and drop:
        rate, idx, n = heappop(drop)
        amount = int(m / prices[idx][-1])
        if amount  > 0:
            res.append((n, 'BUY', str(amount)))
            m -= amount * prices[idx][-1]
    
    print len(res)
    for r in res:
        print ' '.join(r)
        
if __name__ == '__main__':
    m, k, d = [float(i) for i in raw_input().strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = raw_input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)
