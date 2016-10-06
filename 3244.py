

def main():

    Slices = []

    for i in range(0,8):
        Slice = int(raw_input())
        Slices.append(Slice)

    Slices = Slices + Slices


    HigherNumber = 0
    Total = 0
    z = 0

    for x in range(0,8):

        for y in range(0,4):

            Total = Slices[x + y] + Total

        if Total > HigherNumber:
            HigherNumber = Total
        
        Total = 0
    print (HigherNumber)



if __name__ == '__main__':
    main()