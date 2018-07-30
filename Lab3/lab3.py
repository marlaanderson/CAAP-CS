# MARLA ANDERSON
# LAB 3
# got some help from Juan Pablo

from random import randint

# global variable of chutes and ladders
# remenber to let your function know you're using this variable with 'global'
chutes_ladders = {4 : 7,
					8 : 15,
					12 : 2,
					14: 6}

# Rolls a die of six sides and returns the result
def roll_die():
	roll = randint(1,6)
	return roll

# makes a game (just a list) of the given dimensions
def makeGame(w, l):
	list= range(1,(w*l)+1)
	#This also works.
	#for i in range(1,(w*1)+1):
	#	list.append(i)
	return list

# checks if given square is a chutes or ladders
def is_chutes_ladders(d):
	global chutes_ladders
	if d in chutes_ladders:
		return True
	else:
		return False

# function to make and play a game
def play_game(w,l,mode):
	global chutes_ladders
	#i was using this but its uneccesary for my code
	mode = int(input("Who's playing? 1:pc or 2:user? "))
	won = 0
	if mode == 2:
		game = makeGame(w,l)
		players = int(input("How many players?"))
		state = []
		for i in range(players):
			player= input("What is player's %s name?" %(i+1))
			state.append({'player': player, 'state': 1,'moves': 0})
		#This should be a list of dictionaries of each player's state
		while won == 0:
			for i in range(players):
				state[i]["moves"]+=1
				input("%s, Press ENTER to roll the die."%(state[i]["player"]))
				roll = roll_die()
				print ("%s, you rolled a %s."%(state[i]["player"],roll))
				#for debugging purposes
				#print(state[i]['state'])
				placement = state[i]['state']+roll
				#for debugging purposes
				#print (placement) 
				# this is checking before you add the roll to the position
				if is_chutes_ladders(placement):
					state[i]['state'] = chutes_ladders[placement]
					print ("%s, you are now in square %s." %(state[i]["player"],state[i]['state']))
				else:
					state[i]['state'] = placement
					print ("%s, you are now in square %s." %(state[i]["player"],placement))
				if (state[i]['state'] >= len(game)):
					won = 1
					winner = state[i]["player"]
					break
		print("Congratulations, %s, you win. You took %s moves."%(winner,state[i]["moves"]))
	elif mode == 1:
		game = makeGame(w,l)
		players = int(input("How many players?"))
		state = []
		for i in range(players):
			state.append({'player': "", 'state': 1,'moves': 0})
		#This should be a list of dictionaries of each player's state
		won = 0
		while won == 0:
			for i in range(players):
				state[i]["moves"]+=1
				roll = roll_die()
				#for debugging purposes
				#print(state[i]['state'])
				placement = state[i]['state']+roll
				#for debugging purposes
				#print (placement) 
				# this is checking before you add the roll to the position
				if is_chutes_ladders(placement):
					state[i]['state'] = chutes_ladders[placement]
				else:
					state[i]['state'] = placement
				if (state[i]['state'] >= len(game)):
					won = 1
					break
		print("It took %s moves."%(state[i]["moves"]))
	else:
		print ("Please enter an integer: 1 or 2.")
play_game(4,4,2)

# Runs the game as a simulation and keeps track of the number of moves it takes to win and returns average
def simulate_game():
	play_game()
