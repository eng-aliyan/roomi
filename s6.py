c = 1
d = {}
for i in range(100, 400+1):
    if i%2 == 0:
        if i%3 == 0:
            d[c] = i
            c = c + 1

print(d)
