import random

class Bingo:
	def __init__(self):
		self.board = [[0]*5 for i in range(5)] #Create a 5x5 board with initial values of all boxes "0"
		self.mylist = []
		self.mylist_dup = []
		self.sets = [] #This will contain the solution sets, 5 of which when fulfilled in your board will win the game	
		self.sett = [] #This is a single solution set, which will get appended in sets
		self.seq = []
		self.solved = ["X","X","X","X","X"] #This is how the solved set will look like in a list
		self.towin = 5 #You need to complete 5 sets to win a bingo game
		self.setslen = 12 #There are total 12 sets out of which you need 5 in your board to win
		self.bingo = 0 #This is the flag which tells the status of game(Running/Completed)
		self.current = 0 
		self.tocross = 0 #This is the element Player wants to cross out in a turn

	def createBoard(self):
	#board = [[0]*5 for i in range(5)] 
		for i in range(25): #This loop creates a list containing no.s: 1-25
			self.mylist.append(i+1)  
			self.mylist_dup.append(i+1)
		
		for i in range(5): #This nested loop creates a board by randomly assign the 1-25 no.s in different spaces of the 5x5 board
			for j in range(5):
				self.rand_item = random.choice(self.mylist_dup)
				self.board[i][j]=self.rand_item
				self.seq.append(self.rand_item)
				self.mylist_dup.remove(self.rand_item)
		
	def displayBoard(self): #This displays the board
		#for i in range(5):
		#	print(self.board[i])
				
		for i in range(5):
			for j in range(5):
				if self.board[i][j]=="X":
					print(" "+str(self.board[i][j]),end=" ")
				elif self.board[i][j]>9:
					print(self.board[i][j], end = " ")
				else:
					print(end=" ")
					print(self.board[i][j],end=" ")
			print()


		print("No of sets more needed to win: ",self.towin)
		self.tocross = int(input("Enter number you want to cross off:  ")) 

		#self.current = self.seq.index(int(input("Enter number you want to cross off:  ")))
		
	def crossOff(self):  #This locates the element in the board & replaces it with "X" to indicate "Crossed Off"
		self.current = self.seq.index(self.tocross)
		jpos=self.current%5
		ipos=int(self.current/5)
		#print(ipos,jpos)
		self.board[ipos][jpos] = "X"

	def createSets(self): #This creates the current 12 sets, out of which , 5 need to be ["X","X","X","X","X"]
		self.sets = []
		for i in range(5): #5 rows
			for j in range(5):
				self.sett.append(self.board[i][j])
			#print(set)
			self.sets.append(self.sett)
			#print(sets)
			self.sett = []

		self.sett = []
		for i in range(5): #5 columns
			#set = []sets
			for j in range(5):
				self.sett.append(self.board[j][i])
			self.sets.append(self.sett)
			self.sett = []

		for i in range(5): # Set: 1,1 to 5,5
			self.sett.append(self.board[i][i])
		self.sets.append(self.sett)

		j = 4
		self.sett = []
		for i in range(5): # Set: 1,5 to 5,1
			self.sett.append(self.board[i][j])
			j-=1
		self.sets.append(self.sett)
		self.sett = []


	def Sets(self): #Display current sets
		print("Solution Sets:")
		for i in range(len(self.sets)):
			print(self.sets[i])
		print("Total sets: ",len(self.sets))

	def bingocheck(self):
		"""
		print("CURRENT SETS: ")
		for i in range(len(self.sets)):
			print(self.sets[i])
		
		print("---------------------")
		print(len(self.sets))
		"""

		self.towin = 5
		for i in range(len(self.sets)): #Checks how many sets are completed
			if self.sets[i] == self.solved: 
				self.towin-=1
		if self.towin > 0:
			print("No of sets more needed for Player "+str(self.player)+" to win: ",self.towin)
		else:
			self.bingo = 1
			print("BINGO!")
		
		


a = Bingo()
a.createBoard()
#a.displayBoard()
a.createSets()
a.player = 1
#a.Sets()

b= Bingo()
b.createBoard()
b.createSets()
b.player = 2


print("Board ready! The game is about to begin!")
turn = 1
while a.bingo == 0 and b.bingo == 0:
	if turn == 1:
		print("Player 1 turn: ")
		a.displayBoard()
		b.tocross = int(a.tocross)
		turn = 2
	else:
		print("Player 2 turn: ")
		b.displayBoard()
		a.tocross = int(b.tocross)
		turn = 1
	a.crossOff()
	b.crossOff()
	a.createSets()
	b.createSets()
	print()
	a.bingocheck()
	b.bingocheck()
	print()
	