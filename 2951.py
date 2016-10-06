from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():

    num_keys = int(input())
    fin_num = num_keys


    keys = []

    for i in range(0,num_keys):
        keys.append(input())
        for l in keys:
            if similar(keys[i],l) > 0.7 and l != keys[i]:
                fin_num = fin_num - 1
    
    print (fin_num)
    
if __name__ == '__main__':
    main()