# find difference from sum of squares to square of sum
# of first whole numbers

# first make list of 100 numbers
onehundred = range(1,101)

squaresum = 0

tempsum = 0
sumsquare = 0

diff = 0

# find sum of squares
for n in onehundred:
    squaresum += n**2
    print(squaresum)

# find square of sum
for n in onehundred:
    tempsum += n
    print tempsum
sumsquare = tempsum**2

# find difference
diff = squaresum - sumsquare
print diff

# result 286913th person to have solved this problem
# result 25164150 
