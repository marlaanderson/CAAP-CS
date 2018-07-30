#1
def TimeAndHalf():
	hours = float(input ("Enter hours worked for the week: "))
	rate = float(input ("Enter hourly rate: "))
	if hours <= 40:
		totalwages = hours*rate
		print ("You have earned %s total this week" %(totalwages))
	else:
		if hours > 40:
			overtime = hours - 40
			totalwages = (40*rate) + (overtime*rate*1.5)
			print ("You have earned $%s total this week" %(totalwages))
#TimeAndHalf()

#2
def FivePointGrade ():
	score = int(input("Enter your score:"))
	if score == 5:
		print("A")
	if score == 4:
		print("B")
	if score == 3:
		print("C")
	if score == 2:
		print("D")
	if score == 1:
		print("F")
	if score <1:
		print("Incorrect input. Try again.")
	if score >5:
		print("Incorrect input. Try again.")
#FivePointGrade()

#3
def HundredPointGrade ():
	score = int(input("Enter your score:"))
	if score >=90:
		print("A")
	elif 80<= score <=89:
		print("B")
	elif 70<= score <=79:
		print("C")
	elif 60<= score <=69:
		print("D")
	elif score <60:
			print("F")
	else:
		print("Incorrect input. Try again.") 
#HundredPointGrade()

#4
def ClassStanding ():
	credits= int(input("Enter the amount of credits you have: "))
	if credits >= 26:
		print ("Senior")
	elif 16<= credits <=25:
		print("Junior")
	elif 7<= credits <=24:
		print("Sophomore")
	elif 0<= credits <=6:
		print ("Freshman")
	else:
		print("Incorrect input. Try again.") 
#ClassStanding()

#This is where I remembered I was supposed to do evens only

#6
def SpeedingTicketFine():
	SpeedingLimit = int(input("Enter speed limit: "))
	ClockedSpeed = int(input("Enter clocked speed: "))
	if ClockedSpeed > 90:
		if ClockedSpeed > SpeedingLimit:
			Fine = 250 + ((ClockedSpeed - SpeedingLimit)*5)
			print("Fine: $%s" %(Fine))
		else:
			print("Speed is legal")
	elif ClockedSpeed <= 90:
		if ClockedSpeed > SpeedingLimit:
			Fine = 50 + ((ClockedSpeed - SpeedingLimit)*5)
			print("Fine: $%s" %(Fine))
		else:
			print("Speed is legal.")
#SpeedingTicketFine()

#8
def Eligibility():
	age = int(input("Enter your age: "))
	years = int(input("Enter your years of citizenship: "))
	if age >= 30 and years >= 9:
		print("Eligible for Senate and House")
	elif age >= 25 and years >= 7:
		print("Eligible for House, but not Senate")
	else:
		print("Not eligible for House or Senate")
#Eligibility()

#10
def Easter():
	year = int(input("Enter the year: "))
	a = year%19
	b = year%4
	c = year%7
	d = ((19*a)+24)%30
	e = ((2*b)+(4*c)+(6*d)+5)%7
	exceptions = {"1984",
				"1981",
				"2049",
				"2079"}
	if year == exceptions:
		date = 22+d+e-24
		print("Easter in %s is on April %s." %(year, date))
	elif (22+d+e) > 31:
		date = 22+d+e-31
		print("Easter in %s is on April %s." %(year, date))
#Easter() I can't find what is wrong with this one and why it won't work for 2013.

#12
def Validity():
	days = {"January" : 31, "February" : 21, "March" : 31, "April" : 30,
			"May" : 31, "June" : 30, "July" : 31, "August" : 31, 
			"September" : 30, "October" : 31, "November" : 30, "December" : 31}
	date = input("Enter a date in month/day/year format: ")
	date2 = date.split("/")
	month = date2[1]
	day = date2 [2]
	if day <= month:
		print ("Valid.")
	else: 
		print ("Invalid.")
#Validity()

#14
#??

#16
#??