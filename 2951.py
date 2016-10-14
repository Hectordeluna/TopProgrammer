import sys

nums = int(sys.stdin.readline())
uniquekeys = set()

for i in range(nums):

    keys=[l for l in sys.stdin.readline().strip()]
    keys.sort()
    keys="".join(keys)
    uniquekeys.add(keys)


sys.stdout.write(str(len(uniquekeys)))
