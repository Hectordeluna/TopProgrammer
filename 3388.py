
Total = raw_input()
inT = int(Total)
T = 0
while inT > 0:

    LatotS = ""
    Latot = list(Total)
    print (Latot)
    Latot.sort(key=int)
    print (Latot)
    LatotS = LatotS.join(Latot)
    print (LatotS)

    inT = inT - int(LatotS)
    T = T + 1

print (T)