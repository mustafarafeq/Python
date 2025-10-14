# We want the game to our computer play against the user.
computer_choice = "scissors"
user_choice = input('Do you want rock, paper, or scissors? ')

if computer_choice == user_choice:
        print('TIE!') # so far we have an 'if' statement that says, if the computer choice variable is equal to the user_choice variable from their input, then print "Tie!".
## now we can figure out ways that the user can win since we only defined one print tied to one variable.
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You Win!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You Win!')
else:
      print('I Win!')