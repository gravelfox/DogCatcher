import time
import msvcrt
import os
import random
gameCharacters = ("D","&","O","G","$","v","@","T")
gameProgress = ""
gameInstruct = 'Catch that Dog! Use Space Bar to Stop the Letters and Spell "DOG"'


def gameOver():
    playAgain = raw_input('Would you like to play again? Yes or No:').lower()
    if playAgain == 'yes' or playAgain == 'y':
        gameProgress = ""
        selectBreed()
    elif playAgain == 'no' or playAgain == 'n':
        print("Have a great day!")
        time.sleep(2)
        exit()
    else:
        print("Please enter a Yes or a No.")
        time.sleep(2)
        gameOver()
        

def runningDog():
    while 1:
        os.system('cls')
        randomLetter = gameCharacters[random.randint(0,7)]
        print(gameProgress + randomLetter)
        time.sleep(1.0/speed)
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) == 32:
                return randomLetter
                break
    
def runGame():
    global gameProgress
    global breedSelect
    print(gameInstruct)
    for count in range(5, 0, -1):
        print(count)
        time.sleep(1)
    gameProgress = runningDog()            
    if gameProgress == "D":
        gameProgress = gameProgress + runningDog()
        if gameProgress == "DO":
            gameProgress = gameProgress + runningDog()
            if gameProgress == "DOG":
                print("You are Victorious!")
                if breedSelect == 1:
                    print("You caught a Pug. Not that impressive, but you're victorious none the less.")
                elif breedSelect == 2:
                    print("You caught a Terrier. They're not too quick, but they're wiley. Nice Job.")
                elif breedSelect == 3:
                    print("You caught a Shepherd. They can be speedy, and there's a little tooth there. Good work.")
                elif breedSelect == 4:
                    print("You caught a Greyhound. You lured it with a rabbit corpse, didn't you?")
                elif breedSelect == 5:
                    print("You caught a Dire Wolf. I'm not sure how you did that without getting eaten, but you have done the most difficult thing possible. Congratulations.")
                time.sleep(3)
            else:
                print('The dog got away!')
                time.sleep(3)
        else:
            print('The dog got away!')
            time.sleep(3)
    else:
        print('The dog got away!')
        time.sleep(3)
    gameProgress = ""
    gameOver()

def selectBreed():
    global speed
    global breedSelect
    speed = 0.0
    print("Select the breed you'd like to catch:")
    print("1. Pug")
    print("2. Terrier")
    print("3. Shepherd")
    print("4. Greyhound")
    print("5. Dire Wolf")
    breedSelect = int(raw_input("Enter the number: "))
    if breedSelect == 1 or breedSelect == 2 or breedSelect == 3 or breedSelect == 4 or breedSelect == 5:
        speed = 1.6 + (breedSelect * 0.2)
        runGame()
    else:
        print("Please select a choice 1 though 5.")
    selectBreed()
    
selectBreed()
