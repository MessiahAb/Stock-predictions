#!/usr/bin/py
from __future__ import division
from math import sqrt
from operator import add
from heapq import heappush, heappop
import numpy as np
import pandas as pd 
def printTransactions(m, k, d, name, owned, prices):
    def info(price):
        df_data=pd.DataFrame(price)
        short=df_data.ewm(span=3, adjust=False).mean()
        long=df_data.ewm(span=5, adjust=False).mean()
        # sa_long=sum(price[0:4])/4
        # Ema_long=sa_long*2/6+price[-1]*(1-2/6)
        # sa_short=sum(price[2:4])/2
        # # print(price[2:4])
        # Ema_short=sa_short*1/3+price[-1]*(2/3)
        # print(Ema_short-Ema_long)
        # print(short[0][4])
        # print(long[0][4])
        return short[0][4]-long[0][4]
    # infos = map(info, prices)
    res = []
    
    drop = []
    
    for i in range(k):
        cur_info = info(prices[i])
    

        if cur_info > 0 and owned[i] > 0:
            res.append((name[i], 'SELL', str(owned[i])))
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
