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
choice = ask(["Bribe the guard", "Feign an emergency", "Examine the cell", "Pick the lock"])