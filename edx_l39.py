
# Program to search for a secret number

# x = 12345
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = x
# ans = (high + low)/2.0
# while abs(ans**2 - x) >= epsilon:
#     print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0
# print('numGuesses = ' + str(numGuesses))
# print(str(ans) + ' is close to square root of ' + str(x))

# Above is the code for bisection search. Now I will try my code

# We know that the x input must come from raw input by the user.

x = raw_input("Please think of a number between 0 and 100!")
# epsilon = 0.01
# numGuesses = 0
low = 0.0
high = x
ans = (high + low ) /2.0

print "Is your secret number %r" % (ans)

print \
("Enter 'h' to indicate that the guess is too high. Enter 'l' to indicate that the guess is too low. Enter 'c' to indicate I guessed correctly.")

y = raw_input()






