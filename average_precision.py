'''
Calcaultes average precision given a list, where 1 = relevant, 0 = not relevant
E.g.[1,0,0,0,0,0,0,...1] tends to 0.5 AP as does [0,1,0,1,0,1,0,...1]
'''
import numpy as np
from typing import List


def AP(l: List[int]) -> float:
     precision = []
     c = 0.
     for i, m in enumerate(l):
         c += m
         if m==1:
             precision.append(c / (i + 1))
         if int(c) == sum(l):
             break
     return np.mean(precision)


if __name__ == '__main__':

    print(AP([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]))
    print(AP([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1]))
