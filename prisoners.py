# Setup
import os
from random import randint as rand

choice = []


# Modes
def computer():
    wipe()
    print("You chose to play against the computer")
    programs = ["Random", "Tit for Tat", "Friedman", "Joss"]
    print("-------------------------------------------")
    print("Which program would you like to play against?")
    for i, program in enumerate(programs):
        print(f"{program} - {i+1}")
    option = input()
    if option.isdigit():
        option = int(option)
        if option == len(programs):
            option = rand(0, len(programs) - 1)
    else:
        computer()
    game_len = int(input("Enter game length (rounds): "))
    game("You", programs[option], game_len)
    present_score("You", option)


def twoplayer():
    wipe()
    print("2 player mode selected")
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")
    game_len = int(input("Enter game length (rounds): "))
    game(player1, player2, game_len)
    present_score(player1, player2)


# General functions
def score():
    p1, p2 = 0, 0
    for choices in choice:
        if choices == "dd":
            p1 += 1
            p2 += 1
        elif choices == "cc":
            p1 += 3
            p2 += 3
        elif choices == "dc":
            p1 += 5
        elif choices == "cd":
            p2 += 5
    return p1, p2


def wipe():
    os.system('cls' if os.name == 'nt' else 'clear')


def out():
    for moves in choice:
        print(f"|{moves[0]:^2}|{moves[1]:^2}|")


def terminal():
    wipe()
    print("Prisoner's Dilemma")
    print("------------------")
    print("2 Player Game - 1")
    print("Play the Computer - 2")
    print("Hold a Tournament - 3 (Unavailable)")  # Indicate unavailability
    option = input()
    if option == "1":
        twoplayer()
    elif option == "2":
        computer()
    elif option == "3":
        print("Option not available yet")
    else:
        terminal()


def game(a, b, game_len):
    for _ in range(game_len):
        achoice = play(a, 0)
        bchoice = play(b, 1)
        choice.append([achoice, bchoice])


def play(p, num):
    if p.isdigit():
        p = int(p)
        if p == 1:
            return chr(rand(99, 100))
        elif p == 2:
            return t4t(num)
        elif p == 3:
            return Friedman(num)
        elif p == 4:
            return Joss()
        else:
            computer()
    else:
        return player(p)


def present_score(player1, player2):
    wipe()
    out()
    scores = score()
    if scores[0] > scores[1]:
        print(f"{player1} won {scores[0]}-{scores[1]}")
    elif scores[1] > scores[0]:
        print(f"{player2} won {scores[1]}-{scores[0]}")
    else:
        print(f"You Drew {scores[0]}-{scores[1]}")


# Programs
def player(p):
    wipe()
    print(p)
    print("|p1|p2|")
    out()
    ch = input("Defect (d) or Cooperate (c): ")
    if ch in ("d", "c"):
        return ch
    else:
        return player(p)


def t4t(num):
    if choice:
        return choice[-1][num - 1]
    return "c"


def random():
    return chr(rand(99, 100))


def Friedman(num):
    actions = [move[num - 1]
