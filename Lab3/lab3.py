# MARLA ANDERSON
# LAB 3

from random import randint

# global variable of chutes and ladders
# remenber to let your function know you're using this variable with 'global'
chutes_ladders = {4 : 7,
					8 : 15,
					12 : 2,
					14: 6}

chutes = {12 : 2, 14 : 6}
ladders = {4 : 7, 8 : 15}


# Rolls a die of six sides and returns the result
def roll_die():
	roll = randint(1,6)
	print (roll)
roll_die()

# makes a game (just a list) of the given dimensions
def makeGame(w, l):
	list= range(1,(w*l)+1)
	#This also works.
	#for i in range(1,(w*1)+1):
	#	list.append(i)
	return list

# checks if given square is a chutes or ladders
def is_chutes_ladders(d):
	if d in chutes:
		print("Chute") 
	elif d in ladders:
		print("Ladder")
	else:
		print ("False")

is_chutes_ladders(14)
"""
# function to make and play a game
def play_game():
	state = #This should be a list of dictionaries of each player's state
	mode = 'pc' # or 'user'
	raise ValueError("todo")

# Runs the game as a simulation and keeps track of the number of moves it takes to win and returns average
def simulate_game():

"""