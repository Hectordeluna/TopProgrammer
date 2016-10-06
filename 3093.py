

def main():


    word = list(raw_input("").lower())
    sumlet = 1

    for a in word:
        sumlet = sumlet * (ord(a) - 96)
        

    result = sumlet % 26


    if (result < 10):
        print ("0" + str(result))
    else:
        print(result)


if __name__ == '__main__':
    main()