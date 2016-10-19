import sys

T = map(int,raw_input().split())
Points = 0
Goals = T[1]
Ties = 0
dif = []

for i in range(T[0]):
    
    N = map(int,raw_input().split())

    if N[0] > N[1]:
        Points = Points + 3
    elif N[0] == N[1]:
        Ties = Ties + 1
    else:
        dif.append(N[0] - N[1])


for i in range(Ties):
    if Goals > 0:
        Goals = Goals - 1
    else:
        Ties = i
        Points = Points + abs(i - Ties + 1)

Points = Points + (Ties * 3)

if Goals <= 0:
    sys.exit()
    print(Points)
    
dif.sort()
dif = map(abs,dif)


for i in range(len(dif)):
    if Goals - dif[i] > 0:
        Goals = Goals - dif[i]
        Points = Points + 3

print(Points)