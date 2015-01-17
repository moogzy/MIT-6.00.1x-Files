guess = 50
low = 0
high = 100

print "Please think of a number between 0 and 100!"

while True:
    print "Is you secret number %i?" % (guess)
    print "Enter 'h' to indicate the guess is too high.",
    print "Enter 'l' to indicate the guess is too low.",
    usr_input = raw_input("Enter 'c' to indicate I guessed correctly.").lower()
    
    if usr_input == "h":
        high = guess
        guess = (low + high) / 2
    elif usr_input == "l":
        low = guess
        guess = (high + low) / 2
    elif usr_input == "c":
        print "Game over. Your secret number was: %i" % (guess)
        break
    else:
        print "Sorry, I did not understand your input."
        continue
    