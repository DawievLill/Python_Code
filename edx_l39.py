
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

low = 0
high = 100
guessed = False #Initialise the loop with a False value. Get the loop to run till my guess is correct

while not guessed: #This was the loop that I needed to add in order to get it to run multiple times


    guess = (high + low)/2
    print ("Is your secret number %s?") % guess
    print ("Enter 'h' to indicate that the guess is too high. Enter 'l' to indicate that the guess is too low. Enter 'c' to indicate I guessed correctly.")
    x = raw_input()

    if x == 'h':
        high = guess

    elif x == 'l':
        low = guess

    elif x == 'c':
        guessed = True

    else:
        print ("Sorry, I didn't understand your input.")

print ("Game over. Your secret number was: %s") % guess
