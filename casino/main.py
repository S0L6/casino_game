# main.py 
import random
import time
import os
from room import Room


# ------ INITIALISE ROOMS ----- #
# ------ LOBBY ------ #
lobbydescription = "The main lobby of the Casino big marble pillars surround you with High cielings and a central chandelier."

lobbyse = Room("Lobby South East")
lobbyse = lobbydescription

lobbys = Room("Lobby South")
lobbys.description = lobbydescription

lobbysw = Room("Lobby South West")
lobbysw.description = lobbydescription

lobbynw = Room('Lobby North West')
lobbynw.description = lobbydescription

lobbyn = Room("Lobby North")
lobbyn = lobbydescription

lobbyne = Room("Lobby North East")
lobbyne.description = lobbydescription

# ------ Bathrooms ------ #
# ---- MENS BATHROOM ---- #
mensbathroom = Room("The Mens Bathroom")
mensbathroom.description = "The bathroom is filthy with a mysterious odour that makes you want to chunder. A questionable brown mark resides on the wall."

mstall1 = Room("Mens Stall 1")
mstall1.description = "An unflushed toilet with a humungeos turd in the center."

mstall2 = Room("Mens Stall 2")
mstall2.description = "Grafitti lines the walls with crude sayings."

mstall3 = Room("Mens Stall 3")
mstall3.description = "There is a hole in the ground where the toilet should be. All you can see down the hole is darkness."

mstall4 = Room("Mens Stall 4")
mstall4.description = "The toilet walls are smeared with feces."

mstall5 = Room("Mens Stall 5")
mstall5.description = "A mysterious liquid lines the floor. Better have shoes on."

mstall6 = Room("Mens Urinal")
mstall6.description = "A urinal cake sits peacefully in the silver tray with a bite mark in it."

# ---- WOMENS BATHROOM ---- #
womensbathroom = Room("The Womens Bathroom")
womensbathroom.description = "The room is pristine with 3 lit candles producing a pleasant smell. No marks in sight."

wstall1 = Room("Womens Stall 1")
wstall1.description = "Not a speck of dust in sight, no marks or stains either!"

wstall2 = Room("Womens Stall 2")
wstall2.description = "A sanitary bin lies in the corner."

wstall3 = Room("Womens Stall 3")
wstall3.description = "Everything is perfect except there is a floor tile missing?!?"

wstall4 = Room("Womens Stall 4")
wstall4.description = "Suprisingly this stall has some graffiti in it."

wstall5 = Room("Womens Stall 5")
wstall5.description = "There is a shelf with a candle bringing pleasant odurs to your nose."

wstall6 = Room("Womens Stall 6")
wstall6.description = "There is a handbag sitting in the corner. Someone must've left it here."

# ------ BAR ------ #
chip = Room("Chip Collection")
chip.description = "A marble floor surrounds you. A counter sits in the corner with a sign saying CHIPS."

bar = Room("Bar")
bar.description = "A marble floor surrounds you. A bar with hundreds of different drinks line the walls."

# ------ BASIC AREA ------ #

# ------ LINKING ROOMS ------ #
lobbys.link_rooms(lobbyn, "North")


# ------ INITIALISE VARIABLES ------ #
current_room = lobbys
running = True
backpack = []

####### MAIN LOOP #######
while running:
    current_room.describe()
    
    