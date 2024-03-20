import random

class RockPaperScissorsGame:
    def __init__(self):
        self.score = 0
        self.rounds_played = 0

    def get_computer_choice(self):
        choices = ['rock', 'paper', 'scissors']
        return random.choice(choices)

    def play_round(self, user_choice, computer_choice):
        self.rounds_played += 1

        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
            self.score += 1
            return 'win'
        else:
            self.score -= 1
            return 'lose'