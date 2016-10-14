import sys


nums = int(sys.stdin.readline())
keys = []
match = 0

for i in range(0,nums):
    keys.append(sys.stdin.readline())

    curKey = keys[i]
    sortedKey = sorted(list(curKey))

    if len(keys) > 1:
        for x in range(0,len(keys)):
            if sortedKey == sorted(list(keys[x])) and curKey != keys[x]:
                
                match = match + 1

sys.stdout.write(nums - match)