import random 
choices = ['rock','paper','scissors'] #lists
noWinner = True

def winphrase(name): #function
    print(name +", you won!")
          
playername = input("Enter your name: ")
while noWinner: #loops
    print("Let's play rock paper scissors!")
    computerplay = random.choice(choices)
    playerinput = 'q'
   
    while playerinput not in choices:
        playerinput=input("Rock, paper, scissors, shoot! ")
        if playerinput == 'q' or playerinput == 'quit':
            noWinner = False
            print("Bye!")
            break
        if playerinput not in choices: #conditionals
            print("Sorry, I don't understand. Enter 'rock' 'paper' 'scissors' or 'quit' ")
    
    print("I choose..." + computerplay + "!")

    if playerinput==computerplay:
        print("It was a tie!")
    else:
        print('someone won.')
        winphrase(playername)
