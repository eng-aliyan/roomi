
cost = int(input(''))

off = 0
if cost < 5000:
    off = 10
elif 5000 <= cost <= 10000:
    off = 5
elif cost > 10000:
    off = 3

cost = int( cost - (cost*(off/100)) )
print(cost)
