class Scene:
    def __init__(self, description, choices, paths, next, correct, last = False):
        self.description = description
        self.choices = choices
        self.next = next #Branches
        self.paths = paths
        self.correct = correct # [2, 4, 6]
        # self.incorrect = incorrect
        self.last = last
    def run(self):
        print(self.description)
        print("Here are your choices:")
        while True: # Player repeating themselves
            while True: # Input validation
                for i,c in enumerate(self.choices):
                    print(f"Choice {i+1}: {c}")
                choice = input("Which one do you pick? \n Input:")
                if choice.isdigit() and 0 < int(choice) <= len(self.choices):
                    break
                else:
                    print("Invalid input")
            # Paths after choice is chosen
            print(self.paths[int(choice)-1])
            if int(choice) in self.correct:
                if self.last:
                    print("Wow, you have won. Make sure to share the game")
                else:
                    scenes[self.next[int(choice)]].run()
                quit()
        
scenes = {}     
scenes["start"] = Scene("You are in a prison cell. There's a bed, a toilet, and a small window. What do you do?",
                        ["Bribe the guard", "Feign an emergency", "Examine the cell", "Pick the lock"],
                        ["That fails", "That fails too", "You find a way out", "That fails"], {3: "cell_escape"},[3])
scenes["cell_escape"] = Scene("You start running ... you reach a fork",
                              ["Turn left","Turn right"],
                                ["You get caught, you lose!","You escape, congratulations!"], {2: "win"}, correct = [2], last=True)
scenes["start"].run()
