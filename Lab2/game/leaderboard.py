# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 5 #raise ValueError ('todo')
	board = [] #raise ValueError ('todo')

	def __init__(self):
		for rank in range(self.size):
			self.board.append({"place":rank, "name":"", "score":0})



	# prints the leaderboard
	def print_board(self):
		for dictionary in self.board:
			print ("%s, %s, %s" %(dictionary["place"], dictionary["name"], dictionary["score"]))


	# checks if given score should be in the leaderboard
	def update(self, score):
		for dictionary in self.board:
			if dictionary["score"]> Score.get_score():
				self.insert(score, dictionary["place"])



	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	def insert(self, score, i):
		return 1 #raise ValueError ('todo')