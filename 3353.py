

def main():
    
    ItemsAndGuards = map(int,raw_input().split())
    
    Items = ItemsAndGuards[0]
    Guards = ItemsAndGuards[1]

    Total = 0

    ItemsPrices = sorted(map(int,raw_input().split()))

    if Guards > len(ItemsPrices):
        Guards = len(ItemsPrices)
    
    for i in range(0,Guards):
        if ItemsPrices[i] < 0:
            Total = Total + abs(ItemsPrices[i])



    print (Total)



if __name__ == '__main__':
    main()