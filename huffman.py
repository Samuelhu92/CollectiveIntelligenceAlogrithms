from heapq import heapify,heappush,heappop
from itertools import count

def huffman(seq,frq):
    num=count()
    trees=list(zip(frq,num,seq))
    heapify(trees)
    while len(trees)>1:
        fa,_,a = heappop(trees)
        fb,_,b = heappop(trees)
        n=next(num)
        heappush(trees,(fa+fb,n,[a,b]))
    return trees[0][-1]

