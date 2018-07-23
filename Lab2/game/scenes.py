# imports random madule form library
from random import randint

# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class CenterAlley(Scene):
	
	name = 'center_alley'

	def enter(self):
		print ("It's the year 3005. Mutant toddlers have taken over the world, but you have heard of a safe haven to escape to in \ndowntown Chicago: The John Hancock Center.")
		return self.action()
		
		
	def action(self):
		print ("What will you do?")
		choice = input("\n1. Throw your bag at it and run. \n2. Try to hide yourself among the trash. \n3. Confront it. \nChoice:")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You rip your bag off your back and launch it at the mutant toddler. It swiftly reaches up and snatches your bag straight out of thin air, then speed toddles at you, and beats you to death with your own bag.")
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Luckily, you were taught to play smart, not hard. You ruffle through the garbage, cardboard, and debris on the ground, \ntucking yourself beneath it. Then you try to stay as quiet as possible as the mutant toddler searches around. You lay \nthere for what seems like 20 minutes, you feel something touch your foot, and it seems like you're done for but then \nyou hear it walk off in the opposite direciton. After laying there another few minutes, you uncover yourself and walk\n out of the alley.")
			return self.exit_scene('center_street') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("You move from behind the trash can then sprint towards it and launch a punch at its innocent looking face. Your fist connects, but it feels like solid rock. You fall to the ground, and wince from the pain of contact. As you recollect yourself, it stares you down, before kicking you square in the face. You die.")
			return self.exit_scene('death') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class CenterStreet(Scene):
	
	name = 'center_street'

	def enter(self):
		print ("You exit the mouth of the alley and look up. The Center, with two gleaming spires of hope are in your view. So close.")
		print ("You make it to the front doors of the Center. There's a lock on the door with a keypad. That's when you remember: you \nwere told the password when you heard about this place and put it on a piece of paper in your bag. You open it and \nsearch around furiously. Where is it? You can't find the code.")
		return self.action()

	def action(self):
		print ("You look at the key pad and think to yourself, 'I suppose I have to guess.' You remember it wa sthree digits.")
		# raise ValueError ('todo')
		code = [randint(0,9), randint(0,9), randint(0,9)]
		guesses = 0
		# loop to check three random integers, one at a time
		for i in range(3):
			print ("Enter digit %d." % (i+1))
			guess = input("[keypad]> ")
			if guess == ':q':
				return self.exit_scene(guess)
			try:
			   guess = int(guess)
			except ValueError:
			   print("That's not an int!")
			   return self.exit_scene(self.name)
			while int(guess) != code[i] and guesses <10:
				print ("BZZZZEDDD!")
				guesses += 1
				guess =input("[keypad]> ")
				if guess == ':q':
					return self.exit_scene(guess)
				try:
				   guess = int(guess)
				except ValueError:
				   print("That's not an int!")
				   guess = -1
		
		if guesses < 10:
			print ("The light flashes green and the door clicks open. You reach for the handle and open the door.")
			# raise ValueError ('todo')
			return self.exit_scene('the_bridge')
		else:
			print ("The lock buzzes one last time and causes an electric shock through your entire body, killing you instantly.")
			#raise ValueError ('todo')
			return self.exit_scene('death') # raise ValueError ('todo')

	def exit_scene(self, outcome):
		return outcome
			
class TheCenter(Scene):
	
	name ='the_center'

	def enter(self):
		print ("You enter the front lobby of the Center. It is eerily quiet. You think to yourself why is no one here guarding the door? You walk forward towards the elevator and stop. The hairs on your arms start to raise and you wonder how good of an idea this was. You walk into the elevator and turn to face the buttons. All the buttons are marked out except for the one that goes to the SkyDeck.")#raise ValueError ('todo')
		return self.action()
	
	def action(self):
		
		choice= input("What will you do? 1. Click the button that leads to the SkyDeck. 2. Leave the Center.")
		if choice == ':q':
			return self.exit_scene(choice)
		if int(choice) == 1:
			print ("You click the button that goes to the Skydeck. The elevator door closes, and elevator music starts.") 
			return self.exit_scene('finished') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("You decide that this just doesn't feel right. So you walk back out of the center and bac the way you came. Immediately, a mutant toddler jumps out from an alley, and thats when you realize you made a bad decision. It runs towards you and you feel the gut wrenching pain as the lights go dim.")
			return self.exit_scene('death') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		#raise ValueError ('todo')
		return outcome