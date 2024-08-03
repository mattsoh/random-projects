print("""You are stuck in a prison. You have to escape.
      There's a bed, a toilet, and a small window. What do you do?
        1. Bribe the guard.
        2. Feign a medical emergency
        3. Examine the cell.
        4. Pick the lock.
      """)
choice = input("Input: ")
if choice == "1":
    print("You try to signal to the guard, but there is no response.")
    quit()
elif choice == "2":
    print("You decide to drop to the floor in the noisiest way possible. The guard notices and runs over to you")
elif choice == "3":
    print("You find nothing")
    quit()
elif choice == "4":
    print("There is nothing to pick the lock with")
    quit()
else:
    print("Invalid input")
    quit()

#Continue on with another action
            
