#Made By Nanotixx/Hanprince
#Note From Nano: If you don't type anything inside the input command, it will proceed without caution so pick 1 or 2!

import random
import colorama
from colorama import init, Fore, Back, Style
import time

Boss = 100
Player = 100
print("Welcome To TurnBased Game By Nanotixx! | Version: 1.0 Alpha")

while True:
    print("\n[HP: " + Fore.GREEN + str(Player) + Fore.WHITE + "]" + "   [Boss HP: " + Fore.RED + str(Boss) + Fore.WHITE + "]")
    
    In = input("Attack - 1 Heal - 2: ")
    
    if In == "1":
        Dice = random.randint(1, 30)
        Boss = Boss - Dice
        print("\nYou Damaged The Boss By " + Fore.BLUE + str(Dice) + Fore.WHITE + " The Boss Health Is Now " + Fore.RED +str(Boss) + Fore.WHITE +"\n")
        if Dice > 20:
            print(Fore.GREEN + "A Critical Hit!" + Fore.WHITE)
        if Boss < 0 or Boss == 0:
            break
            
    if In == "2":
        Player = Player + 20
        print("You Healed, Your Health Is Now " + Fore.GREEN + str(Player) + Fore.WHITE)
    
    for Ba in range(3, 0, -1):
        print("\n" + str(Ba) + "...\n")
        time.sleep(0.8)
        Dice2 = random.randint(1, 30)
      
        if Ba == 1:
            Player = Player - Dice2
            print("The Boss Damaged You By " + Fore.BLUE + str(Dice2) + Fore.WHITE + " Your Health Is Now " + Fore.GREEN + str(Player) +Fore.WHITE)
            if Dice2 > 20:
                print(Fore.RED + "A Critical Hit!" + Fore.WHITE)
            
        if Player < 0 or Player == 0:
            exit()