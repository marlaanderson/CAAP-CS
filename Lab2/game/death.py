# importing random int maker module
from random import randint

# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
	quips = ["It's not even that difficult.",
			"Bro you're telling me you landed a top 3 university but can't get top 3 in a videogame?",
			"Lol. Here's your L",
			"My grandma plays games better than you.",
			"Come again soon."
			# raise ValueError ('todo')
			]
	def enter(self):
		print (Death.quips[randint(0, len(self.quips)- 1)])
		return 'died'