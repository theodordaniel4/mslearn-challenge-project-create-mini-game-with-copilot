import random

score = 0  # Initialize score variable
rounds_played = 0  # Initialize rounds_played variable

def rock_paper_scissors():
    global score, rounds_played  # Declare score and rounds_played as global variables

    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    user_choice = input('Enter your choice (rock, paper, scissors): ')
    while user_choice not in choices:
        user_choice = input('Invalid choice. Enter your choice (rock, paper, scissors): ')

    print('Computer chose:', computer_choice)

    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print('You win!')
        score += 1
    else:
        print('You lose!')
        score -= 1

    rounds_played += 1  # Increment rounds_played by 1

    play_again = input('Do you want to play again? (yes/no): ')
    while play_again.lower() not in ['yes', 'no']:
        play_again = input('Invalid choice. Do you want to play again? (yes/no): ')

    if play_again.lower() == 'yes':
        rock_paper_scissors()
    else:
        print('Total rounds played:', rounds_played)  # Print the total rounds played
        print('Final score:', score)
        print('Thanks for playing!')

rock_paper_scissors()