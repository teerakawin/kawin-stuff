import random
import os
import time

print("You see a door")
choice = input("Open it? (yes/no/confused): ")

if choice == "yes":
    print("There's nothing")
    choice2 = input("put something?(yes/no): ")

    if choice2 == "yes":
        print("wait you have nothing")
        print("bruh")
        print("THE END")
    elif choice2 == "no":
        print("ok i guess")
        print("you go away")
        print("THE END")
    else:
        print("bruh")

elif choice == "no":
    print("ok i guess")
    print("you go away")
    print("THE END")

elif choice == "confused":
    print("You stand there confused")
    print("THE END")

else:
    print("bruh")
    print("hmmmm")
    print("the coder of this is bored sooooo")
    print("you got sent to somewhere...")
    print("You walk forward...")

    time.sleep(1)
    event = random.randint(1, 5)

    if event == 3:
        print("You hear rumbling...")
        time.sleep(1)
        print("WAIT WHAT—")
        time.sleep(1)
        os.system("sl")
        print("bruh that train almost got me...")
        print("well theres just nothing now")
        print("i guess this is the end")
        print("cool")
    else:
        print("Nothing happened")
        print("oh yeah theres a rng in this try to get it :3")