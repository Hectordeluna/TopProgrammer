import sys
import math

n = int(sys.stdin.readline())

for i in range(n):

    num = map(int, sys.stdin.readline().split())

    result = math.factorial(num[0] + num[1] - 1) / ((math.factorial(num[0]) * math.factorial(num[1] - 1)))
    print (result % 1000000007)