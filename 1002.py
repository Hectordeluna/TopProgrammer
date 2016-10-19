T = input()


for i in range(T):
    HigherCube = 0
    N = input()
    Land = []  
    for x in range(N):
        Land.append(list(raw_input()))
        for y in range(len(Land[x])):
            if Land[x][y] == "#":
                Land[x][y] = 0
            elif x == 0 or y == 0:
                Land[x][y] = 1
            elif x > 0 and y > 0:
                CL = Land[x - 1][y]
                Tp = Land[x - 1][y - 1]
                if CL > Tp:
                    CL = Tp
                Tp = Land[x][y - 1]
                if CL > Tp:
                    CL = Tp
                Land[x][y] = CL + 1
                if Land[x][y] > HigherCube:
                    HigherCube = Land[x][y]
    print (HigherCube)

    