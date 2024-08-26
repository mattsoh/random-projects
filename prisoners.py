#setup
import os
from random import randint as rand
choice=[]
#modes
def computer():
    wipe()
    print("You have chosen to play against the computer")
    computer_programs=["Random","Tit for tat", "Freidman","Joss"]
    print("-------------------------------------------")
    print("Which program would you like to play against?")
    for i in range(len(computer_programs)+1):
        if i == len(computer_programs):
            print(f"Choose for me - {i+1}")
        else:
            print(f"{computer_programs[i]} - {i+1}")
    option=input()
    if option.isdigit():
        option=int(option)
        if option == len(computer_programs):
            option=rand(0,len(computer_programs)-1)
    else:
        computer()
    gamelen=int(input("Please enter game length (number of rounds):  "))
    game("You",str(option),gamelen)
    presentscore("You",option)
def twoplayer():
    wipe()
    print("2 player mode selected")
    player1=input("Please enter player 1 name:  ")
    player2=input("Please enter player 2 name:  ")
    gamelen=int(input("Please enter game length (number of rounds):  "))
    game(player1,player2,gamelen)
    presentscore(player1,player2)
#general functions
def score():
    p1score=0
    p2score=0
    for i in choice:
        choices=i[0]+i[1]
        if choices == "dd":
            p1score+=1
            p2score+=1
        elif choices == "cc":
            p1score+=3
            p2score+=3
        elif choices == "dc":
            p1score+=5
        elif choices == "cd":
            p2score+=5
    return [p1score,p2score]
def wipe():
    os.system('cls' if os.name =='nt' else 'clear')
def out():
    for i in choice:
        print(f"|{i[0]:^2}|{i[1]:^2}|")
def terminal():
    wipe()
    print("Prisoner's Dilemma")
    print("------------------")
    print("2 player game - 1")
    print("Play the computer - 2")
    print("Hold a Tournament - 3")
    option=input()
    if option=="1":
        twoplayer()
    elif option=="2":
        computer()
    elif option=="3":
        print("option not available yet")
    else:
        terminal()
def game(a,b,gamelen):
    for i in range(gamelen):
        achoice=play(a,0)
        bchoice=play(b,1)
        choice.append([achoice,bchoice])
def play(p,num):
    if p.isdigit():
        p=int(p)
        if p==1:
            c=random()
        elif p==2:
            c=t4t(num)
        elif p==3:
            c=Freidman(num)
        elif p==4:
            c=Joss()
        else:
            computer()
    else:
        c=player(p)
    return c
def presentscore(player1,player2):
    wipe()
    out()
    n=score()
    if n[0]>n[1]:
        print(f"{player1} won {n[0]}-{n[1]}")
    elif n[1]>n[0]:
        print(f"{player2} won {n[1]}-{n[0]}")
    else:
        print(f"You drew {n[0]}-{n[1]}")
    
#programs
def player(p):
    wipe()
    print(p)
    print("|p1|p2|")
    out()
    ch=input("defect (d) or cooperate (c):  ")
    if ch=="d" or ch=="c":
        return ch
    else:
        return player(p)
def t4t(num):
    if len(choice)>0:
        return choice[-1][num-1]
    return "c"
def random():
    return chr(rand(99,100))
def Freidman(num):
    a=[]
    for i in choice:
        a.append(i[num-1])
    if "d" in a:
        print("d")
        return "d"
    print("c")
    return "c"
def Joss():
    return chr(round(rand(994,999)/10))
terminal()
