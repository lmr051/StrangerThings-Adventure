# desc:
# a text adventure game with 4 endings, 3 of them end with either you, your friends, or all of you getting killed and eaten by a monster
# context: you don't know the monster is out there, 
# therefore you don't know its weaknesses and strengths, 
# therefore you and your friends are 100000% unprepared and that's why it catches you off guard and eats you

# version: PyCharm 2022.3.1 (Community Edition)
# Build #PC-223.8214.51, built on December 20, 2022
# Runtime version: 17.0.5+1-b653.23 amd64
# VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
# Windows 11 10.0
# GC: G1 Young Generation, G1 Old Generation
# Memory: 2010M
# Cores: 8
# Non-Bundled Plugins:
#     com.yemreak.DarkCode-Theme (1.1)
#     com.elliotwaite.godot_theme (1.0.12)

import random
import time
import winsound
from playsound import playsound


def intro():
    direction = ["left", "right"]
    print("You're at the end of the neighborhood street. Which way do you want to go?")
    print("Type: 'left' or 'right'")
    user = input()
    while user not in direction:
        print("You can go left or right.")
    if user == "left":
        winsound.Beep(1200, 500)
        showTrainStation()
    if user == "right":
        winsound.Beep(400, 500)
        showStore()


def showTrainStation():
    print("You're at the train station! You rest for a bit.")
    f = open("..scenes\\trainStation.txt", "r")
    print(f.read())
    trainDecision()


def trainDecision():
    print("Do you want to go on the train?")
    print("Type: 'yes' or 'no'")
    user = input()
    if user == "yes":
        print("You and your friends hop onto the train.")
        winsound.Beep(200, 300)
        trainRide()
    if user == "no":
        print("You and your friends bike towards the creek.")
        winsound.Beep(500, 800)
        showLake()


def showLake():
    print("You and your friends reached the creek.")
    f = open("..scenes\\lake.txt", "r")
    print(f.read())
    lakeDecision()


def lakeDecision():
    print("You hear something coming from the water. But you aren't sure.")
    time.sleep(1.4)
    print("Do you investigate or stand by?")
    print("Type: 'investigate' or 'stand'")
    user = input()
    if user == "investigate":
        winsound.Beep(100, 1000)
        print("You walk towards the edge of the creek.")
        print("You hear something from the water.")
        print("..........")
        time.sleep(2.3)
        print("...............")
        time.sleep(1.4)
        print("..?")
        time.sleep(1.3)
        print("!!!")
        print("Something jumps out!")
        playsound("demoMon2.mp3")
        f = open("..endings\\end4.txt", encoding="utf8")
        print(f.read())
    if user == "stand":
        winsound.Beep(400, 900)
        print("You stand by. But your friends decide to walk towards the edge of the creek.")
        print("You hear something coming out of the water but it's too late.")
        playsound("demoMon2.mp3")
        f = open("..endings\\end3.txt", encoding="utf8")
        print(f.read())


def trainRide():
    print("...")
    print("The train is empty except for some boxes..")
    time.sleep(1.2)
    print("After a long train ride, it stops at the edge of town. It's dark out.")
    print("You hear some rustling in the corner of the train. Do you investigate with your friends? Or get off the train?")
    print("... Type: 'investigate' or 'get off train'")
    user = input()
    if user == "investigate":
        winsound.Beep(200, 700)
        print("You and your friends decide to investigate the sound..")
        time.sleep(2.3)
        playsound("demoMon2.mp3")
        f = open("..endings\\end1.txt", encoding="utf8")
        print(f.read())
    if user == "get off train":
        winsound.Beep(600, 1000)
        print("You and your friends decide to get off the train.")
        time.sleep(1.3)
        print("You bike until you reach the end of the tracks at a road.")
        trainTracks()


def trainTracks():
    print("Do you want to go home? Or go to the store?")
    print("Type: 'home' or 'continue'")
    user = input()
    if user == "home":
        winsound.Beep(900, 1100)
        f = open("..endings\\end2.txt", encoding="utf8")
        print(f.read())
    if user == "continue":
        winsound.Beep(300, 600)
        showStore()


def showStore():
    print("You're at the store! You rest for a bit.")
    f = open("..scenes\\store.txt", "r")
    print(f.read())
    storeDecision()


def storeDecision():
    print("Do you get snacks or simply look around?")
    print("Type: 'snacks' or 'look'")
    user = input()
    if user == "snacks":
        winsound.Beep(200, 700)
        storeSnacks()
    if user == "look":
        winsound.Beep(600, 900)
        print("You look around for a bit and decide to sit on the counter at the front.")
        print("You get bored sitting around and wander around the store.")
        storeLook()


def storeSnacks():
    print("You pick up your favorite snacks.")
    print("You walk towards the back near the freezers near the drinks. You hear a sound from one of the freezers.")
    print("Do you investigate or ignore and walk away?")
    print("Type: 'investigate' or 'ignore'")
    user = input()
    if user == "investigate":
        winsound.Beep(400, 800)
        print("You investigate the sound..")
        storeInvestigateFreezer()
    if user == "ignore":
        winsound.Beep(300, 900)
        print("You walk away from the freezers. But you have a weird feeling about the sound.")
        print("Do you get your friends to come with you to the front?")
        storeIgnoreFreezer()


def storeIgnoreFreezer():
    print("Type: 'yes' or 'no'")
    user = input()
    if user == "yes":
        winsound.Beep(600, 400)
        f = open("..endings\\end2.txt", encoding="utf8")
        print(f.read())
        print("You and your friends decide to leave the store.")
    if user == "no":
        winsound.Beep(200, 700)
        print("You decide that you're just hearing things. You walk to the front.")
        playsound("demoMon2.mp3")
        f = open("..endings\\end3.txt", encoding="utf8")
        print(f.read())


def storeInvestigateFreezer():
    print("You investigated the sound coming from the freezer.")
    print("Something jumps out!!")
    playsound("demoMon2.mp3")
    f = open("..endings\\end1.txt", encoding="utf8")
    print(f.read())


def storeLook():
    print("You hear something creeping up behind you..")
    playsound("demoMon2.mp3")
    randomEnding()


def randomEnding():
    x = random.randint(1, 2)
    if x == 1:
        badEnding()
    else:
        goodEnding()


def badEnding():
    f = open("..endings\\end4.txt", encoding="utf8")
    print(f.read())


def goodEnding():
    print("You reacted in time and found a bat to hit the monster!")
    print("It's stunned!! You run and take your friends with you to bike home!")
    f = open("..endings\\end2.txt", encoding="utf8")
    print(f.read())

if __name__ == "__main__":
    print("You're with your group of friends and you plan to take a bike ride throughout town.")
    print("What is your name? Enter here: ")
    name = input()
    print("You're ready for your bike ride " + name + "!")
    intro()
