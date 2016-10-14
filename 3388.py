
Total = raw_input()
inT = int(Total)
LatotS = ""
T = 0
while inT > 0:

    LatotS = ""
    Latot = list(str(inT))
    Latot.sort(key=int)
    LatotS = LatotS.join(Latot)

    inT = inT - int(LatotS)
    T = T + 1

print (T)