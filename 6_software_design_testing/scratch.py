#%%
import random

# Print the options:
options = ['rock', 'paper', 'scissors']
print('(1) Rock\n(2) Paper\n(3) Scissors')
# Let the user choose
human_choice = options[int(input('Enter the number of your choice: ')) - 1]
# Print the user's choice
print(f'You chose {human_choice}')
# Make the computer choose one option amongst the options list
computer_choice = random.choice(options)
# print the computer's choice
print(f'The computer chose {computer_choice}')
# Print the results
if human_choice == 'rock':
    if computer_choice == 'paper':
        print('Sorry, paper beat rock')
    elif computer_choice == 'scissors':
        print('Yes, rock beat scissors!')
    else:
        print('Draw!')
elif human_choice == 'paper':
    if computer_choice == 'scissors':
        print('Sorry, scissors beat paper')
    elif computer_choice == 'rock':
        print('Yes, paper beat rock!')
    else:
        print('Draw!')
elif human_choice == 'scissors':
    if computer_choice == 'rock':
        print('Sorry, rock beat scissors')
    elif computer_choice == 'paper':
        print('Yes, scissors beat paper!')
    else:
        print('Draw!')
# %%
import random
class RPS:
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        print('(1) Rock\n(2) Paper\n(3) Scissors')
    
    def cpu_choice(self):
        self.cpu = random.choice(self.options)
        print(f'The computer chose: {self.cpu}')
        return self.cpu
    
    def human_choice(self):
        self.user_choice = self.options[int(input('Enter the number of your choice: '))-1]
        print(f'The user chose: {self.user_choice}')
        return self.user_choice
    
    def results(self):
        if self.user_choice == 'rock':
            if self.cpu == 'paper':
                print('Sorry, paper beat rock')
            elif self.cpu == 'scissors':
                print('Yes, rock beat scissors!')
            else:
                print('Draw!')
        elif self.user_choice == 'paper':
            if self.cpu == 'scissors':
                print('Sorry, scissors beat paper')
            elif self.cpu == 'rock':
                print('Yes, paper beat rock!')
            else:
                print('Draw!')
        elif self.user_choice == 'scissors':
            if self.cpu == 'rock':
                print('Sorry, rock beat scissors')
            elif self.cpu == 'paper':
                print('Yes, scissors beat paper!')
            else:
                print('Draw!')
    
    def initialize(self):
        self.cpu_choice()
        self.human_choice()
        self.results()
        
rps = RPS()
rps.initialize()
# %%
import random

class JanKenPon:
    options = ['rock', 'paper', 'scissors']
    def __init__(self):
        self.computer_choice = None
        self.human_choice = None
    
    def get_computer_choice(self):
        self.computer_choice = random.choice(self.options)
        return self.computer_choice
    
    def get_human_choice(self):
        self.human_choice = self.options[int(input('Input a number for your choice: '))-1]
        return self.human_choice

    def print_options(self):
        for idx, choice in enumerate(self.options):
            print(f'({idx+1}) {choice}')

    def print_choices(self): 
        print(f'You chose {self.human_choice}, the computer chose {self.computer_choice}')
    
    def results(self):
        if self.human_choice == 'rock':
            self.human_beats = ['scissors']
            self.human_loses_to = ['paper']
        elif self.human_choice == 'paper':
            self.human_beats = ['rock']
            self.human_loses_to = ['scissors']
        elif self.human_choice == 'scissors':
            self.human_beats = ['paper']
            self.human_loses_to = ['rock']
        return self.human_beats, self.human_loses_to

    def print_win_lose(self):
        if self.computer_choice in self.human_beats:
            return True
        elif self.computer_choice in self.human_loses_to:
            return False
        else:
            return None

    def print_result(self):
        if self.print_win_lose() == True:
            print('You Won!')
        elif self.print_win_lose() == False:
            print('Sorry, the computer won')
        elif self.print_win_lose() == None:
            print("It's a Draw!")
            
    def simulate(self):
        self.print_options()
        self.get_human_choice()
        self.get_computer_choice()
        self.results()
        self.print_choices()
        self.print_result()

game = JanKenPon()
game.simulate()
# %%
