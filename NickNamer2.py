"""
Created on Sun Mar  7 10:19:40 2021

@author: Jared
"""

import random
import time
nick = "Nick-namer"

def playfunc(n):
    if n[0].lower() == "y" or n.lower() == "sure" or n[0:2].lower() == "ok" or n == "k":
        return True
    else:
        return False

def name_generator(name):
    xlist = [name+"-asaurus Rex!",
    name+"-ceratops!",
    name+"y "+name+"aroo!",
    "Big "+name+" the "+"Z"+name[1:len(name)]+"!",
    name+" "+name+"Bo B"+name[1:len(name)],
    name+"ster!",
    "The Incredible "+name+"!",
    name+"y"+name+"y "+name[0]+"oo"+name[0]+"oo",
    "Ba Ba Baa, Ba Ba Ba "+name,
    "The Mighty "+name+"!",
    name+"ster bad"+name[1:len(name)]+"ster!",
    name+" "+name+"bad"+name[1:len(name)]+"aroo!",
    name+" "+name+"enny Cheroo!!!!!",
    name[0]+"illicky"+name[0]+"ellicky"+name+"y Jellicky",
    "Bonk Bonk "+name+" Clonk-a-donk",
    "Z"+name[1:len(name)]+" Ba-D"+name[1:len(name)]+"N"+name[1:len(name)]+"etty Kl"+name[1:len(name)],
    "The great and mysterious "+name+"-steeeerio!"] 
    x = random.randint(0, len(xlist)-1)
    for i in xlist:
        yield xlist[x]

def nn_generator(nnname):
    ylist = [nnname+"! Well, that's a new one!",
    "My name is Nick-namer, but you can call me "+nnname+"!",
    "Hello, my name is "+nnname+".",
    "I am the great and powerful "+nnname+"!",
    "<In Iron Man voice:> I am "+nnname+"man!"]
    y = random.randint(0, len(ylist)-1)
    for i in ylist:
        yield ylist[y]

while True:
    play = ""
    namenamer = ""
    name = ""
    nnname =""
    contin = ""
    print("Hello, I am "+nick+"...")    
    while play == "":
        play = input("Would you like me to give you a nickname?")
    
    if playfunc(play): 
        print(".")
        time.sleep(1)
        print("Great! Here we go...")
        while name == "":
            name = input("What is your name?")
    else:
        print(".\n"+play+"?\n.\nOkay... We could do something else...")
        time.sleep(1)
        print(".")
        time.sleep(1)
        while namenamer == "": 
            namenamer = input("Do you want to give ME a nickname?")
    
    if name != "":
        print(".\n.\n.\nHi "+name+",")
        time.sleep(1)
        print(".\n.")
        time.sleep(1)
        print(".\nI am going to call you...")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        name = next(name_generator(name))
        print(name)
        time.sleep(1)
        print(".")
    
    while namenamer != "":
        if playfunc(namenamer): 
            print(".")
            time.sleep(1)
            print("Okay, I can't wait to hear it...")
            while nnname == "": 
                nnname = input("What is your nickname for me?")
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".\n"+next(nn_generator(nnname)))
            nick = nnname
            namenamer = ""
        else: 
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("Okay... See you next time!!!!")
            break
        
    while contin == "":
        contin = input("Would you like to play again?")
    if playfunc(contin): 
        print(".")
        time.sleep(1)
        print(".\nGreat! Let's start again!") 
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
    else: 
        print("Okay... See you next time "+name+"!!!!")
        break
