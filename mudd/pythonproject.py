##from functions.class_stats import *
##from functions.func_libry import *
falsenameexist = False
reversetitle = False
title = "sir"
classlist = {
    "knight", "cleric", "wizard", "warlock", "hunter", "warrior", "assassin", "noble"
    }
classlist2 = {""," "
    }
base_health = 20
base_strength = 10
base_armor = 0


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



if title == "thing":
    base_charisma = 2
else:
    base_charisma = 10
base_intellect = 10
class knight():
    total_health = base_health + 5
    total_strength = base_strength + 5
    total_charisma = base_charisma + 2
    total_intellect = base_intellect

class cleric():
    total_health = base_health + 5
    total_strength = base_strength -2
    total_charisma = base_charisma 
    total_intellect = base_intellect + 5

class wizard():
    total_health = base_health - 2
    total_strength = base_strength - 2
    total_charisma = base_charisma + 3
    total_intellect = base_intellect + 3

class warlock():
    total_health = base_health - 5 
    total_strength = base_strength 
    total_charisma = base_charisma - 2
    total_intellect = base_intellect + 3

class hunter():
    total_health = base_health +2
    total_strength = base_strength +2
    total_charisma = base_charisma +3
    total_intellect = base_intellect +2
    
class warrior():
    total_health = base_health +6
    total_strength = base_strength +7
    total_charisma = base_charisma 
    total_intellect = base_intellect -3

class assassin(): 
    total_health = base_health 
    total_strength = base_strength -2
    total_charisma = base_charisma +5
    total_intellect = base_intellect +5
    
class noble():
    total_health = base_health - 2
    total_strength = base_strength - 3
    total_charisma = base_charisma + 8
    total_intellect = base_intellect + 2

class idiot():
    total_health = base_health 
    total_strength = base_strength 
    total_charisma = base_charisma 
    total_intellect = base_intellect   

        
while True:
    name = (input("whats your name?"))
    print(name + " are you sure thats your name?")
    correctname = (input())
    correctname = correctname.lower()
    if correctname == "no":
        print()
    elif correctname =="yes":
        break
    else:
        print("that was a yes or no question.")
print("whats your age")
while True:
    age = int((input()))
    if age == str(age):
        print("thats not a number!whats your actual age?")
    elif age > 100 and age < 1000:
        print("wow your old")
        break
    elif age < 10:
        print("wow your young")
        break
    elif age >= 1000:
        print(".....suuuuure")
        break
    elif age >= 10 and age <=100:
        break

print("you are " + str(age) + " years old")

gender = (input("whats your gender?"))
if gender == "male":
    title = "sir"
    print("your a guy!")
elif gender == "female":
    title = "lady"
    print("your a girl!")
else:
    title = "thing"
    print("congrats your an it!")

fromplace = (input("where are you from?"))
print("so let me get this right you are " + title + " Gretchan of Hoboken") 
profileconfirmation = (input())

if profileconfirmation == "yes":
    falsenameexist = True
    falsename = "Gretchan"
else:
    print("no no no thats not right. Oh! I know! is it " + title + " Bennidict Cumberbatch of " + fromplace + "?")
    confirm2 = (input())
    if confirm2 == "yes":
        falsenameexist = True
        falsename = "Bennidict Cumberbatch"
    else:
        print("oh damn I really thought i had it that time. but hey I got the place right......right?")
        input("Its on the tip of my tounge this time! really I promise it is! your name is .......")
        print("noooono no no no no.... dont intererupt me while im thinking! your name...")
        print("you are")
        if gender == "male":
            print("lady " + name + " of " + fromplace)
        elif gender == "female":
            print("sir " + name + " of " + fromplace)
        elif title =="thing":
            print("shemale " + name + " of " + fromplace)
        print("so....... did i get it right this time?")
        confirm3 = (input(""))
        if confirm3 == "yes":
                reversetitle = True
        else:
            print("oh I called you by the wrong gender? are you sure I mean you definatley look like one to me but what do i kno- I mean yes yes of course I knew you were a")
            if gender == "male":
                print("guy. I was just testing your observational skills....you get +50 to...uh..observationalisticism...")
            elif gender == "female":
                print("woman I was just testing your observational skills....you get +50 to...uh..observationalisticism...")
            else:
                print(" aha ha I knew that.......-akward silence-......")
while True:
    if falsenameexist == True:    
        classquestion = (input("so " + title + " " + falsename + " what class are you?"))
        break
    else:
        if reversetitle == True and gender == "male":
            classquestion = (input("so lady " + name + "what class are you?"))
            break
        elif reversetitle == True and gender == "female":
            classquestion = (input("so sir " + name + "what class are you?"))
            break
        else:
            classquestion = (input("so " + title + " " + name + " what class are you"))
            break
if classquestion not in classlist and classquestion not in classlist2:
    print("what the hell is a " + classquestion + "? oh silly me you are obviously a babling fool")
    clas = "babling fool"
    input("confirm your class, current class - " + clas)
    print("conragradulations you are now a " + clas)
    #break    
elif classquestion in classlist and classquestion not in classlist2 :
    clas = classquestion
    print("conragradulations you are now a " + clas)
    #break                           
elif classquestion in classlist2 and classquestion not in classlist:
    print("SPEAK UP! I cant hear you!")
if classquestion in classlist:
                clas = classquestion
if clas == "knight":
    Player = knight()
elif clas == "wizard":
    Player = wizard()
elif clas == "cleric":
    Player = cleric()
elif clas == "warlock":
    Player = warlock()
elif clas == "hunter":
    Player = hunter()
elif clas == "warrior":
    Player = warrior()
elif clas == "assassin":
    Player = assassin()
elif clas == "noble":
    Player = noble()
elif clas == "babling fool":
    player = idiot()
                               
print("here are your current stats: health " + str(Player.total_health))
print("                             strength" + str(Player.total_strength))
print("                             charisma" + str(Player.total_charisma))
print("                             intellect" + str(Player.total_intellect))
    
phys_adj = (input("now....tell me whats your best characteristic?"))
mental_adj = (input("So if you were to describe your personality in one word what would that word be?"))
print("hmmmm..... intersesting....")
print("so lets begin our story.")
pref_start = (input("where would you like your journey to start?"))
print("Well we dont have a good enough budget to go there so get over it.")
print("You awaken in a dark chamber with no memory of the last few days. Armed only with your " + mental_adj + " and " + phys_adj)
first_action = (input("what will you do?"))
print("you start to " + first_action + " but as you do a giant snake slithers out from the shadows distracting you from the origonal task.")
second_action = (input("as the snake begins to rear its head you start taking note of your surroundings. There seems to be no exits, you cant even find any walls other than the one behind you. What will you do?"))
print("you attempt to " + second_action + " but the snake lunges forward, as its head hurtles twords you, its fangs glisening in the dim torch light you " + second_action)
print("luckily for you it seems as though the snake was distracted by the sight of your " + phys_adj)
third_action = (input("this would be an opportune time for you to attempt to 'SNEAK AWAY' but I mean IM just the narator here right, do what you want"))
if third_action == "sneak away":
    print("you quickly grab the nearest torch and begin slinking backwards into the darkness.")
else:
    print("YOU WHAT!? you want to " + third_action + " now!? like right now? I mean yeah the narator litterally just told you the best option right now would be to sneak away")
    print("but what does he know? I mean its not like hes the one telling the story or anything. NO NO dont let me stop you go ahead do what you want.")
    input("")
    print("you die game over")
    print()
    print()
    print()
    print("ok I lied your not dead....")
    print("but you could have been! Just do me a favor from here on out. if your good ol pal....uh...Creig - thats me just so you know - comes to ou with advice just take it ok cause trust me I know what im talking about. ")
    print("so where were we oh yeah")
print("wow that sure was a close one with that snake-thing....guy? back there. I mean if it wasnt for your bravery")
print("and magnificent " + phys_adj + "our story might have ended back there but it didnt so")
print(" as we walk around the dark and grimey floor of what i can only assume i probably a room, or dungeon, or cave or- nevermind you get the point- ")
print("you feel your foot brush across some sort of object on the ground")
weapon_type = (input( "this object on the ground what could it be hmmmmmm? hmmmmm? what so ever is this thing you found hint hint- no seriously I left my glasses at home what is it? "))
print("you pick up the item on the floor to examine it.")
print("to your suprise you recognize it as the great " + weapon_type + " of legend. you decide that you will brannish this new found. ")
weapon_name = input(weapon_type + "as a weapon but all great weapons have a name. What will you name it? ")
print(weapon_name + "? oh why thats a fantastic name! They will sing stories about the mighty hero ")
if falsenameexist == True:
    print(falsename + "and ")
else:
    if gender == "male":
        print("his famed weapon " + weapon_name + " for years to come.")
    elif gender == "female":
        print("her famed weapon " + weapon_name + " for years to come.")
    elif title == "thing":
        print("its famed weapon " + weapon_name + " for years to come.")

print("ok so now you have your fancy " + weapon_type + " but what use is having some sort of awesome weapon, espicially one with a name as cool as " + weapon_name + "if you dont use it?")
print("what kind of story would this be if there wasnt excitment! danger! mystery?! and even maybe......")
print("MURDER WHAHAHAHAHAHHAHHAHAHHAHAHAH")
print("all of the sudden a hole opens up in the ground where you were once standing and you find yourself")
print("plumeting twords what like an endlessy void.")
print("everywhere you look it seems dark. so dark you cant even see your own body.")
print("were it mot for the fact that you can feel the air rushing past your face you wouldnt event know that your falling.")
print("suddenly it stops.....")
   
while True:
    stndrdprmt()
    if chk_last_in():
        check_constant()                                
