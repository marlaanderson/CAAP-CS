# takes the number of rows and columns and makes a matrix of those dimensions
def make_matrix(r, c)
	matrix = []
    for i in range(r):
    	list1= []
		for j in range(c):
	    	list1.append(0)
		matrix.append(store)
    return matrix

# takes two matrices and multiplies them returnin the resulting matrix
def matrixmult(a,b):
    if len(a[0]) == len(b):
		matrix2 = make_matrix(len(a), len(b[0]))
		for i in range(len(product)):
	    	for j in range(len(product[0])):
	        	variable = 0
				for n in range(len(b)):
		    		product[i][j] += float(a[i][n]) * float(b[n][j])
		return product
    else:
		return []

# prints the given matrix, mostly for testing purposes
def print_matrix(m):
	print(matrixmult(a,b))

# given a state matrix, and a transition matrix, runs a markov simulation of the game and returns average number of moves.  
def markov_simulation(initial, transition, simulation):
	value = 0
	for i in range(simulation):
		loop = True
		moves = 0
		temp = matrixmult(initial, transition)
			while loop == True:
				temp = matrixmult(temp, transition)
				moves += 1
				if float(temp[0][11]) > float(0.99):
					value += moves
					loop = False
	avgmoves = float(value)/simulation
	print("Average moves: %s" %(avgmoves))