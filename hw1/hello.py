# Prints "Hello!" to screen.
def hello_world ():
    print ("Hello!")
    name = input ("What's your name?")
    color = input ("Nice to meet you, %s. We should get to know each other! What's your favorite color?" %(name))
    ice_cream = input ("I can respect that. What about your favorite ice cream?")
    place_on_earth = input ("Mmm. Tasty! Guess what? I've been thinking about going on a trip some time this month. Where's your favorite place on earth?")
    artist = input ("Interestinggggg. One last question. This one's the dealbreaker. Who is your favorite artist?")
    print ("Ah! You're so cool, %s! I've gotta say, we have a lot in common! I love %s and %s ice cream too! I also love your suggestion and I think I just might take that trip to %s! But, honestly, I think you could've done a little better than %s for your favorite artist. There are just so many better options out there to choose from." %(name,color,ice_cream,place_on_earth,artist))
hello_world ()