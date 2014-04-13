# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

# initialize global variables used in your code
secret = None
low = 0
high = 100
guess_limit = 7
guesses_remaining = guess_limit

# helper function to start and restart the game
def new_game():
    global secret
    global guesses_remaining

    guesses_remaining = guess_limit
    secret = random.randrange(low, high)
    print 'New Game. Guess Range [%s,%s)'%(low, high)
    print 'You have %s guesses'%guesses_remaining

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global high
    global guess_limit
    high = 100
    guess_limit = calc_guess_limit(low, high)
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global high
    global guess_limit
    high = 1000
    guess_limit = calc_guess_limit(low, high)
    new_game()

def input_guess(guess):
    # main game logic goes here
    global guesses_remaining
    guess_num = int(guess)

    if guess_num == secret:
        print "Correct!"
        return

    if guess_num < secret:
        print "Higher!"
    elif guess_num > secret:
        print "Lower!"

    guesses_remaining -= 1
    if guesses_remaining <= 0:
        print 'Sorry, you have run out of guesses!'
        new_game()
        return
    print 'Guesses Remaining: %s'%guesses_remaining

def calc_guess_limit(low, high):
    return int(math.ceil(math.log(high - low + 1, 2)))

# create frame
frame = simplegui.create_frame("Guess", 200, 200)
# register event handlers for control elements
range_100 = frame.add_button('Range 100', range100)
range_1000 = frame.add_button('Range 1000', range1000)
guess = frame.add_input("Your Guess:", input_guess, 50)
# call new_game and start frame
new_game()
