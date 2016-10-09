

tests = int(raw_input())



for i in range(0,tests):
    nums = map(float,raw_input().split())

    Distance = nums [0]
    Vone = nums[1]
    Vtwo = nums[2]
    Vfly = nums [3]


    Time = Distance / (Vone + Vtwo)
    DistanceFly = Vfly * Time
    print (format(DistanceFly,'.2f'))
