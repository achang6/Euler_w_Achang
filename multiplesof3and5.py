# find the sum of all the multiples of 3 or 5 below 1000
# assuming 1000 is not included

# first find multiples
thousandintegers = range(0,1000)
usefulintegers = []

# check
# print(thousandintegers)

# process integers
for i in thousandintegers:
    # check if divisible by 3 or 5
    if i % 3 == 0 or i % 5 == 0:
        usefulintegers.append(thousandintegers[i])

# add up all of the multiples
monkeysum = sum(usefulintegers)
print(monkeysum)
