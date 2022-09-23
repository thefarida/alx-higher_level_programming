#!/usr/bin/python3
import sys

if __name__ == "__main__":
    ag = sys.argv
    l_ag = len(sys.argv)
    sum = 0

if l_ag > 1:
    for i in range(1, l_ag):
        sum += int(ag[i])

    print(sum)
