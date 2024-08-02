from colorama import Fore
from Commands import theend
qn = int(input("Are you going to travel at day(press 2) or at night (press 1)\nInput:"))
if qn == 1:
  print("The immense coldness of the Mountain takes your life along with you. ")
  theend()
else:
  print("The heat of the sun warms you a bit as you travel through the immense coldness")
  print("You arrive at Samarkand. Samarkand is by the Fergana valley. This city is home to around 100 merchants. This city is founded by the Persians and remained a centre of Persian-Sogdian civilisation. The Persians built a very beautiful city, even Alexander the Great wanted to add this place to his empire. He also visited multiple times.\nThis is where traders can take a break by enjoying the sweet fruit and fresh bread.")
