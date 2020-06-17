#########################################
#####################
###The Game of Dice
#########################

#Another command line game in python
#We'll make use of data structures
#
#Game play: To simulate the flipping coin
#To have the program to randomly select a side of the coin
#Give the user the ability to guess the side the coin landed on
#If the user guessed the correct side then win
#If they guessed the incorrect side then they'll lose
#########################################
# import random
# right=random.choice(['head','tail'])
# guess_number=input("Please guess head or tail:")
# if guess_number==right:
#     print("You Win, its {right}")
#     print(right)
# else:
#     print(F"you lose, it is {right}")


import random
times=0
while True:
    right_number=random.choice(['head','tail'])
    guess_number=input("Please guess head or tail:")
    if guess_number==right_number:
        print(F"you win,it's {right_number}")
        times+=1
    else:
         print(F"You lose, its{right_number}")
    play_again=input("Do you want to play again? Y/N: ")
    if play_again=='Y':
        continue
    else:
        break
print("You have won ", times, "times")

"""
Tuples are immutable data structure
tuples like lists holds items in memory
tuples can be indexed
tuples can be sliced
tuples can be reassigned
tuples can be iterated over because they are iterables
"""

"""
Dictionary is key/value mappings 
It is very important due to its fast properties
can retrieve, index, very quickly, 0(1) constant time
"""

