import random
com_score = 0
usr_score = 0

while True:
    option = ['rock','paper','scissors']
    a = random.choice(option)
    
    usr_input = input('''Enter your option
                      1.ROCK
                      2.PAPER
                      3.SCISSORS
                      
                      press q to quit
                      
                      Enter your value''')
    
    if usr_input.isdigit()==True:
        usr_input = int(usr_input)
        if option[usr_input-1]==a:
            com_score,usr_score = com_score,usr_score
            print("DRAW")
        elif option[usr_input-1]=='rock':
            if a == 'paper':
                com_score = com_score + 1
                print("COMPUTER WINS")
                print("COMPUTER SCORE",com_score,"PLAYER SCORE",usr_score)
                print(" ")
            elif a == 'scissors':
                usr_score = usr_score + 1
                print("PLAYER WINS")
                print("COMPUTER SCORE",com_score,"PLAYER SCORE",usr_score)
                print(" ")
            
        elif option[usr_input-1]=='paper':
            if a == 'rock':
                usr_score = usr_score + 1
                print("PLAYER WINS")
                print("COMPUTER SCORE",com_score,"PLAYER SCORE",usr_score)
                print(" ")
            elif a == 'scissors':
                com_score = com_score + 1
                print("COMPUTER WINS")
                print("COMPUTER SCORE",com_score,"PLAYER SCORE",usr_score)
                print(" ")
            
        elif option[usr_input-1]=='scissors':
            if a == 'paper':
                usr_score = usr_score + 1
                print("PLAYER WINS")
                print("COMPUTER SCORE",com_score,"PLAYER SCORE",usr_score)
                print(" ")
            elif a == 'rock':
                com_score = com_score + 1
                print("COMPUTER WINS")
                print("COMPUTER SCORE",com_score,"PLAYER SCORE",usr_score)
                print(" ")        
    
    elif usr_input.isdigit() == False:
        if str(usr_input) == 'q':
            print("Final Score")
            print("")
            print("COMPUTER SCORE",com_score,"PLAYER SCORE",usr_score)
            break
        else:
            print("INVALID INPUT")
            break