# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the follwing pass statement and fill in your code below
    # convert name to number using if/elif/else
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    else: #must be scissors?
        return 4
    # don't forget to return the result!


def number_to_name(number):
    # delete the follwing pass statement and fill in your code below
    # convert number to a name using if/elif/else
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    else:
        return 'scissors'
    # don't forget to return the result!


def rpsls(player_choice):
    # delete the follwing pass statement and fill in your code below
    # print a blank line to separate consecutive games
    print '\r\n'
    # print out the message for the player's choice
    print 'Player chooses %s' % player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_choise_value = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    ai_choise_value = random.randrange(0,4)
    # convert comp_number to comp_choice using the function number_to_name()
    ai_choice = number_to_name(ai_choise_value)
    # print out the message for computer's choice
    print 'Computer chooses %s' % ai_choice
    # compute difference of comp_number and player_number modulo five
    diff = (player_choise_value - ai_choise_value)% 5
    # use if/elif/else to determine winner, print winner message
    if diff == 1 or diff == 2:
        print 'Player wins!'
    elif diff == 3 or diff == 4:
        print 'Computer wins!'
    else:
        print 'Player and computer tie!'


if __name__ == '__main__':
    # test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")
