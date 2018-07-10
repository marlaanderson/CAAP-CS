#Converts years into seconds
def seconds_alive ():
    YearsAlive = input ("This program converts your age to seconds, and tells you the minimum amount of seconds you have been alive. This is not accurate to the exact second, but is simply an estimation. How old are you?")
    SecondsAlive = (YearsAlive) * (31449600/2*2)
    print ("Wow, congratulations! You've succesfully been alive for at least %s seconds!" %(SecondsAlive))
seconds_alive ()