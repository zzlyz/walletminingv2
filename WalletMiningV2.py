from asyncio import selector_events
import random
import sys
import os
from time import sleep
from os import system
import colorama

# use colorama to make a red colour
colorama.init()
# make red 
red = colorama.Fore.RED
yeller = colorama.Fore.RED
valid = colorama.Fore.GREEN
reset = colorama.Fore.LIGHTRED_EX

def typingFast(text):
    for char in text:
        sleep(0.000005)
        sys.stdout.write(char)
        sys.stdout.flush()

def nextLine():
    # make a new line using end
    print("", end="\n")

cwd = str(os.getcwd())

print(yeller + '''
 .oooooo..o ooooo   ooooo   .oooooo.   ooooooooooooo  .oooooo..o 
d8P'    `Y8 `888'   `888'  d8P'  `Y8b  8'   888   `8 d8P'    `Y8 
Y88bo.       888     888  888      888      888      Y88bo.      
 `"Y8888o.   888ooooo888  888      888      888       `"Y8888o.   ''' + cwd + '''
     `"Y88b  888     888  888      888      888           `"Y88b 
oo     .d8P  888     888  `88b    d88'      888      oo     .d8P 
8""88888P'  o888o   o888o  `Y8bood8P'      o888o     8""88888P'  
''')
os.system('title SHOTS- Loading...')
# pause for 1 second
name = (os.getlogin())
sleep(0.75)
nextLine()
typingFast('Welcome ' + name + ' to the SHOTS - Digital Currency Mining Program')
nextLine()
os.system('title SHOTS - Waiting for input...')
typingFast(yeller + 'Press any key to continue')
input()
# allow input to be anything and then start the program
os.system('cls')
print(yeller + '''
 .oooooo..o ooooo   ooooo   .oooooo.   ooooooooooooo  .oooooo..o 
d8P'    `Y8 `888'   `888'  d8P'  `Y8b  8'   888   `8 d8P'    `Y8 
Y88bo.       888     888  888      888      888      Y88bo.      
 `"Y8888o.   888ooooo888  888      888      888       `"Y8888o.   STARTING
     `"Y88b  888     888  888      888      888           `"Y88b 
oo     .d8P  888     888  `88b    d88'      888      oo     .d8P 
8""88888P'  o888o   o888o  `Y8bood8P'      o888o     8""88888P'                                   
''')
# pause for 1 second
sleep(0.75)
os.system('title Mining...')

# because chance is below 2 then pick a number between 0.0 and 5.9 and pick a number between it and save it to be used later
while True:
    chance = random.uniform(0, 500)
    # if the chance is less than 259
    if chance < 499999:
        chance = 0.0
        os.system('title INVALID BTC')
        # make the letters randomised and change everytime they are generated
        letters = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(random.randint(70, 71)))
        # print a message that uses a new random integer
        print(yeller + '[-] ' + reset + str(letters) + red +' (' + str(chance) + ') BTC ')
        # pause for 1 second
        sleep(0.025)
    # if the chance is below 1
    elif chance > 499999:
        chance = random.uniform(0.0001, 5.99)
        # make the letters randomised and change everytime they are generated
        letters = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(random.randint(70, 71)))
        typeLetters = (yeller + '[+] ' + reset + str(letters) + valid +' (' + str(chance) + ') BTC ')
        # print a message that uses a new random integer
        typingFast(typeLetters)
        nextLine()
        # wait for input before continuing
        # print a line to seperate the messages
        os.system('title VALID BTC')
        typingFast(yeller + 'You just mined some BITCOIN!')
        nextLine()
        input('Press ENTER to continue...')
        print(yeller + '\n')
        
        
