
def main():


    test = int(input(""))
    total = 0.0

    for i in range(0,test):
        num = int(input(""))

        for z in range(0,num):
            total = (total + 0.5) * 2

        print (int(total))
        total = 0

if __name__ == '__main__':
    main()


            