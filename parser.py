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


def main():
    R,C,F,N,B,T = map(int, input().split())

    rides = []
    for i in range(N):
        a,b,x,y,s,t = map(int, input().split())
        rides.append((a,b,x,y,s,t))

    vstup = Vstup(R,C,F,N,B,T,rides)
#    print(vstup.R)
    return vstup


if __name__ == "__main__":
    main()
