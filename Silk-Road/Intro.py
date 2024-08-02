from colorama import Fore, Style
from Commands import line,theend,taka,shows
from PIL import Image
im = Image.open("Pictures//Map.jpg")
im.show()
print("You will be starting from Chang'an and will be trying to get to Merv in Serbia.")
print("You know a friendly merchant who will pay well for your goods.")
name = input("What is your name?\nInput:")
line()
print("Welcome "+name)
print(name+", you currently have 300 bolts of silk as well as 100 bowls of porcelain. Along the way you will recieve help, be threatened by bandits or experience extreme temperatures. You will have to travel from Chang'an to Merv, earn a profit, and beat the game!")
silk = 300
porc = 100
shows()
line()
print(Fore.YELLOW,Style.BRIGHT,"Welcome to the golden age of the Silk Road, during the Tang Dynasty(618-907AD). You start off at the marketplace and breathe the heavy perfume all around you. Musicians traveled from far and wide to perform in Chang’an, bearing a wide variety of instruments that had never before been seen there. You also hear Buddhist chants and stories promoting Islamic values.")
yesno = int(input("If you want, you can enlist help from chinese guards for 10 bolts of silk (press 1). Do you want to try? Press 1 for yes, 0 for no\nInput:"))
line()
if yesno == 1:
  print("You have successfully employed 10 guards at a price of 10 silk pieces.")
  silk -=10
  shows()
  camel = int(input("Do you want to hire 5 camels to carry your valuables for 3 porcelain bowls. Press 0 for yes, 1 for no\nInput:"))
  line()
  if camel == 1:
    shows()
    #print("savin' some valuables i see")
    print("After 2 days, you have only made a distance of 2km. The guards protecting you decide to abandon you as they have more things to do. Bandits take their chance to attack you and steal your valuables.")
    theend()
  else:
    print("Transaction completed")
    porc -=5
    shows()
else:
  print("Very well, lets go!")
  print("With no guards to protect you, you soon realise that you are vulnerable to bandits, and is a easy target.")
  theend()
line()
taka()