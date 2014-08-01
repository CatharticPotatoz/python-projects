
last_in = ""

health = 20
fortitude = 5
intellect = 7
agillity = 7
charisma = 7
armor = 5

##########################################################################################


grassy_noll = ("your surouded by thickets of grass that stretch out as far as you can see in any direction. out in the distance you can see a house in the opposite direction you see a single tree. the rest of the field seems eirily empty.")






























###################################################################################################

def look_room():
    global last_in
    if last_in == "look" or last_in == "look around":
        print(room)

    
def stndrdprmt():
    global last_in
    last_in = input("what would you like to do?")
    
inventory = ["pocketlint", " a pocket", "nothing"]
def check_constant():
    if last_in == "stats":
        print(health + "" + fortitude + "" + intellect + "" + agillity + "" + charisma + "" + armor)
    elif last_in == "inventory":
        print(inventory)

def chk_last_in():
    return last_in == "stats" or last_in == "inventory"
#def Master_temp():        
    while True:
        stndrdprmt()
        if chk_last_in():
            check_constant()
        #else

room = grassy_noll

while True:
    stndrdprmt()
    if chk_last_in():
        check_constant()
  

        
    else:
        print("you " + last_in + ". after " +last_in + "ing for hours you grow weary and decide to take a nap.")
        break
print("you wake up from your nap feeling rejuvinated + 1 to health and + 1 to intellect")
#health + 1 = health
#intellect + 1 = intellect

Master_temp()
    
