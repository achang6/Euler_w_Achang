# find sum of even fibonacci numbers below 4 million

fibo = [1,2]
backnum = 0
nownum = 0
newnum = 0
evenfibo = []

# find all fibonacci below 4000000
while newnum < 4000000:
    backnum = fibo[len(fibo) - 2]
    nownum = fibo[len(fibo) - 1]
    newnum = backnum + nownum
    if newnum < 4000000:
        fibo.append(newnum)

# separate into even fibonacci
for f in fibo:
    if f % 2 == 0:
        evenfibo.append(f)

# sum
fibosum = sum(evenfibo)
print(fibosum)

# 418592nd person
