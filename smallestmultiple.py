# find smallest positive number 
# that is evenly divisible by all of the numbers from 1 to 20

monkey = 1
multiplesobtained = 0
divisors = range(1,21)
done = False

while not done:
    for d in divisors:
        if monkey % d == 0:
            multiplesobtained += 1
    print multiplesobtained
    if multiplesobtained == 20:
        done = True
    else:
        monkey += 1
        multiplesobtained = 0
    print monkey

print monkey

# result: 232792560
# 285097th person to have solved this problem
# it's funny because while I was waiting for the result
# I went ahead and found the answer by hand
# through prime factorization
# took me 10 minutes to find what
# my program took 2 and a half hours to find. 
