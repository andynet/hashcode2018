import numpy as np
from sys import stdin


def main():
    first = True
    a = np.array([])
    for line in stdin:
        line = np.fromstring(line, dtype=int, sep=' ')
        if first:
            a = np.append(a,line)
            first = False
        else:
            a = np.vstack([a, line])
        #print(line.size)
        #print(line)
    print(a)
    


if __name__ == "__main__":
    main()
