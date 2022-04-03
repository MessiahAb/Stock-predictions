#!/usr/bin/py
from __future__ import division
from math import sqrt
from operator import add
from heapq import heappush, heappop

def printTransactions(m, k, d, name, owned, prices):
    #In thist function the percentage of differnce between last three prices is computed 
    def info(price):
        return (price[-1] - price[-2]) / price[-2], (price[-3] - price[-2]) / price[-3]
    infos = map(info, prices)
    res = []
    
    drop = []
    
    for i in range(k):
        cur_info1,cur_info2 = info(prices[i])
        if cur_info1 > 0 and cur_info2>0 and owned[i] > 0:
            res.append((name[i], 'SELL', str(owned[i])))
        elif cur_info1 < 0:
            heappush(drop, (cur_info1, i, name[i]))
    
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
