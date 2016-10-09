

num = int(raw_input())
nums = map(int,raw_input().split())

Total = 0

for a in nums:
    for i in range(0,num):
        Total = (Total + a * nums[i])




print (Total)

