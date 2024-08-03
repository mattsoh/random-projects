#Abstraction

def ask(choices):
    print("Here are your choices:")
    while True:
        for i,c in enumerate(choices):
            print(f"Choice {i+1}: {c}")
        choice = input("Which one do you pick? \n Input:")
        if choice.isdigit() and 0 < int(choice) <= len(choices):
            return int(choice)
        else:
            print("Invalid input")
            
print("""You are stuck in a prison. You have to escape.
There's a bed, a toilet, and a small window. What do you do?
      """)
key = False
while True:
    choice = ask(["Bribe the guard", "Feign an emergency", "Examine the cell", "Pick the lock"])

    if choice == 1:
        print("You try, but you fail.")
    elif choice == 2:
        print("The guard rushes over, but nothing happens after that.")
    elif choice == 3:
        print("You find a key.")
        key = True
    else:
        if key:
            break
        else: print("You don't even have a key.")
            
# Continue and do something

print("You start running in one direction, and reach a fork. What will you do?")
choice = ask(["Left", "Right"])
# Continue on 


