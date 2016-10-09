

nums = map(int,raw_input().split())
Jugados = nums[1]
Players = float(nums[0])


if Jugados < Players / 2:
    print (int(Players * Jugados))
else:
    print ("-1")