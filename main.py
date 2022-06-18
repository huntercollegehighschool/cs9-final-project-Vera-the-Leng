"""
Name(s): Vera Leng
Name of Project: 
"""
yourhealth = 4
yourattack = 2
goathealth = 3
goatattack = 3

def begin():
  print("While traveling on a long, abandoned path, you encounter a mysterious traveler. The mysterious traveler stops you and asks for you to retrieve a bag of gold from a cave at the top of a mountain and get it for them, and offers some gold in return for your efforts. Do you go up the mountain, or refuse.\n")
  choice = input("Enter M to go up the mountain or R to refuse.\n")
  while choice != "M" and choice != "R":
    print("You must choose either M or R. \n")
    choice = input("Enter M to go up the mountain or R to refuse.\n")
  if choice == "M":
    mountain()
  elif choice == "R":
    refuse()



def mountain():
  print("\nYou start walking up the mountain. Suddenly your path is blocked by a river, and you see a very thin branch going across it and a strong current in the water. Do you cross the river by walking on the branch, or braving the rapids?\n")
  choice = input("Enter B to walk across the branch or S to swim in the rapids.\n")
  while choice != "B" and choice != "S":
    print("You must choose either B or  R. \n")
    choice = input("Enter B to walk across the branch or S to swim in the rapids.\n")
  if choice == "B":
    branch()
  elif choice == "S":
    rapids()


def branch():
  print("\nYou attempt to walk across the thin branch, but it breaks under your feet, tossing you into the river. Do you attempt to cling to a broken piece of the branch or try swimming across the river?\n")
  choice = input("Enter C to cling to the branch or A to attempt to swim across.\n")
  while choice != "C" and choice != "A":
    print("You must choose either C or A. \n")
    choice = input("Enter C to cling to the branch or A to attempt to swim across.\n")
  if choice == "C":
    cling()
  elif choice == "A":
    drown()


def cling():
  print("\nYou clng to the branch for your dear life, and eventually float down to where the current is weaker and to shore. Eventually you make it out of the river, and continue on a path you see.\n")
  shore()


def drown():
  print("You attempt to swim across, only to get pulled down by the rapids, and drown. Game Over!")


def rapids():
  print("\nYou attempt to swim across the river, only to find yourself pulled downriver by the current. Do you attempt to swim across, or let yourself get pulled by the river?\n")
  choice = input("Enter A to attempt to swim across or P to get pulled by the river.\n")
  while choice != "P" and choice != "A":
    print("You must choose either C or A. \n")
    choice = input("Enter C to cling to the tree or A to attempt to swim across.\n")
  if choice == "P":
    pull()
  elif choice == "A":
    drown()


def pull():
  print("\nYou get pulled by the river, barely keeping your head above the water, and eventually end up on the other side. Eventually you make it out of the river, and continue on a path you see.\n")
  shore()
        

def shore():
  print("You walk up the mountain, until the path you are walking on turns right, slightly away from where you want to go. You also see a steep path that heads directly up the mountain.\n") 
  choice = input("Enter R to go on the path to the right or U to go on the path upwards.\n")
  while choice != "R" and choice != "U":
    print("You must choose either R or U.\n")
    choice = input("Enter R to go on the path to the right or U to go on the path upwards.\n")
  if choice == "R":
    pathright()
  elif choice == "U":
    pathup()



def pathup():
  print("\nYou start up the path, which starts heading up a cliff.")
  goatpath()

#GOATSSS


def goatpath():
  print("\nSuddenly, you get stopped by a vicious looking mountain goat blocking your path. Do you run away from the goat, grab a nearby stick and attack the goat, or use the stick to defend yourself from the goat?\n")
  print("Your health: ", yourhealth, "\nYour attack: ", yourattack, "\nGoat's health: ", goathealth, "\nGoat's attack: ", goatattack)
  choice = input("Enter A to attack the goat, D to defend from the goat, or R to run back down the path.\n")
  while choice != "R" and choice != "A" and choice != "D":
    print("You must choose either A, D, or R. \n")
    choice = input("Enter A to attack the goat, D to defend from the goat, or R to run back down the path.\n")
  if choice == "A":
    attackcliff()
  elif choice == "D":
    defendcliff()
  elif choice == "R":
    mountainending1()

def mountainending1():
  print("\nWhile fleeing from the killer goat, you slip on the path and fall to you death. Game Over!")

  

def attackcliff():
  print("\nYou attack the goat with your stick. It tumbles backwards and doesn't attack you back.")
  global yourhealth
  global yourattack
  global goathealth
  global goatattack 
  goathealth = int(goathealth) - int(yourattack)
  if goathealth <= 0:
    print("You kill the goat. Nice!")
    goatdie()
  else:
    print("Your health: ", yourhealth, "\nYour attack: ", yourattack, "\nGoat's health: ", goathealth, "\nGoat's attack: ", goatattack)
    choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    while choice != "A" and choice != "D":
      print("You must choose either A or D.\n")
      choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    if choice == "A":
      attackcliff()
    elif choice == "D":
      defendcliff()

def defendcliff():
  print("\nYou attempt to defend yourself with a stick, but end up slipping backwards and taking 1 damage from the goat.\n")
  global yourhealth
  global yourattack
  global goathealth
  global goatattack 
  yourhealth = int(yourhealth) - 1
  if yourhealth <= 0:
    print("You have died from a deadly goat attack. Game Over!")
  else:
    print("Your health: ", yourhealth, "\nYour attack: ", yourattack, "\nGoat's health: ", goathealth, "\nGoat's attack: ", goatattack)
    choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    while choice != "A" and choice != "D":
      print("You must choose either A or D.\n")
      choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    if choice == "A":
      attackcliff()
    elif choice == "D":
      defendcliff()
        
def goatdie():
  print("You continue walking. Finally, you encouunter the cave the traveler described. You walk into the cave, only to find a cult doing a ritual. They notice you, and offer to give you the gold only if you get initiated into the cult.\n")
  choice = input("Enter C to join the cult, or L to leave the cave.\n")
  while choice != "C" and choice != "L":
    print("You must choose either C or  L. \n")
    choice = input("Enter C to join the cult, or L to leave the cave.\n")
  if choice == "C":
    cult()
  elif choice == "L":
    sacrifice()

def cult():
  print("\nYou join the cult and get initiated. The traveler enters, getting their gold from you and giving you your riches. You live out your life happily as a member of the mountain cult. You won!")
  

def sacrifice():
  print("\n You try to leave the cave, only to find the traveler behind you, grinning while holding a knife. You get sacrificed for the cult. Game Over!")



def pathright():
  print("\nWhile you walk on the path, you encounter a fallen tree. You can either climb over it, or under it.\n")
  choice = input("Enter O to go over the tree, or U to go under it.\n")
  while choice != "O" and choice != "U":
    print("You must choose either O or U. \n")
    choice = input("Enter O to go over the tree, or U to go under it.\n")
  if choice == "O":
    overtree()
  elif choice == "U":
    undertree()


def overtree():
  print("\nYou climb over the tree, only to encounter a rabid mountain goat. Do you run back and hide under the tree, grab a nearby stick and attack the goat, or use the stick to defend yourself from the goat?\n")
  print("Your health: ", yourhealth, "\nYour attack: ", yourattack, "\nGoat's health: ", goathealth, "\nGoat's attack: ", goatattack)
  choice = input("Enter H to hide under the tree, A to attack the goat, or D to defend yourself from the goat.\n")
  while choice != "H" and choice != "A" and choice != "D":
    print("You must choose either H, A, or D.\n")
    choice = input("Enter H to hide under the tree, A to attack the goat, or D to defend yourself from the goat.\n")
  if choice == "H":
    hideover()
  elif choice == "A":
    attackover()
  elif choice == "D":
    defendover()

def hideover():
  print("\nYou attempt to hide underneath the tree, but get spotted and killed by the goat. Game Over!")


def attackover():
  print("\nYou attack the goat with your stick. It tumbles backwards and doesn't attack you back.")
  global yourhealth
  global yourattack
  global goathealth
  global goatattack 
  goathealth = int(goathealth) - int(yourattack)
  if goathealth <= 0:
    print("You kill the goat. Nice!")
    goatdie()
  else:
    print("Your health: ", yourhealth, "\nYour attack: ", yourattack, "\nGoat's health: ", goathealth, "\nGoat's attack: ", goatattack)
    choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    while choice != "A" and choice != "D":
      print("You must choose either A or D.\n")
      choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    if choice == "A":
      attackover()
    elif choice == "D":
      defendover()

def defendover():
  print("\nYou attempt to defend yourself with a stick, but end up pinned against the tree and taking 1 damage from the goat.\n")
  global yourhealth
  global yourattack
  global goathealth
  global goatattack 
  yourhealth = int(yourhealth) - 1
  if yourhealth <= 0:
    print("You have died from a deadly goat attack. Game Over!")
  else:
    print("Your health: ", yourhealth, "\nYour attack: ", yourattack, "\nGoat's health: ", goathealth, "\nGoat's attack: ", goatattack)
    choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    while choice != "A" and choice != "D":
      print("You must choose either A or D.\n")
      choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    if choice == "A":
      attackover()
    elif choice == "D":
      defendover()


def undertree():
  print("\nYou climb under the tree, only to see a rabid mountain goat out from under the tree. Do you hide where you are, or attack with a sharp stick from the tree?\n")
  print("Your health: ", yourhealth, "\nYour attack: ", yourattack, "\nGoat's health: ", goathealth, "\nGoat's attack: ", goatattack)
  choice = input("Enter H to hide by the tree, or A to attack the goat.\n")
  while choice != "H" and choice != "A":
    print("You must choose either H or A.\n")
    choice = input("Enter H to hide by the tree, or A to attack the goat.\n")
  if choice == "H":
    hideunder()
  elif choice == "A":
    attackunder()

def hideunder():
  print("\nYou hide under the tree, and the mountain goat doens't notice you. It eventually walks away, and you emerge from under the tree. Nice!")
  goatdie()

def attackunder():
  print("\nYou attack the goat with your stick, but get yourself stuck under the tree, giving the goat 1 damage and yourself 2.")
  global yourhealth
  global yourattack
  global goathealth
  global goatattack 
  goathealth = goathealth - 1
  yourhealth = yourhealth - 2
  if goathealth <= 0:
    print("You kill the goat. Nice!")
    goatdie()
  elif yourhealth <= 0:
    print("You have died from a deadly goat attack. Game Over!")
  else:
    print("Your health: ", yourhealth, "\nYour attack: ", yourattack, "\nGoat's health: ", goathealth, "\nGoat's attack: ", goatattack)
    choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    while choice != "A" and choice != "D":
      print("You must choose either A or D.\n")
      choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    if choice == "A":
      attackover()
    elif choice == "D":
      defendover()

def defendover():
  print("\nYou successfully defend yourself with a stick from under the tree, and cause the goat to take 1 damage from the sharp branches around you.\n")
  global yourhealth
  global yourattack
  global goathealth
  global goatattack 
  goathealth = goathealth - 1
  if yourhealth <= 0:
    print("You have died from a deadly goat attack. Game Over!")
  elif goathealth <= 0:
    goatdie()
  else:
    print("Your health: ", yourhealth, "\nYour attack: ", yourattack, "\nGoat's health: ", goathealth, "\nGoat's attack: ", goatattack)
    choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    while choice != "A" and choice != "D":
      print("You must choose either A or D.\n")
      choice = input("Enter A to attack the goat or D to defend from the goat.\n")
    if choice == "A":
      attackover()
    elif choice == "D":
      defendover()

def refuse():
  print("\nYou politely refuse the traveler's request, and continue walking. You feel an ominous feeling, but ignore it. Eventually, you start to feel tired. Do you set up camp and go to sleep, or continue walking?\n")
  choice = input("Enter S to set up camp and go to sleep or C to continue walking.\n")
  while choice != "S" and choice != "C":
    print("You must choose either S or C.\n")
    choice = input("Enter S to set up camp and go to sleep or C to continue walking.\n")
  if choice == "S":
    sleep()
  elif choice == "C":
    continuew()

def sleep():
  print("\nYou set up camp and peacefully fall asleep.\n However, you are soon abruptly awaked by the traveler, who is holding a knife to your throat. They offer you the choice of going to get their gold in the mountain again. Do you accept, or refuse again?\n")
  choice = input("Enter M to accept and go on the mountain quest, or R to refuse again.\n")
  while choice != "M" and choice != "R":
    print("You must choose either M or R.\n")
    choice = input("Enter M to accept and go on the mountain quest, or R to refuse again.\n")
  if choice == "M":
    mountain()
  elif choice == "R":
    refusal()

def refusal ():
  print("\nYou refuse the traveler again, and get killed for your impoliteness. Game Over!")

def continuew():
  print("\nYou continue walking, until you grow so tired that you simply collapse of exhaustion.\n When you wake up, you find the traveler holding a knife to your throat. They offer you the choice of going to get their gold in the mountain again. Do you accept, or refuse again?\n")
  choice = input("Enter M to accept and go on the mountain quest, or R to refuse again.\n")
  while choice != "M" and choice != "R":
    print("You must choose either M or R.\n")
    choice = input("Enter M to accept and go on the mountain quest, or R to refuse again.\n")
  if choice == "M":
    mountain()
  elif choice == "R":
    refusal()
begin()