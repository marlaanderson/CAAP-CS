# Converts years into seconds
def seconds_alive ():
    SecondsPerMinute = 60
    MinutesPerHour = 60
    HoursPerDay = 24
    DaysPerWeek = 7
    WeeksPerYear = 52
    YearsAlive = int(input("This program converts your age to seconds, and tells you the minimum amount of seconds you have been alive. This is not accurate to the exact second, but is simply an estimation. How old are you?"))
    SecondsAlive = SecondsPerMinute*MinutesPerHour*HoursPerDay*DaysPerWeek*WeeksPerYear*YearsAlive
    print ("Wow, congratulations! You've succesfully been alive for at least %s seconds!" %(SecondsAlive))
seconds_alive ()