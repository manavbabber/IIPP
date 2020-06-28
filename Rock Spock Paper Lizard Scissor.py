import random
def name_to_number(name):
    if(name=='rock'):
        return 0
    elif(name=='Spock'):
        return 1
    elif(name=='paper'):
        return 2
    elif(name=='lizard'):
        return 3
    elif(name=='scissors'):
        return 4
    else:
        return name,"is an invalid name"
def number_to_name(number):
    if(number == 0):
        return 'rock'
    elif(number == 1):
        return 'Spock'
    elif(number == 2):
        return 'paper'
    elif(number == 3):
        return 'lizard'
    elif(number == 4):
        return 'scissors'
    else:
        return number,"is an invalid number"
def rpsls(player_choice):
    print ""
    print "Player chooses",player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses",comp_choice
    difference = (comp_number-player_number)%5
    if(difference == 0):
        print "Player and computer tie!"
    elif(difference == 1 or difference == 2 ):
        print "Computer wins!"
    elif(difference == 3 or difference == 4 ):
        print "Player wins!"
    else:
        print "Incorrect input"
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")