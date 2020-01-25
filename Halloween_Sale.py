#Link: https://www.hackerrank.com/challenges/halloween-sale/problem?h_r=profile


import math
import os
import random
import re
import sys

def costOfGame(a, p, d, m):
    
    if p == 0:
        return a
    elif  p-d < m :
        return m
    else:
        return p-d
    
    
def howManyGames(p, d, m, s): 
    
    games = 0
    
    pp = 0
    
    while 1:
           
        if pp == 0:
            pp = costOfGame(p, pp, d, m)
            
            if pp > s:
                break
            else: 
                s = s - pp
                games+=1
        else:
            pp = costOfGame(-1, pp, d, m)
            if pp > s:
                break
            else: 
                s = s - pp
                games+=1
        
    return games
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
