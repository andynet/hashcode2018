import numpy as np
from sys import stdin
import operator

def rate(insert, solution):
    # [.... ]
    # indexy
    total = 0
    for car in solution.keys():
        score = carScore(solution[car], insert)
        if score == -1:
            return 0
        total += score
    return total




#chybaju bonusi
def carScore(car, insert):
    score = 0
    car.sort(key=operator.itemgetter(4))
    if not checkTimeSorted(car):
        return -1
    for i in range(len(car)):
        score += distance(car[i])
    return score

def checkTimeSorted(car):
    for i in range(len(car)-1):
        #if len(car) > 1:
            #print(car)
            #print("hahahasdhahsdhasdhahsdhahsd")
        if car[i][5] > car[i+1][4]:
            #print("zly cas")
            return False
                
        if ride1to2Distaces(car[i], car[i+1]) > (car[i+1][4] - car[i][5]):
            #print("nesedi vzialenost")
            return False
    return True


def distance(ride):
    return abs(ride[2] - ride[0]) + abs(ride[3] - ride[1])

def ride1to2Distaces(ride1, ride2):
    return abs(ride1[2] - ride2[0]) + abs(ride1[3] - ride2[1])

if __name__ == "__main__":
    main()
