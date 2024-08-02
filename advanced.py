class Scene:
    def __init__(self, description, choices, next = []):
        self.description = description
        self.choices = choices
        self.next = next #Branches
    def run(self):
        print(self.description)
        print("Here are your choices:")
        while True:
            for i,c in enumerate(self.choices):
                print(f"Choice {i+1}: {c}")
            choice = input("Which one do you pick? \n Input:")
            if choice.isdigit() and 0 < int(choice) <= len(self.choices):
                break
            else:
                print("Invalid input")
        # Paths after choice is chosen
        
scenes = {}     
scenes["start"] = Scene("You are in a prison cell. There's a bed, a toilet, and a small window. What do you do?", ["Bribe the guard", "Feign an emergency", "Examine the cell", "Pick the lock"])
scenes["start"].next = ["branch1", "branch2"]
scenes["start"].run()
