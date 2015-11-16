# find smallest positive number 
# that is evenly divisible by all of the numbers from 1 to 20

'''monkey = 1
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

print monkey'''

# result: 232792560
# 285097th person to have solved this problem
# it's funny because while I was waiting for the result
# I went ahead and found the answer by hand
# through prime factorization
# took me 10 minutes to find what
# my program took 2 and a half hours to find. 



# round 2
def choppablebyfirstxwholenumbers(x, testmonkey):
    # x is the number of axes we will chop
    # a monkey with to see
    # if our super soldier serum works

    # testmonkey is the suspect subject
    # that we put on the chopping block

    # first we ready a stand
    # to hold all the axes/divisors
    # that could not cut the monkey
    axesrepelled = 0

    # next we test each axe
    # one at a time
    for axe in range(1,x+1):
        if testmonkey % axe == 0:
            axesrepelled += 1   # if an axe fails we add it to the wall of approval

        if axesrepelled != axe: # if an axe succeeds we eliminate the monkey
            return False 
        elif axesrepelled == x: # if all axes fail, we run further tests
            return True



# done? we haven't even started!
done = False
# how many axes shall we try?
axes = 20
# the first monkey shall be...
monkey = 1
# so begins the cycle of science
while not done:
    if choppablebyfirstxwholenumbers(axes, monkey):     # FOR SCIENCE!
        done = True     # we have found our monkey
    else:
        monkey += 1     # move on to next monkey

# publish research paper
print monkey



# science budget:
# net lines of code: 18

