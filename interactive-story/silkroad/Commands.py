# from colorama import Fore, Style, Back
# from PIL import Image
def line():
  print("----------------------------------------")
def shows():
  from Intro import silk,porc
  print("bolts of silk left: %s"%silk)
  print("porcelain bowls left: %s"%porc)

def theend():
  from playsound import playsound

# for playing note.wav file
  playsound('/Death.mp3')
  print("THE END")
  print( "Thank you for playing")
  shows()
  iy = input("Press [space] to exit")
  if iy == " ":
    quit()
def taka():
  filename = "Pictures//Taka.jpg"
  import webbrowser
  webbrowser.open(filename)
  #im = Image.open("Pictures//Taka.jpg")
  #im.show()
  print("The fertile lands of Chang’an slowly transform to a harsh desert as the caravan bends its way towards the north-west. Traveling on camel is slow and brutal through sand dunes with varying height, even as high as a skyscraper! Looking across the horizon, you spot the Flaming Mountains, noticeable for it brilliant red cliffs.")
  qn = int(input("Do you want to go north of the Taklimakan desert which is a longer route (press 1), or go directly through the desert which is a shorter route (press 2).\nInput:"))
  line()
  if qn == 1:
    print("You have chosen to go north of the Taklimakan desert. Going directly through the Taklimakan desert is suicide; it is too hot.")
  else:
    print("As you travel through the immense heat of the desert, sweat pours from your face. Collapsing to the rough sand, you lose consciousness. But it is too late to realise your mistake.")
    theend()