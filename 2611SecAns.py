T = map(int,raw_input().split())
points = []
Goals = T[1]
Total = 0

for i in range(T[0]):
    N = map(int,raw_input().split())

    # Checar si es mayor y asignar que se gano el partido
    if N[0] - N[1] > 0:
        Total = Total + 3
    # Si es empate, checa si se hay Goles si si le resta uno y le suma 3 Puntos al Total
    elif N[0] - N[1] == 0:
        if Goals > 0:
            Goals = Goals - 1
            Total = Total + 3
        else:
            Total = Total + 1
    elif N[1] - N[0] == 1:
        if Goals >= 2:
            if Goals - (N[1] - N[0]) + 2 > N[1]:
                Total = Total + 3
        else:
            Total = Total + 1
        Goals = Goals - (N[1] - N[0])
    # Si todo falla saca la diferencia de los dos goles
    else:
        points.append(N[1] - N[0])
    

points.sort()
points.reverse()


if Goals > 0:
    for i in range(len(points)):
        if points[i] - Goals > 0:
            Goals = points[i] - Goals
            Total = Total + 3
print(Total)