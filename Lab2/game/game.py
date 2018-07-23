# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ""
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves
	score = Score(name, moves)
	if won:
		leaderboard.update(score)
	print ("\nGame Over.")
	leaderboard.print_board()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name 
		global moves 
		print ("Welcome to \n                      .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.                     \n                     | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |                    \n                     | | ____    ____ | || | _____  _____ | || |  _________   | || |      __      | || | ____  _____  | || |  _________   | |                    \n                     | ||_   \  /   _|| || ||_   _||_   _|| || | |  _   _  |  | || |     /  \     | || ||_   \|_   _| | || | |  _   _  |  | |                    \n                     | |  |   \/   |  | || |  | |    | |  | || | |_/ | | \_|  | || |    / /\ \    | || |  |   \ | |   | || | |_/ | | \_|  | |                    \n                     | |  | |\  /| |  | || |  | '    ' |  | || |     | |      | || |   / ____ \   | || |  | |\ \| |   | || |     | |      | |                    \n                     | | _| |_\/_| |_ | || |   \ `--' /   | || |    _| |_     | || | _/ /    \ \_ | || | _| |_\   |_  | || |    _| |_     | |                    \n                     | ||_____||_____|| || |    `.__.'    | || |   |_____|    | || ||____|  |____|| || ||_____|\____| | || |   |_____|    | |                    \n                     | |              | || |              | || |              | || |              | || |              | || |              | |                    \n                     | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |                    \n                      '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'                     \n  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.\n | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |\n | |  _________   | || |     ____     | || |  ________    | || |  ________    | || |   _____      | || |  _________   | || |  _______     | || |    _______   | |\n | | |  _   _  |  | || |   .'    `.   | || | |_   ___ `.  | || | |_   ___ `.  | || |  |_   _|     | || | |_   ___  |  | || | |_   __ \    | || |   /  ___  |  | |\n | | |_/ | | \_|  | || |  /  .--.  \  | || |   | |   `. \ | || |   | |   `. \ | || |    | |       | || |   | |_  \_|  | || |   | |__) |   | || |  |  (__ \_|  | |\n | |     | |      | || |  | |    | |  | || |   | |    | | | || |   | |    | | | || |    | |   _   | || |   |  _|  _   | || |   |  __ /    | || |   '.___`-.   | |\n | |    _| |_     | || |  \  `--'  /  | || |  _| |___.' / | || |  _| |___.' / | || |   _| |__/ |  | || |  _| |___/ |  | || |  _| |  \ \_  | || |  |`\____) |  | |\n | |   |_____|    | || |   `.____.'   | || | |________.'  | || | |________.'  | || |  |________|  | || | |_________|  | || | |____| |___| | || |  |_______.'  | |\n | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |\n | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |\n  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' \n To quit enter :q at any time. Good luck!") # raise ValueError ('')
		name = input("\nLet's play. Enter your name. > ") # raise ValueError ('todo')
		if (name == ':q'):
			exit(1)
		difficulty_level= ""
		while True:
			difficulty_level = str(input("Choose a difficulty level: easy, medium, or hard: "))
			if difficulty_level == "easy" or difficulty_level == "medium" or difficulty_level == "hard":
				break
			else:
				print ("Error. Please choose 'easy', 'medium', or 'hard'.")
		a_map = Map('center_alley') 
		a_game = Engine(a_map, difficulty_level)
		moves = a_game.play()
		game_over(a_game.won())

play_game()
