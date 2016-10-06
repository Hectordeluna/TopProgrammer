

def main():

    num = int(raw_input())

    
    for i in range(0,num):

        word = raw_input()

        rvs = word[::-1]

        if rvs == word:
            print ("YES")
        else:
            print ("NO")


if __name__ == '__main__':
    main()