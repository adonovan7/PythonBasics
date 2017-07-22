print "I will now count my chickens:"

# dont forget order of operations: PEDMAS
# / operator rounds down
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
    # recall that the "%" character is a modulus, not a percent
    # its the remainder from division of two numbers
    # ex: 25 * 3 % 4 = 75 % 4 = 3 since 4 goes into 75 18 times (72)
    # remainder: 3
    # therefore the expression returns 100-3 = 97

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print 7.0 / 4.0 # floats point number gives decimal 1.75
print 7/4 # returns 1
