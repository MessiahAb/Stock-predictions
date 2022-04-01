#!/usr/bin/py
from __future__ import division
from math import sqrt
from operator import add
from heapq import heappush, heappop
def printTransactions(m, k, d, name, owned, prices):
    def info(price):
        weights=[0.2,0.4,0.6,0.8]
        avg=0
        for i in range(0,len(price)-1):
            avg+=(price[i+1]-price[i])/price[i]*weights[i]

        
        return avg/5
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
