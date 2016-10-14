
T = input()

for i in range(T):

    X = map(int,raw_input().split())

    print (abs(X[0] - X[2]) + abs(X[1] - X[3]))