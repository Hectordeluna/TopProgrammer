
T = input()

for i in range(T):
    W = raw_input().split(" ")
    W1 = list(W[0])
    W2 = list(W[1])
    Total = 0
    for x in range(len(W1)):
        if W1[x] != W2[x]:
            Total = Total + 1

    print(Total)