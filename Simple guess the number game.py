secret_number = 12 #Assigning or initializing variable.
min_chance = 0
max_chance = 7

x = 7         #Assigning a value for x to see the no of turns in guess (line-9), by using a formatted string in the guess variable.

while min_chance < max_chance:

    guess=int(input(f"Guess the number between 0 - 30 in {x} turns: "))   #If min chance < max chance ask guess and min chance will be +1.
    min_chance += 1
    x -= 1                                      #Every time the turns will be -1 after each turn.

    if guess==secret_number:    #If the condition is true print won and break the loop.
        print("You won!")
        break
else:                         #If the condition is false and out of turns u will get out of loop and print next line else that is lost.
    print("You lost!")