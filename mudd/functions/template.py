
last_in = ""

def stndrdprmt():
    global last_in
    last_in = input("what would you like to do?")
    
inventory = ["pocketlint", " a pocket", "nothing"]
def check_constant():
    if last_in == "stats":
        print(health + fortitude + intellect + agillity + charisma + armor)
    elif last_in == "inventory":
        print(inventory)

def chk_last_in():
    return last_in == "stats" or last_in == "inventory"
        




while True:
    stndrdprmt()
    print(last_in)
    if chk_last_in():
        check_constant()
  

        
    else:
        print("didnt work " + last_in)
