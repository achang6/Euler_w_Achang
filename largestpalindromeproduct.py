# find largest palindrom product of 2 3-digit numbers

# assemble all 3 digit integers
threedigits = range(100,1000)
product = 0
iampalindrome = 0
iamlargestpalindrome = 0

# double for for all products
for i in threedigits:
    for j in threedigits:
        # yeah
        product = i * j
        # string converion 
        monkey = str(product)
        # palindrome comparison
        # found the str[::-1] on internet
        # something about splicing the string backwards
        if monkey == monkey[::-1]:
            # move product up as a palindrome candidate
            iampalindrome = product
            # compare leading to newest candidate
            if iampalindrome > iamlargestpalindrome:
                # boot the old candidate
                iamlargestpalindrome = iampalindrome
# crown the king
print(iamlargestpalindrome)

# 273212th person to have solved this problem
