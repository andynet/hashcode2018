import numpy as np


class Vstup:
    def __init__(self, R,C,F,N,B,T,rides):
        self.R = R
        self.C = C
        self.F = F
        self.N = N
        self.B = B
        self.T = T
        self.rides = rides


def parse():
    R,C,F,N,B,T = map(int, input().split())

    rides = []
    for i in range(N):
        a,b,x,y,s,t = map(int, input().split())
        rides.append((a,b,x,y,s,t))

    vstup = Vstup(R,C,F,N,B,T,rides)
#    print(vstup.R)
    return vstup


def converter(insert, data):
    cars_indexy = dict()
    cars = dict()
    for i in range(1, insert.F + 1):
        cars[i] = []
        cars_indexy[i] = []

    for i in range(len(data)):
        if data[i] ==0:
            continue
        cars[data[i]].append(insert.rides[i])
        cars_indexy[data[i]].append(i)
    
    return cars, cars_indexy

def vystupConverted(data):
    f = open('out.txt', 'w')
    for i in range(len(data.keys())):
        f.write("%d" % len(data[i + 1]))
        for a in data[i + 1]:
            print(a)
            f.write(" %d" % a)
        f.write("\n")
    f.close()

