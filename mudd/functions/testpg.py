from random import randrange

def print_hello_world(name = "fghjkl"):    
    print("hello world I am {}".format(name))
    othername = input("name?")
    print_hello_world(othername)

def print_math(number = 2):
    print(number * number)
    number = int(input("give me a number"))
    print_math(number)




MAX_STATS_STARTING = 15
MIN_STATS_STARTING = 5

def roll_stats():
    print(randrange(MAX_STATS_STARTING,MIN_STATS_STARTING))

