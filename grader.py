import numpy as np
from sys import stdin


def rate(insert, solution):
    # [.... ]
    # indexy
    total = 0
    for car in solution.keys():
        score = carScore(solution[car])
        if score == 0:
            return 0
        total += score

    return total




#chybaju bonusi
def carScore(car, insert):
    score = 0
    sorted(car, cmp= lambda x,y: x[4] < y[4])
    if not checkTimeSorted(car):
        return 0
    
    for i in range(len(car)):
        score += distance(car[i])

def checkTimeSorted(car):
    for i in range(len(car)-1):
        if car[i][5] > car[i+1][4]:
            return False
                
        if ride1to2Distaces(car[i], car[i+1]) > (car[i][5] - car[i+1][4])
            return False
    return True


def distance(ride):
    return abs(ride[2] - ride[0]) + abs(ride[3] - ride[1])

def ride1to2Distaces(ride1, ride2):
    return abs(ride1[2] - ride2[0]) + abs(ride1[3] - ride2[1])

if __name__ == "__main__":
    main()
