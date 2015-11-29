
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

print("Please think of a number between 0 and 100!")
x = int(raw_input())
low = 0
high = x
ans = (high + low)/2

print "Is your secret number", ans

print ("Enter 'h' to indicate that the guess is too high. Enter 'l' to indicate that the guess is too low. Enter 'c' to indicate I guessed correctly.")

#Up until this point it works fine

x = raw_input()

if x == 'h':
    low = 0
    high = ans
    ansh = (high + low)/2
    print "Is your secret number", ansh

elif x == 'l':
    low = ans
    high = 100
    ansl = (high + low)/2
    print "Is your secret number", ansl

elif x == 'c':
    print ("Cool")

else:
    print "I don't know what this means"
