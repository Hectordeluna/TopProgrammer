def part_sum(numbers):
    total = 0
    for i in numbers:
        total += i
        yield total



def main():
    num = input()
    data_list = map(int,raw_input().split())
    new_list = []

    Total = 0

    x = 0
    y = num - 1
    z = 0
    data_list.sort()

    while len(new_list) < num:
        
        iA = data_list[x]
        iB = data_list[y]

        if z % 2 == 0:
            iA, iB = iB, iA

        if len(new_list) < num:
            new_list.append(iB)
            y = y - 1
        if len(new_list) < num:
            new_list[:0] = [iA]
            x = x + 1

        z = z + 1

    new_list.reverse()
    totsum = (sum(new_list))
    parttot = list(part_sum(new_list))
    for i in range(num - 2):
        if i == 0:
            Total += new_list[i] * ((totsum - new_list[len(new_list) - 1]) - parttot[i+1])
        else:
            Total += new_list[i] * (totsum - parttot[i+1]) 

    if(len(str(Total)) > 5):
        stTot = str(Total)
        lstTot = list(stTot)
        size = len(lstTot)
        print(lstTot[size - 5] + lstTot[size - 4] + lstTot[size - 3] + lstTot[size - 2] + lstTot[size - 1])
       
    else:
        print(str(Total).zfill(5))

if __name__ == "__main__":
    main()