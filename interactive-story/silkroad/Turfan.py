# from colorama import Fore
import Intro
from Commands import shows
print("Welcome to Turfan!")
print("Turfan’s many inns serve as gathering places for rest, refuelling and exchange of ideas and goods.\nOne of the famous parts of Turfan is the Karez water system. This ancient system provides water for all the residents (known as Turfan water). Using snow and letting the heat melt it, the refreshing water travels in underground mud tunnels to a distribution centre.")
yesno = int(input("Do you want to feed your camels for 10 silk?(press 1). They're starving? \nPress 2 if you don't want to.\nInput:"))
Intro.silk-=100
shows()
if yesno == 1:
  print("Amazing, the camels are feeling a lot better now.\nBut you do not need them any more though. However, you sell them for 5 porcelain bowls.")
  Intro.porc+=5
  shows()
else:
  qn = int(input("Do you want to sell the camels now for 5 porcelain?(press 1 for yes, 2 for no)\nInput:"))
  if qn == 1:
    print("You have sold the camels successfully.")
    shows()
  else:print("You realise the camels stopped breathing, but you don't need them anymore. But you can't sell them as they are not worth anything.")
print("Say goodbye to the cool Turfan water, as you start going to Samarkand through mountains.")
