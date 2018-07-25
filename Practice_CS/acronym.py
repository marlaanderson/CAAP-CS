def acronym ():
	str1 = input("What is your string?")
	str2 = str1.split("")
	firstlet = ""
	for i in str2:
		firstlet.append(i[0])
	print(firstlet.upper())
acronym()

