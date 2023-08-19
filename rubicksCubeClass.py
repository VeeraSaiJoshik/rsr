"""
QUOTES : 



"""

from enum import Enum
#The enum library allows you to create custom macros and shortcuts, and it also allows you to map integer values to string values which
#    which makes managing data much easier
import random
#The random library allows us to generate random numbers from a given range, which was mainly used in the implementation of the 
#    scramble generator algorithm


def findIndex(arr, val):
	# this function takes in values arr, which is a list, and val, which is a integer values, and goes through to the list to check
	#  where in the list the value is presented. 
	# post codition : return values fi, 0 <= fi < len(arr), such that arr[fi] == val
	i = 0
	while i < len(arr):
		if val == arr[i] : 
			return i
		i += 1

# ENUMS
class Color(Enum): # <--- The Color Enum is used to identify what color each square on a rubiks cube is
	RED = 1
	BLUE = 2
	GREEN = 3
	WHITE = 4
	YELLOW = 5
	ORANGE = 6
class Side(Enum): # <--- The Side enum allows us to represent the side of a rubiks cube, so we are naming each of the 6 spaces
	Front = 0
	Back = 1
	Left = 2
	Right = 3
	Top = 4
	Bottom = 5
class Edge(Enum): # <--- The Edges, or the pieces on the rubiks cube with 2 colors on them, can be classified into 4 sub-categories in this algorithm. This enum allows us to allocate what subcategory the edge comes under
	Top = 0
	Left = 1
	Right = 2
	Bottom = 3
class WhiteCornerColors(Enum) : # <--- The White Corner, apart from its white side, has two others sides that can be 1 of 4 combinations of colors. We can use this enum to classify what color that corner belogns too; this is important for the F2L step
	RG = 0
	RB = 1
	OG = 2
	OB = 3
class Corner(Enum): # <--- The White Corner, or the pieces on the rubiks cube with 3 colors on them, will have 1 white side and 2 sides of different colors. These White Corners can be in 1 of 8 places, and we can use this enum to identify where it is. This is important for the F2L step.
	BFL = 0
	BFR = 1
	BBL = 2
	BBR = 3
	TFL = 4
	TFR = 5
	TBL = 6
	TBR = 7
class f2lPairStatus(Enum): # <--- An F2L, or first two layer pair, can be classified to be in 1 of 4 states in this algorithm. I can either be formed, be 1 step from being formed, be 3 steps from being formed or be many steps from being formed. Our computer must know what status each f2l pair is when performing the algorithm, which is why we use this ENUM to classify that dat
	pairFormed = 3
	pairUp = 2
	pairDown = 1
	whiteTop = 0
class edgePair(Enum): # <--- This is like the Corner ENUM but for Edges
	TF = 0
	TR = 1
	TB = 2
	TL = 3
	RF = 4
	LF = 5
	RB = 6
	LB = 7
class oll1StepStatus(Enum): # <--- This enum allows us to identify what state our rubiks cube is in during PLL. For this algorith, we use Beginners 2-look PLL, which has 9 different permutations for a total of 3 different possible scenarios
	Dot = 0
	I = 1
	L = 2

#The enumToString method allows us to represent each Enum as a String in the terminal. This function is mainly used for debugging.
def enumToString(enum): 
	if enum == Side.Front :
		return "Front"
	elif enum == Side.Back :
		return "Back"
	elif enum == Side.Right :
		return "Right"
	elif enum == Side.Left :
		return "Left"
	elif enum == Side.Top :
		return "Top"
	elif enum == Side.Bottom :
		return "Bottom"
	elif enum == Edge.Top :
		return "Top Edge"
	elif enum == Edge.Left :
		return "Left Edge"
	elif enum == Edge.Right :
		return "Right Edge"
	elif enum == Edge.Bottom :
		return "Bottom Edge"

class RubicksCubeSides:
	#  The RubiksCubeSides class represents each face of the rubiks cube. It is comprised of a 3x3 array that represent each square on the rubiks cube's side
	#  The RubiksCubeSides class has instance variables that allows you to get the values of a certain block on the side of the rubiks cube
	#	 You can ask for the color of the top-right spot, or the bottom-left spot
	#  This class also has functions that allow you to modify the face of the rubiks cube
	def __del__(self):
		pass
	def arrayIsSame(self):
		what = self.rubicksCubeSidesArray[0][0]
		for i in self.rubicksCubeSidesArray: 
			for j in i : 
				if j != what : 
					return False
		return True
	def getArray(self):
		return self.rubicksCubeSidesArray
	def assignNewValues(self, newSideValues):
		i = j = 0
		while i < 3 : 
			j = 0
			while j < 3 : 
				self.rubicksCubeSidesArray[i][j] = newSideValues[i][j]
				j += 1
			i += 1
		self.assignValToShortCut()

	# The assignValToShortCut function allows one to update the instance variables to match the 3x3 list
	def assignValToShortCut(self):
		self.topLeft = self.rubicksCubeSidesArray[0][0]
		self.topMiddle = self.rubicksCubeSidesArray[0][1]
		self.topRight = self.rubicksCubeSidesArray[0][2]
		# center
		self.centerLeft = self.rubicksCubeSidesArray[1][0]
		self.centerMiddle = self.rubicksCubeSidesArray[1][1]
		self.centerRight = self.rubicksCubeSidesArray[1][2]
		#bottom
		self.bottomLeft = self.rubicksCubeSidesArray[2][0]
		self.bottomMiddle = self.rubicksCubeSidesArray[2][1]
		self.bottomRight = self.rubicksCubeSidesArray[2][2]
	
	# The __init__ declares the side to default to solved. So all 9 squares of a rubik's cube face will have the same color
	def __init__(self, sideArray):
			
		self.rubicksCubeSidesArray = [[], [], []]
		self.rubicksCubeSidesArray[0] = [sideArray, sideArray, sideArray]
		self.rubicksCubeSidesArray[1] = [sideArray, sideArray, sideArray]
		self.rubicksCubeSidesArray[2] = [sideArray, sideArray, sideArray]
		# creating the individual rubicks cube parts
		# top
		self.assignValToShortCut()
		#write code to assign a solved cube
	
	# The changeRight, changeLeft, changeBottom, and changeTop functions allow you to change certain parts of the rubiks cubes face with ease
	#   - These functions come to use when you want to turn the rubiks cube by 90 degrees
	def changeRight(self, newChange):
		original = [self.rubicksCubeSidesArray[0][2], self.rubicksCubeSidesArray[1][2], self.rubicksCubeSidesArray[2][2]]
		self.rubicksCubeSidesArray[0][2] = newChange[0]
		self.topRight = newChange[0]
		self.rubicksCubeSidesArray[1][2] = newChange[1]
		self.centerRight = newChange[1]
		self.rubicksCubeSidesArray[2][2] = newChange[2]
		self.bottomRight = newChange[2]
		return original
	def changeLeft(self, newChange):
		original = [self.rubicksCubeSidesArray[0][0], self.rubicksCubeSidesArray[1][0], self.rubicksCubeSidesArray[2][0]]
		self.rubicksCubeSidesArray[0][0] = newChange[0]
		self.topLeft = newChange[0]
		self.rubicksCubeSidesArray[1][0] = newChange[1]
		self.centerLeft = newChange[1]
		self.rubicksCubeSidesArray[2][0] = newChange[2]
		self.bottomLeft = newChange[2]
		return original
	def changeBottom(self, newChange):
		original = [self.rubicksCubeSidesArray[2][0], self.rubicksCubeSidesArray[2][1], self.rubicksCubeSidesArray[2][2]]
		self.rubicksCubeSidesArray[2][0] = newChange[0]
		self.bottomLeft = newChange[0]
		self.rubicksCubeSidesArray[2][1] = newChange[1]
		self.bottomMiddle = newChange[1]
		self.rubicksCubeSidesArray[2][2] = newChange[2]
		self.bottomRight = newChange[2]
		return original
	def changeTop(self, newChange):
		original = [self.rubicksCubeSidesArray[0][0], self.rubicksCubeSidesArray[0][1], self.rubicksCubeSidesArray[0][2]]
		self.rubicksCubeSidesArray[0][0] = newChange[0]
		self.topLeft = newChange[0]
		self.rubicksCubeSidesArray[0][1] = newChange[1]
		self.topMiddle = newChange[1]
		self.rubicksCubeSidesArray[0][2] = newChange[2]
		self.topRight = newChange[2]
		return original
	# the rotate functions rotates the 3x3 matrix by 90 degrees or -90 degrees
	def rotate(self, clockWise):
		if(clockWise == False):
			n = 3
			rotated_arr = [[0 for _ in range(n)] for _ in range(n)]
			for i in range(n):
				for j in range(n):
					rotated_arr[j][n-i-1] = self.rubicksCubeSidesArray[i][j]
			self.rubicksCubeSidesArray = rotated_arr
			self.assignValToShortCut()
		else:
			n = 3
			rotated_arr = [[0 for _ in range(n)] for _ in range(n)]
			for i in range(n):
				for j in range(n):
					rotated_arr[n-j-1][i] = self.rubicksCubeSidesArray[i][j]
			self.rubicksCubeSidesArray = rotated_arr
			self.assignValToShortCut()

	#this function allows you to turn the color enum to a string. It is mainly used for debugging.
	def colorToString(self, color):
		if(color == Color.WHITE):
			return "White "
		elif(color== Color.YELLOW):
			return "Yellow"
		elif(color== Color.BLUE):
			return "Blue  "
		elif(color== Color.GREEN):
			return "Green "
		elif(color== Color.RED):
			return "Red   "
		elif(color ==Color.ORANGE):
			return "Orange"
	
	#this function allows you to print out a rubiks cube face. It is used for the GUI of the terminal application
	def printF(self):
		print("======= Cube Current State =========")
		print(self.rubicksCubeSidesArray[0][0])
		print(self.colorToString(self.rubicksCubeSidesArray[0][0]))
		print(self.colorToString(self.rubicksCubeSidesArray[0][0]) + " " + self.colorToString(self.rubicksCubeSidesArray[0][1]) + " " + self.colorToString(self.rubicksCubeSidesArray[0][2]))
		print(self.colorToString(self.rubicksCubeSidesArray[1][0]) + " " + self.colorToString(self.rubicksCubeSidesArray[1][1]) + " " + self.colorToString(self.rubicksCubeSidesArray[1][2]))
		print(self.colorToString(self.rubicksCubeSidesArray[2][0]) + " " + self.colorToString(self.rubicksCubeSidesArray[2][1]) + " " + self.colorToString(self.rubicksCubeSidesArray[2][2]))


class RubiksCube:
	def colorToString(self, color):
		if(color == Color.WHITE):
			return "⬜"
		elif(color== Color.YELLOW):
			return "🟨"
		elif(color== Color.BLUE):
			return "🟦"
		elif(color== Color.GREEN):
			return "🟩"
		elif(color== Color.RED):
			return "🟥"
		elif(color ==Color.ORANGE):
			return "🟧"
	def reMapColors(self):
		colorMap = {
			self.front.centerMiddle:Color.BLUE,
   			self.back.centerMiddle:Color.GREEN,
      		self.right.centerMiddle:Color.RED ,
        	self.left.centerMiddle:Color.ORANGE,
			self.top.centerMiddle:Color.YELLOW ,
			self.bottom.centerMiddle:Color.WHITE,
		}
		
		#remapping each side
  
		#remapping the front
		curColor = self.front.getArray()
		for i in range(3):
			for j in range(3):
				curColor[i][j] = colorMap[curColor[i][j]]
		self.front.assignNewValues(curColor)
		
  		#remapping the back
		curColor = self.back.getArray()
		for i in range(3):
			for j in range(3):
				curColor[i][j] = colorMap[curColor[i][j]]
		self.back.assignNewValues(curColor)
  
		#remapping the left
		curColor = self.left.getArray()
		for i in range(3):
			for j in range(3):
				curColor[i][j] = colorMap[curColor[i][j]]
		self.left.assignNewValues(curColor)
  
		#remapping the right
		curColor = self.right.getArray()
		for i in range(3):
			for j in range(3):
				curColor[i][j] = colorMap[curColor[i][j]]
		self.right.assignNewValues(curColor)
  
		#remapping the top
		curColor = self.top.getArray()
		for i in range(3):
			for j in range(3):
				curColor[i][j] = colorMap[curColor[i][j]]
		self.top.assignNewValues(curColor)

		#remapping the bottom
		curColor = self.bottom.getArray()
		for i in range(3):
			for j in range(3):
				curColor[i][j] = colorMap[curColor[i][j]]
		self.bottom.assignNewValues(curColor)
		
                
	def cubeDone(self) : 
		return self.front.arrayIsSame() and self.back.arrayIsSame() and self.top.arrayIsSame() and self.bottom.arrayIsSame() and self.right.arrayIsSame() and self.left.arrayIsSame()
	def getParticipatingEdges(self, corner : Corner, whiteSide): 
		if corner == Corner.TFR and whiteSide == "Right": 
			return {
				"Same" : edgePair.TF, 
				"Opposite" : edgePair.TB
			}
		elif corner == Corner.TFR and whiteSide == "Front": 
			return {
				"Same" : edgePair.TR, 
				"Opposite" : edgePair.TL
			}
		elif corner == Corner.TFL and whiteSide == "Left":
			return {
				"Same" : edgePair.TF, 
				"Opposite" : edgePair.TB
			}
		elif corner == Corner.TFL and whiteSide == "Front":
			return {
				"Same" : edgePair.TL, 
				"Opposite" : edgePair.TR
			}
		elif corner == Corner.TBL and whiteSide == "Back":
			return {
				"Same" : edgePair.TL, 
				"Opposite" : edgePair.TR
			}
		elif corner == Corner.TBL and whiteSide == "Left":
			return {
				"Same" : edgePair.TB, 
				"Opposite" : edgePair.TF
			}
		elif corner == Corner.TBR and whiteSide == "Right":
			return {
				"Same" : edgePair.TB, 
				"Opposite" : edgePair.TF
			}
		elif corner == Corner.TBR and whiteSide == "Back":
			return {
				"Same" : edgePair.TR, 
				"Opposite" : edgePair.TL
			}
		
		
	def getEdges(self, edge : edgePair):
		if edge == edgePair.TF : 
			return {
				"Top" : self.top.bottomMiddle, 
				"Front" : self.front.topMiddle
			}
		elif edge == edgePair.TR : 
			return {
				"Top" : self.top.centerRight, 
				"Right" : self.right.topMiddle
			}
		elif edge == edgePair.TL : 
			return {
				"Top" : self.top.centerLeft, 
				"Left" : self.left.topMiddle
			}
		elif edge == edgePair.TB : 
			return {
				"Top" : self.top.topMiddle, 
				"Back" : self.back.topMiddle
			}
		elif edge == edgePair.RF : 
			return {
				"Dominant" : self.front.centerRight, 
				"Side" : self.right.centerLeft
			}
		elif edge == edgePair.LF : 
			return {
				"Dominant" : self.front.centerLeft, 
				"Side" : self.left.centerRight
			}
		elif edge == edgePair.RB : 
			return {
				"Dominant" : self.back.centerLeft, 
				"Side" : self.right.centerRight
			}
		else : 
			return {
				"Dominant" : self.back.centerRight, 
				"Side" : self.left.centerLeft
			}
	def getCorner(self, corner : Corner):
		
		if corner == Corner.BFR :
			return {
				"Bottom" : self.bottom.topRight, 
				"Front" : self.front.bottomRight, 
				"Right" : self.right.bottomLeft
			}
		elif corner == Corner.BFL:
			return {
				"Bottom" : self.bottom.topLeft, 
				"Front" : self.front.bottomLeft, 
				"Left" : self.left.bottomRight, 
			}
		elif corner == Corner.BBL:
			return {
				"Back" : self.back.bottomRight, 
				"Bottom" : self.bottom.bottomLeft, 
				"Left" : self.left.bottomLeft
			}
		elif corner == Corner.BBR:
			return {
				"Back" : self.back.bottomLeft, 
				"Bottom" : self.bottom.bottomRight, 
				"Right" : self.right.bottomRight
			}
		elif corner == Corner.TFL:
			return {
				"Front" : self.front.topLeft, 
				"Left" : self.left.topRight, 
				"Top" : self.top.bottomLeft
			}
		elif corner == Corner.TFR:
			return {
				"Front" : self.front.topRight, 
				"Right" : self.right.topLeft, 
				"Top" : self.top.bottomRight
			}
		elif corner == Corner.TBL:
			return {
				"Top" : self.top.topLeft, 
				"Back" : self.back.topRight,
				"Left" : self.left.topLeft
			}
		elif corner == Corner.TBR:
			return {
				"Top" : self.top.topRight, 
				"Back" : self.back.topLeft, 
				"Right" : self.right.topRight
			}
	def __init__(self, param):
		self.solution = ""
		if(isinstance(param, bool)): 
			self.bottom = RubicksCubeSides(Color.WHITE)
			self.top = RubicksCubeSides(Color.YELLOW)
			self.right = RubicksCubeSides(Color.RED)
			self.left = RubicksCubeSides(Color.ORANGE)
			self.back = RubicksCubeSides(Color.GREEN)
			self.front = RubicksCubeSides(Color.BLUE)
		elif(isinstance(param , list)):
			self.top = RubicksCubeSides(param[0])
			self.bottom = RubicksCubeSides(param[1])
			self.left = RubicksCubeSides(param[2])
			self.right = RubicksCubeSides(param[3])
			self.front = RubicksCubeSides(param[4])
			self.back = RubicksCubeSides(param[5])
	def printF(self):
		print("       --------")
		print("       |" +  self.colorToString(self.top.topLeft)+""+self.colorToString(self.top.topMiddle)+ "" +self.colorToString(self.top.topRight)+ "|              ")
		print("       |" +  self.colorToString(self.top.centerLeft)+""+self.colorToString(self.top.centerMiddle)+""+self.colorToString(self.top.centerRight)+ "|              ")
		print("       |" +  self.colorToString(self.top.bottomLeft)+""+self.colorToString(self.top.bottomMiddle)+""+self.colorToString(self.top.bottomRight)+ "|              ")
		print("-------"*4 + "-")
		print("|" + self.colorToString(self.left.topLeft)+""+self.colorToString(self.left.topMiddle)+ "" +self.colorToString(self.left.topRight)+"|" +  self.colorToString(self.front.topLeft)+""+self.colorToString(self.front.topMiddle)+ "" +self.colorToString(self.front.topRight)+ "|"+ self.colorToString(self.right.topLeft)+""+self.colorToString(self.right.topMiddle)+ "" +self.colorToString(self.right.topRight)+"|"+ self.colorToString(self.back.topLeft)+""+self.colorToString(self.back.topMiddle)+ "" +self.colorToString(self.back.topRight) + "|")
		print("|" + self.colorToString(self.left.centerLeft)+""+self.colorToString(self.left.centerMiddle)+ "" +self.colorToString(self.left.centerRight)+"|" +  self.colorToString(self.front.centerLeft)+""+self.colorToString(self.front.centerMiddle)+""+self.colorToString(self.front.centerRight)+ "|" + "" + self.colorToString(self.right.centerLeft)+""+self.colorToString(self.right.centerMiddle)+ "" +self.colorToString(self.right.centerRight)+"|" + self.colorToString(self.back.centerLeft)+""+self.colorToString(self.back.centerMiddle)+ "" +self.colorToString(self.back.centerRight)+ "|")
		print("|" + self.colorToString(self.left.bottomLeft)+""+self.colorToString(self.left.bottomMiddle)+ "" +self.colorToString(self.left.bottomRight)+"|" +  self.colorToString(self.front.bottomLeft)+""+self.colorToString(self.front.bottomMiddle)+""+self.colorToString(self.front.bottomRight)+ "|"+ self.colorToString(self.right.bottomLeft)+""+self.colorToString(self.right.bottomMiddle)+ "" +self.colorToString(self.right.bottomRight)+"|" + self.colorToString(self.back.bottomLeft)+""+self.colorToString(self.back.bottomMiddle)+ "" +self.colorToString(self.back.bottomRight)+ "|")
		print("-------"*4 + "-")
		print("       |" +  self.colorToString(self.bottom.topLeft)+""+self.colorToString(self.bottom.topMiddle)+ "" +self.colorToString(self.bottom.topRight)+ "|              ")
		print("       |" +  self.colorToString(self.bottom.centerLeft)+""+self.colorToString(self.bottom.centerMiddle)+""+self.colorToString(self.bottom.centerRight)+ "|              ")
		print("       |" +  self.colorToString(self.bottom.bottomLeft)+""+self.colorToString(self.bottom.bottomMiddle)+""+self.colorToString(self.bottom.bottomRight)+ "|              ")
		print("       --------")
	def moveRight(self):
		self.right.rotate(False)
		tempChange = self.front.changeRight([self.bottom.topRight, self.bottom.centerRight, self.bottom.bottomRight])
		tempChange = self.top.changeRight(tempChange)
		tempChange = self.back.changeLeft([tempChange[2], tempChange[1], tempChange[0]])
		self.bottom.changeRight([tempChange[2], tempChange[1], tempChange[0]])
	def moveLeft(self):
		self.left.rotate(False)
		tempChange = self.front.changeLeft([self.top.topLeft, self.top.centerLeft, self.top.bottomLeft])
		tempChange = self.bottom.changeLeft(tempChange)
		tempChange = self.back.changeRight([tempChange[2], tempChange[1], tempChange[0]])
		self.top.changeLeft([tempChange[2], tempChange[1], tempChange[0]])
	def moveFront(self):
		temp =  self.top.changeBottom([self.left.bottomRight, self.left.centerRight, self.left.topRight])
		temp1 = [self.right.rubicksCubeSidesArray[2][0], self.right.rubicksCubeSidesArray[1][0], self.right.rubicksCubeSidesArray[0][0]]
		self.right.rubicksCubeSidesArray[0][0] = temp[0]
		self.right.rubicksCubeSidesArray[1][0] = temp[1]
		self.right.rubicksCubeSidesArray[2][0] = temp[2]
		self.right.assignValToShortCut()
		temp = [self.bottom.rubicksCubeSidesArray[0][0], self.bottom.rubicksCubeSidesArray[0][1], self.bottom.rubicksCubeSidesArray[0][2]]
		self.bottom.rubicksCubeSidesArray[0] = [temp1[0], temp1[1], temp1[2]]
		self.bottom.assignValToShortCut()
		self.left.rubicksCubeSidesArray[0][2] = temp[0]
		self.left.rubicksCubeSidesArray[1][2] = temp[1]
		self.left.rubicksCubeSidesArray[2][2] = temp[2]
		self.left.assignValToShortCut()
		self.front.rotate(False)
	def moveBack(self):
		temp = [self.left.topLeft, self.left.centerLeft, self.left.bottomLeft]
		self.left.rubicksCubeSidesArray[0][0] = self.top.topRight
		self.left.rubicksCubeSidesArray[1][0] = self.top.topMiddle
		self.left.rubicksCubeSidesArray[2][0] = self.top.topLeft
		self.left.assignValToShortCut() 
		temp2 = [self.bottom.bottomRight, self.bottom.bottomMiddle, self.bottom.bottomLeft]
		self.bottom.rubicksCubeSidesArray[2][0] = temp[0]
		self.bottom.rubicksCubeSidesArray[2][1] = temp[1]
		self.bottom.rubicksCubeSidesArray[2][2] = temp[2]
		self.bottom.assignValToShortCut()
		temp = self.right.changeRight(temp2)
		self.top.changeTop(temp)
		self.back.rotate(False)
	def moveUp(self):
		self.top.rotate(False)
		tempChange = self.front.changeTop([self.right.rubicksCubeSidesArray[0][0], self.right.rubicksCubeSidesArray[0][1], self.right.rubicksCubeSidesArray[0][2]])
		tempChange = self.left.changeTop(tempChange)
		tempChange = self.back.changeTop(tempChange)
		self.right.changeTop(tempChange)
	def moveDown(self):
		self.bottom.rotate(False)
		tempChange = self.back.changeBottom(self.right.rubicksCubeSidesArray[2])
		tempChange = self.left.changeBottom(tempChange)
		tempChange = self.front.changeBottom(tempChange)
		self.right.changeBottom(tempChange)
	def getOtherEdgeColor(self, side, orientation):
		if side == Side.Top:
			if orientation == Edge.Top :
				return self.back.topMiddle
			elif orientation == Edge.Left : 
				return self.left.topMiddle
			elif orientation == Edge.Right : 
				return self.right.topMiddle
			else : 
				return self.front.topMiddle
		elif side == Side.Bottom:
			if orientation == Edge.Top :
				return self.front.bottomMiddle
			elif orientation == Edge.Left : 
				return self.left.bottomMiddle
			elif orientation == Edge.Right : 
				return self.right.bottomMiddle
			else : 
				return self.back.bottomMiddle
		elif side == Side.Right:
			if orientation == Edge.Top :
				return self.top.centerRight
			elif orientation == Edge.Left : 
				return self.front.centerRight
			elif orientation == Edge.Right : 
				return self.back.centerLeft
			else : 
				return self.bottom.centerRight
		elif side == Side.Left:
			if orientation == Edge.Top :
				return self.top.centerLeft
			elif orientation == Edge.Left : 
				return self.back.centerRight
			elif orientation == Edge.Right : 
				return self.front.centerLeft
			else : 
				return self.bottom.centerLeft
		elif side == Side.Front:
			if orientation == Edge.Top :
				return self.top.bottomMiddle
			elif orientation == Edge.Left : 
				return self.left.centerRight
			elif orientation == Edge.Right : 
				return self.right.centerLeft
			else : 
				return self.bottom.topMiddle
		elif side == Side.Back:
			if orientation == Edge.Top :
				return self.top.topMiddle
			elif orientation == Edge.Left : 
				return self.right.centerRight
			elif orientation == Edge.Right : 
				return self.left.centerLeft
			else : 
				return self.bottom.bottomMiddle
	def playGround(self):
		moveN = 1
		move = input("move:")
		while True:
			
			moveN += 1
			if move == "break":
				break
			else:
				self.scramble(move.upper())
			self.printF()
			move = input("(move #" + str(moveN) + ") next move :")
			
	
	def scrambleUnharmed(self, scramble):
		scrambleList = scramble.split()
		commandList = ""
		for move in scrambleList:
			if len(move) == 1:
				commandList += move
			elif move[1].isdigit():
				commandList += move[0] * int(move[1])
			else:
				commandList += move[0].lower()
		for command in commandList:
			if command == "U":
				self.moveUp()
			if command == "D":
				self.moveDown()
			if command == "R":
				self.moveRight()
			if command == "L":
				self.moveLeft()
			if command == "F":
				self.moveFront()
			if command == "B":
				self.moveBack()
			if command == "u":
				self.moveUp()
				self.moveUp()
				self.moveUp()
			if command == "d":
				self.moveDown()
				self.moveDown()
				self.moveDown()
			if command == "r":
				self.moveRight()
				self.moveRight()
				self.moveRight()
			if command == "l":
				self.moveLeft()
				self.moveLeft()
				self.moveLeft()
			if command == "f":
				self.moveFront()
				self.moveFront()
				self.moveFront()
			if command == "b":
				self.moveBack()
				self.moveBack()
				self.moveBack()
		self.front.assignValToShortCut()
		self.back.assignValToShortCut()
		self.left.assignValToShortCut()
		self.right.assignValToShortCut()
		self.top.assignValToShortCut()
		self.bottom.assignValToShortCut()
	def scramble(self, scramble):
		scrambleList = scramble.split()
		commandList = ""
		self.solution += scramble + " "
		for move in scrambleList:
			if len(move) == 1:
				commandList += move
			elif move[1].isdigit():
				commandList += (move[0] * int(move[1]))
			elif len(move) == 3 :
				commandList += (move[0].lower() * int(move[2]))
			else:
				commandList += move[0].lower()
		for command in commandList:
			if command == "U":
				self.moveUp()
			if command == "D":
				self.moveDown()
			if command == "R":
				self.moveRight()
			if command == "L":
				self.moveLeft()
			if command == "F":
				self.moveFront()
			if command == "B":
				self.moveBack()
			if command == "u":
				self.moveUp()
				self.moveUp()
				self.moveUp()
			if command == "d":
				self.moveDown()
				self.moveDown()
				self.moveDown()
			if command == "r":
				self.moveRight()
				self.moveRight()
				self.moveRight()
			if command == "l":
				self.moveLeft()
				self.moveLeft()
				self.moveLeft()
			if command == "f":
				self.moveFront()
				self.moveFront()
				self.moveFront()
			if command == "b":
				self.moveBack()
				self.moveBack()
				self.moveBack()
		self.front.assignValToShortCut()
		self.back.assignValToShortCut()
		self.left.assignValToShortCut()
		self.right.assignValToShortCut()
		self.top.assignValToShortCut()
		self.bottom.assignValToShortCut()
		
class CubeSolver:
	def __init__(self, cube : RubiksCube):
		self.rubiksCube = cube
		moves3 = open("moveList/3Move.txt", "r")
		moves6 = open("moveList/6Move.txt", "r")
		moves4 = open("moveList/4Move.txt", "r")
		self.moves3 = moves3.readlines()
		self.moves6 = moves6.readlines()
		self.moves4 = moves4.readlines()
	def reversePermutations(self, permutation : str):
		pList = permutation.split()
		pList.reverse()
		ans  = ""
		for p in pList : 
			if len(p) == 2 : 
				ans += p[0] + " "
			else : 
				ans += p + "' "
		return ans
	def whiteCrossDoneNumber(self):
		cube = self.rubiksCube
		pairsFormed = 0
		if cube.bottom.topMiddle == Color.WHITE and cube.getOtherEdgeColor(Side.Bottom, Edge.Top) == Color.BLUE: 
			pairsFormed+=1
		if (cube.bottom.centerLeft == Color.WHITE and cube.getOtherEdgeColor(Side.Bottom, Edge.Left) == Color.ORANGE) == True: 
			pairsFormed+=1
		if (cube.bottom.centerRight == Color.WHITE and cube.getOtherEdgeColor(Side.Bottom, Edge.Right) == Color.RED) == True: 
			pairsFormed+=1
		if (cube.bottom.bottomMiddle == Color.WHITE and cube.getOtherEdgeColor(Side.Bottom, Edge.Bottom) == Color.GREEN) == True: 
			pairsFormed+=1
		return pairsFormed
	def whiteCrossDone(self):
		cube = self.rubiksCube
		if (cube.bottom.topMiddle == Color.WHITE and cube.getOtherEdgeColor(Side.Bottom, Edge.Top) == Color.BLUE) == False: 
			return False
		elif (cube.bottom.centerLeft == Color.WHITE and cube.getOtherEdgeColor(Side.Bottom, Edge.Left) == Color.ORANGE) == False: 
			return False
		elif (cube.bottom.centerRight == Color.WHITE and cube.getOtherEdgeColor(Side.Bottom, Edge.Right) == Color.RED) == False: 
			return False
		elif (cube.bottom.bottomMiddle == Color.WHITE and cube.getOtherEdgeColor(Side.Bottom, Edge.Bottom) == Color.GREEN) == False: 
			return False
		return True
	def cubePairs(self, cube : RubiksCube):
		solvedSides = 0
		if cube.front.topMiddle == Color.BLUE and cube.getOtherEdgeColor(Side.Front, Edge.Top) == Color.WHITE:
			solvedSides +=1
		elif cube.front.centerLeft == Color.BLUE and cube.getOtherEdgeColor(Side.Front, Edge.Left) == Color.WHITE:
			solvedSides +=1
		elif cube.front.centerRight == Color.BLUE and cube.getOtherEdgeColor(Side.Front, Edge.Right) == Color.WHITE:
			solvedSides +=1
		elif cube.front.bottomMiddle == Color.BLUE and cube.getOtherEdgeColor(Side.Front, Edge.Bottom) == Color.WHITE:
			solvedSides +=1
		
		if cube.left.topMiddle == Color.ORANGE and cube.getOtherEdgeColor(Side.Left, Edge.Top) == Color.WHITE:
			solvedSides +=1
		elif cube.left.centerLeft == Color.ORANGE and cube.getOtherEdgeColor(Side.Left, Edge.Left) == Color.WHITE:
			solvedSides +=1
		elif cube.left.centerRight == Color.ORANGE and cube.getOtherEdgeColor(Side.Left, Edge.Right) == Color.WHITE:
			solvedSides +=1
		elif cube.left.bottomMiddle == Color.ORANGE and cube.getOtherEdgeColor(Side.Left, Edge.Bottom) == Color.WHITE:
			solvedSides +=1
		
		if cube.right.topMiddle == Color.RED and cube.getOtherEdgeColor(Side.Right, Edge.Top) == Color.WHITE:
			solvedSides +=1
		elif cube.right.centerLeft == Color.RED and cube.getOtherEdgeColor(Side.Right, Edge.Left) == Color.WHITE:
			solvedSides +=1
		elif cube.right.centerRight == Color.RED and cube.getOtherEdgeColor(Side.Right, Edge.Right) == Color.WHITE:
			solvedSides +=1
		elif cube.right.bottomMiddle == Color.RED and cube.getOtherEdgeColor(Side.Right, Edge.Bottom) == Color.WHITE:
			solvedSides +=1
		
		if cube.back.topMiddle == Color.GREEN and cube.getOtherEdgeColor(Side.Back, Edge.Top) == Color.WHITE:
			solvedSides +=1
		elif cube.back.centerLeft == Color.GREEN and cube.getOtherEdgeColor(Side.Back, Edge.Left) == Color.WHITE:
			solvedSides +=1
		elif cube.back.centerRight == Color.GREEN and cube.getOtherEdgeColor(Side.Back, Edge.Right) == Color.WHITE:
			solvedSides +=1
		elif cube.back.bottomMiddle == Color.GREEN and cube.getOtherEdgeColor(Side.Back, Edge.Bottom) == Color.WHITE:
			solvedSides +=1
		return solvedSides
	def yellowSideDone(self) : 
		for i in self.rubiksCube.top.rubicksCubeSidesArray : 
			for j in i: 
				if j != Color.YELLOW : 
					return False
		return True
	def f2lSideFree(self) : 
		if ((self.rubiksCube.getCorner(Corner.BFR)["Front"] == Color.BLUE and self.rubiksCube.getCorner(Corner.BFR)["Right"] == Color.RED and self.rubiksCube.getCorner(Corner.BFR)["Bottom"] == Color.WHITE) and (self.rubiksCube.getEdges(edgePair.RF)["Dominant"] == Color.BLUE and self.rubiksCube.getEdges(edgePair.RF)["Side"] == Color.RED)) == False:
			self.rubiksCube.scramble("R U R' U'")
			return [Corner.TFR, "R U R' U' "]
		elif ((self.rubiksCube.getCorner(Corner.BFL)["Front"] == Color.BLUE and self.rubiksCube.getCorner(Corner.BFL)["Left"] == Color.ORANGE and self.rubiksCube.getCorner(Corner.BFL)["Bottom"] == Color.WHITE) and (self.rubiksCube.getEdges(edgePair.LF)["Dominant"] == Color.BLUE and self.rubiksCube.getEdges(edgePair.LF)["Side"] == Color.ORANGE)) == False:
			self.rubiksCube.scramble("L' U' L U")
			return [Corner.TFL, "L' U' L U "]
		elif ((self.rubiksCube.getCorner(Corner.BBR)["Back"] == Color.GREEN and self.rubiksCube.getCorner(Corner.BBR)["Right"] == Color.RED and self.rubiksCube.getCorner(Corner.BBR)["Bottom"] == Color.WHITE) and (self.rubiksCube.getEdges(edgePair.RB)["Dominant"] == Color.GREEN and self.rubiksCube.getEdges(edgePair.RB)["Side"] == Color.RED)) == False:
			self.rubiksCube.scramble("R' U' R U")
			return [Corner.TBR, "R' U' R U "]
			
		elif ((self.rubiksCube.getCorner(Corner.BBL)["Back"] == Color.GREEN and self.rubiksCube.getCorner(Corner.BBL)["Left"] == Color.ORANGE and self.rubiksCube.getCorner(Corner.BBL)["Bottom"] == Color.WHITE) and (self.rubiksCube.getEdges(edgePair.LB)["Dominant"] == Color.GREEN and self.rubiksCube.getEdges(edgePair.LB)["Side"] == Color.ORANGE)) == False:
			self.rubiksCube.scramble("L U L' U'")
			return [Corner.TBL, "L U L' U' "]
		return False
	def f2l(self):
		pairDone = 0
		cornerList = [Corner.TFR, Corner.TFL, Corner.TBL, Corner.TBR]
		colorToColorMap = {
			WhiteCornerColors.OB : Corner.TFL, 
			WhiteCornerColors.RB : Corner.TFR, 
			WhiteCornerColors.OG : Corner.TBL, 
			WhiteCornerColors.RG : Corner.TBR
		}
		f2lPermutation = ""
		final = ""
		while pairDone < 4: 
			mostOptimalCorner = None
			mostOptimalCornerStatus = None
			corners = [Corner.TFL, Corner.TFR, Corner.TBL, Corner.TBR]
			edgeList = [edgePair.TF, edgePair.TL, edgePair.TB, edgePair.TR]
			for i in corners : 
				cKey = ""
				otherColors = []
				for key in self.rubiksCube.getCorner(i):
					if self.rubiksCube.getCorner(i)[key] == Color.WHITE : 
						cKey = key
					else : 
						otherColors.append(self.rubiksCube.getCorner(i)[key])
				if cKey != "":
					cornerStatus = None
					setEdge = None
					for edge in edgeList : 
						flag = True
						for key in self.rubiksCube.getEdges(edge) : 
							if (self.rubiksCube.getEdges(edge)[key] in otherColors) == False : 
								flag = False
						if flag == True : 
							setEdge = edge
					edgesPairList = self.rubiksCube.getParticipatingEdges(i, cKey)
					
					if cKey == "Top" : 
						cornerStatus = f2lPairStatus.whiteTop
					elif setEdge == None : 
						cornerStatus = f2lPairStatus.pairDown
					elif setEdge == edgesPairList["Opposite"] and self.rubiksCube.getEdges(setEdge)["Top"] != self.rubiksCube.getCorner(i)["Top"] : 
						cornerStatus = f2lPairStatus.pairFormed
					elif setEdge == edgesPairList["Same"] and self.rubiksCube.getEdges(setEdge)["Top"] == self.rubiksCube.getCorner(i)["Top"] : 
						cornerStatus = f2lPairStatus.pairFormed
					else : 
						cornerStatus = f2lPairStatus.pairUp
					if mostOptimalCornerStatus == None : 
						mostOptimalCorner = i
						mostOptimalCornerStatus = cornerStatus
					elif cornerStatus.value > mostOptimalCornerStatus.value: 
						mostOptimalCorner = i
						mostOptimalCornerStatus =  cornerStatus
			f2lPermutation0 = ""
			topF2lPermutation = ""
			topF2lPermutation5 = ""

			if mostOptimalCorner == None : 
				solve = self.f2lSideFree()
				#print(solve)
				if  solve != False : 
					topF2lPermutation = solve[1]
					i =solve[0]
					cKey = ""
					otherColors = []
					for key in self.rubiksCube.getCorner(i):
						if self.rubiksCube.getCorner(i)[key] == Color.WHITE : 
							cKey = key
						else : 
							otherColors.append(self.rubiksCube.getCorner(i)[key])
					if cKey != "":
						cornerStatus = None
						setEdge = None
						for edge in edgeList : 
							flag = True
							for key in self.rubiksCube.getEdges(edge) : 
								if (self.rubiksCube.getEdges(edge)[key] in otherColors) == False : 
									flag = False
							if flag == True : 
								setEdge = edge
						edgesPairList = self.rubiksCube.getParticipatingEdges(i, cKey)
						
						if cKey == "Top" : 
							cornerStatus = f2lPairStatus.whiteTop
						elif setEdge == None : 
							cornerStatus = f2lPairStatus.pairDown
						elif setEdge == edgesPairList["Opposite"] and self.rubiksCube.getEdges(setEdge)["Top"] != self.rubiksCube.getCorner(i)["Top"] : 
							cornerStatus = f2lPairStatus.pairFormed
						elif setEdge == edgesPairList["Same"] and self.rubiksCube.getEdges(setEdge)["Top"] == self.rubiksCube.getCorner(i)["Top"] : 
							cornerStatus = f2lPairStatus.pairFormed
						else : 
							cornerStatus = f2lPairStatus.pairUp
						if mostOptimalCornerStatus == None : 
							mostOptimalCorner = i
							mostOptimalCornerStatus = cornerStatus
						elif cornerStatus.value > mostOptimalCornerStatus.value: 
							mostOptimalCorner = i
							mostOptimalCornerStatus =  cornerStatus
				else : 
					break
			if mostOptimalCornerStatus == f2lPairStatus.whiteTop : 
				cornerColors = []
				for key in self.rubiksCube.getCorner(mostOptimalCorner) : 
					if self.rubiksCube.getCorner(mostOptimalCorner)[key] != Color.WHITE :
						cornerColors.append(self.rubiksCube.getCorner(mostOptimalCorner)[key])
				if Color.ORANGE in cornerColors and Color.BLUE in cornerColors : 
					cornerColor = WhiteCornerColors.OB
				elif Color.ORANGE in cornerColors and Color.GREEN in cornerColors : 
					cornerColor = WhiteCornerColors.OG
				elif Color.RED in cornerColors and Color.BLUE in cornerColors : 
					cornerColor = WhiteCornerColors.RB
				elif Color.RED in cornerColors and Color.GREEN in cornerColors : 
					cornerColor = WhiteCornerColors.RG
				upMovesNum = findIndex(cornerList, colorToColorMap[cornerColor]) - findIndex(cornerList, mostOptimalCorner)
				ij = 0
				mostOptimalCorner = colorToColorMap[cornerColor]
				
				while ij < abs(upMovesNum):
					if upMovesNum < 0 : 
						f2lPermutation += "U' "
						self.rubiksCube.scramble("U'")
					else : 
						f2lPermutation += "U "
						self.rubiksCube.scramble("U")
					ij += 1
				if mostOptimalCorner == Corner.TFL : 
					topF2lPermutation += "L' U L U U "
					self.rubiksCube.scramble("L' U L U U")
				elif mostOptimalCorner == Corner.TFR : 
					topF2lPermutation += "R U' R' U' U' "
					self.rubiksCube.scramble("R U' R' U' U'")
				elif mostOptimalCorner == Corner.TBL : 
					topF2lPermutation += "L U' L' U' U' "
					self.rubiksCube.scramble("L U' L' U' U'")
				else : 
					topF2lPermutation += "R' U R U U "
					self.rubiksCube.scramble("R' U R U U")
				i = mostOptimalCorner
				cKey = ""
				otherColors = []
				for key in self.rubiksCube.getCorner(i):
					if self.rubiksCube.getCorner(i)[key] == Color.WHITE : 
						cKey = key
					else : 
						otherColors.append(self.rubiksCube.getCorner(i)[key])
				if cKey != "":
					cornerStatus = None
					setEdge = None
					for edge in edgeList : 
						flag = True
						for key in self.rubiksCube.getEdges(edge) : 
							if (self.rubiksCube.getEdges(edge)[key] in otherColors) == False : 
								flag = False
						if flag == True : 
							setEdge = edge
					edgesPairList = self.rubiksCube.getParticipatingEdges(i, cKey)
					
					if cKey == "Top" : 
						cornerStatus = f2lPairStatus.whiteTop
					elif setEdge == None : 
						cornerStatus = f2lPairStatus.pairDown
					elif setEdge == edgesPairList["Opposite"] and self.rubiksCube.getEdges(setEdge)["Top"] != self.rubiksCube.getCorner(i)["Top"] : 
						cornerStatus = f2lPairStatus.pairFormed
					elif setEdge == edgesPairList["Same"] and self.rubiksCube.getEdges(setEdge)["Top"] == self.rubiksCube.getCorner(i)["Top"] : 
						cornerStatus = f2lPairStatus.pairFormed
					else : 
						cornerStatus = f2lPairStatus.pairUp
					if mostOptimalCornerStatus == None : 
						mostOptimalCorner = i
						mostOptimalCornerStatus = cornerStatus
					elif cornerStatus.value > mostOptimalCornerStatus.value: 
						mostOptimalCorner = i
						mostOptimalCornerStatus =  cornerStatus
			if mostOptimalCornerStatus == f2lPairStatus.pairDown: 
				mo = self.rubiksCube.getCorner(mostOptimalCorner)
				colorList = []
				for key in mo : 
					if mo[key] != Color.WHITE :
						colorList.append(mo[key])
				for edge in [edgePair.RF, edgePair.LF, edgePair.RB, edgePair.LB]: 
					flag = True
					for key in self.rubiksCube.getEdges(edge) : 
						if flag == True : 
							flag = self.rubiksCube.getEdges(edge)[key] in colorList 
					if flag : 
						targetEdge = edge
				if targetEdge == edgePair.RF : 
					if mostOptimalCorner == Corner.TFR : 
						f2lPermutation0 += "U "
						self.rubiksCube.scramble("U")
						mostOptimalCorner = Corner.TFL
					if mostOptimalCorner == Corner.TBL : 
						f2lPermutation0 += "U "
						self.rubiksCube.scramble("U")
						mostOptimalCorner = Corner.TBR
					f2lPermutation0 += "R U R' "
					self.rubiksCube.scramble("R U R'")
					if mostOptimalCorner == Corner.TFL : 
						mostOptimalCorner = Corner.TBL
					elif mostOptimalCorner == Corner.TBL : 
						mostOptimalCorner = Corner.TFR
				elif targetEdge == edgePair.RB : 
					if mostOptimalCorner != Corner.TFL:
						upMovesNum = findIndex(cornerList,  Corner.TFL) - findIndex(cornerList, mostOptimalCorner)
						ij = 0
						while ij < abs(upMovesNum):
							if upMovesNum < 0 : 
								f2lPermutation0 += "U' "
								self.rubiksCube.scramble("U'")
							else : 
								f2lPermutation0 += "U "
								self.rubiksCube.scramble("U ")
							ij += 1
					f2lPermutation0 += "R' U R "
					self.rubiksCube.scramble("R' U R")
					
					mostOptimalCorner = Corner.TBL 
				elif targetEdge == edgePair.LB : 

					if mostOptimalCorner == Corner.TBL:
						f2lPermutation0 += "U "
						mostOptimalCorner = Corner.TBR
						self.rubiksCube.scramble("U")
					if mostOptimalCorner == Corner.TFR:
						f2lPermutation0 += "U "
						mostOptimalCorner = Corner.TFL
						self.rubiksCube.scramble("U")
					f2lPermutation0 += "L U L' "
					self.rubiksCube.scramble("L U L' ")
					if mostOptimalCorner == Corner.TBR : 
						mostOptimalCorner = Corner.TFR 
					elif mostOptimalCorner == Corner.TFR : 
						mostOptimalCorner = Corner.TBL
				else : 
					if mostOptimalCorner != Corner.TBR:
						upMovesNum = findIndex(cornerList,  Corner.TBR) - findIndex(cornerList, mostOptimalCorner)
						ij = 0
						while ij < abs(upMovesNum):
							if upMovesNum < 0 : 
								f2lPermutation0 += "U' "
								self.rubiksCube.scramble("U'")
							else : 
								f2lPermutation0 += "U "
								self.rubiksCube.scramble("U")
							ij += 1
					
					f2lPermutation0 += "L' U L "
					self.rubiksCube.scramble("L' U L")
					mostOptimalCorner = Corner.TFR 
				mostOptimalCornerStatus = f2lPairStatus.pairUp
				
			f2lPermutation = ""
			if mostOptimalCornerStatus == f2lPairStatus.pairUp: 
				cornerColor = None
				cornerColors = []
				for key in self.rubiksCube.getCorner(mostOptimalCorner) : 
					if self.rubiksCube.getCorner(mostOptimalCorner)[key] != Color.WHITE :
						cornerColors.append(self.rubiksCube.getCorner(mostOptimalCorner)[key])
				if Color.ORANGE in cornerColors and Color.BLUE in cornerColors : 
					cornerColor = WhiteCornerColors.OB
				elif Color.ORANGE in cornerColors and Color.GREEN in cornerColors : 
					cornerColor = WhiteCornerColors.OG
				elif Color.RED in cornerColors and Color.BLUE in cornerColors : 
					cornerColor = WhiteCornerColors.RB
				elif Color.RED in cornerColors and Color.GREEN in cornerColors : 
					cornerColor = WhiteCornerColors.RG
				upMovesNum = findIndex(cornerList, colorToColorMap[cornerColor]) - findIndex(cornerList, mostOptimalCorner)
				ij = 0
				mostOptimalCorner = colorToColorMap[cornerColor]
				while ij < abs(upMovesNum):
					if upMovesNum < 0 : 
						f2lPermutation += "U' "
						self.rubiksCube.scramble("U'")
					else : 
						f2lPermutation += "U "
						self.rubiksCube.scramble("U")
					ij += 1
				mocm = self.rubiksCube.getCorner(mostOptimalCorner)
				# checking for the amabigous case 
				if mostOptimalCorner == Corner.TFR : 
					
					if mocm["Right"] == Color.WHITE and self.rubiksCube.getEdges(edgePair.TR)["Top"] in [Color.RED, Color.BLUE] and self.rubiksCube.getEdges(edgePair.TR)["Right"] in [Color.RED, Color.BLUE]:
						f2lPermutation += "U' R U' R' U "
						self.rubiksCube.scramble("U' R U' R' U")
					elif self.rubiksCube.getEdges(edgePair.TF)["Top"] in [Color.RED, Color.BLUE] and self.rubiksCube.getEdges(edgePair.TF)["Front"] in [Color.RED, Color.BLUE]: 
						f2lPermutation += "U F' U F U' "
						self.rubiksCube.scramble("U F' U F U'")
				elif mostOptimalCorner == Corner.TFL : 
					if mocm["Left"] == Color.WHITE and self.rubiksCube.getEdges(edgePair.TL)["Top"] in [Color.ORANGE, Color.BLUE] and self.rubiksCube.getEdges(edgePair.TL)["Left"] in [Color.ORANGE, Color.BLUE]:
						f2lPermutation += "U L' U L U' "
						self.rubiksCube.scramble("U L' U L U'")
					elif self.rubiksCube.getEdges(edgePair.TF)["Top"] in [Color.ORANGE, Color.BLUE] and self.rubiksCube.getEdges(edgePair.TF)["Front"] in [Color.ORANGE, Color.BLUE]: 
						f2lPermutation += "U' F U' F' U "
						self.rubiksCube.scramble("U' F U' F' U")
				elif mostOptimalCorner == Corner.TBL : 
					if mocm["Left"] == Color.WHITE and self.rubiksCube.getEdges(edgePair.TL)["Top"] in [Color.ORANGE, Color.GREEN] and self.rubiksCube.getEdges(edgePair.TL)["Left"] in [Color.ORANGE, Color.GREEN]:
						f2lPermutation += "U' L U' L' U" 
						self.rubiksCube.scramble("U' L U' L' U")
					elif self.rubiksCube.getEdges(edgePair.TB)["Top"] in [Color.ORANGE, Color.GREEN] and self.rubiksCube.getEdges(edgePair.TB)["Back"] in [Color.ORANGE, Color.GREEN]: 
						f2lPermutation += "U B' U B U' "
						self.rubiksCube.scramble("U B' U B U'")
				else : 
									
					if mocm["Right"] == Color.WHITE and self.rubiksCube.getEdges(edgePair.TR)["Top"] in [Color.RED, Color.GREEN] and self.rubiksCube.getEdges(edgePair.TR)["Right"] in [Color.RED, Color.GREEN]:
						f2lPermutation += "U R' U R U' "
						self.rubiksCube.scramble("U R' U R U'")
					elif self.rubiksCube.getEdges(edgePair.TB)["Top"] in [Color.GREEN, Color.RED] and self.rubiksCube.getEdges(edgePair.TB)["Back"] in [Color.GREEN, Color.RED]: 
						f2lPermutation += "U' B U' B' U "
						self.rubiksCube.scramble("U' B U' B' U")
				if mostOptimalCorner == Corner.TFR : 
					if mocm["Right"] == Color.WHITE : 
						# move the edge out of the way
						f2lPermutation += "U F' "
						self.rubiksCube.scramble("U F'")
						for edge in edgeList : 
							flag = True
							for key in self.rubiksCube.getEdges(edge) : 
								if (self.rubiksCube.getEdges(edge)[key] in cornerColors) == False : 
									flag = False
							if flag == True : 
								setEdge = edge
						if self.rubiksCube.getEdges(setEdge)["Top"] == mocm["Top"] : 
							wannaMove = findIndex(edgeList, edgePair.TL) - findIndex(edgeList, setEdge)
						else : 
							wannaMove = findIndex(edgeList, edgePair.TR) - findIndex(edgeList, setEdge)
					else : 
						f2lPermutation += "U' R "
						self.rubiksCube.scramble("U' R")
						for edge in edgeList : 
							flag = True
							for key in self.rubiksCube.getEdges(edge) :
								if (self.rubiksCube.getEdges(edge)[key] in cornerColors) == False : 
									flag = False
							if flag == True : 
								setEdge = edge
						if self.rubiksCube.getEdges(setEdge)["Top"] == mocm["Top"] : 
							wannaMove = findIndex(edgeList, edgePair.TB) - findIndex(edgeList, setEdge)
						else : 
							wannaMove = findIndex(edgeList, edgePair.TF) - findIndex(edgeList, setEdge)
					iterator = 0
					while iterator < abs(wannaMove) : 
						if wannaMove < 0 : 
							f2lPermutation += "U' "
							self.rubiksCube.scramble("U'")
						else : 
							f2lPermutation += "U "
							self.rubiksCube.scramble("U")
						iterator += 1
					if mocm["Right"] == Color.WHITE : 
						f2lPermutation += "F U' "
						self.rubiksCube.scramble("F U'")
					else : 
						f2lPermutation += "R' U "
						self.rubiksCube.scramble("R' U")
				elif mostOptimalCorner == Corner.TFL : 
					if mocm["Left"] == Color.WHITE : 
						# move the edge out of the way
						f2lPermutation += "U' F "
						self.rubiksCube.scramble("U' F")
						for edge in edgeList : 
							flag = True
							for key in self.rubiksCube.getEdges(edge) : 
								if (self.rubiksCube.getEdges(edge)[key] in cornerColors) == False : 
									flag = False
							if flag == True : 
								setEdge = edge
						if self.rubiksCube.getEdges(setEdge)["Top"] == mocm["Top"] : 
							wannaMove = findIndex(edgeList, edgePair.TR) - findIndex(edgeList, setEdge)
						else : 
							wannaMove = findIndex(edgeList, edgePair.TL) - findIndex(edgeList, setEdge)
					else : 
						f2lPermutation += "U L' "
						self.rubiksCube.scramble("U L'")
						for edge in edgeList : 
							flag = True
							for key in self.rubiksCube.getEdges(edge) : 
								if (self.rubiksCube.getEdges(edge)[key] in cornerColors) == False : 
									flag = False
							if flag == True : 
								setEdge = edge
						if self.rubiksCube.getEdges(setEdge)["Top"] == mocm["Top"] : 
							wannaMove = findIndex(edgeList, edgePair.TB) - findIndex(edgeList, setEdge)
						else : 
							wannaMove = findIndex(edgeList, edgePair.TF) - findIndex(edgeList, setEdge)
				
					iterator = 0
					while iterator < abs(wannaMove) : 
						if wannaMove < 0 : 
							f2lPermutation += "U' "
							self.rubiksCube.scramble("U'")
						else : 
							f2lPermutation += "U "
							self.rubiksCube.scramble("U")
						iterator += 1
					
					if mocm["Left"] == Color.WHITE : 
						f2lPermutation += "F' U "
						self.rubiksCube.scramble("F' U")
					else : 
						f2lPermutation += "L U' "
						self.rubiksCube.scramble("L U'")
				elif mostOptimalCorner == Corner.TBL : 
					if mocm["Back"] == Color.WHITE : 
						# move the edge out of the way
						f2lPermutation += "U' L "
						self.rubiksCube.scramble("U' L")
						for edge in edgeList : 
							flag = True
							for key in self.rubiksCube.getEdges(edge) : 
								if (self.rubiksCube.getEdges(edge)[key] in cornerColors) == False : 
									flag = False
							if flag == True : 
								setEdge = edge
						if self.rubiksCube.getEdges(setEdge)["Top"] == mocm["Top"] : 
							wannaMove = findIndex(edgeList, edgePair.TF) - findIndex(edgeList, setEdge)
						else : 
							wannaMove = findIndex(edgeList, edgePair.TB) - findIndex(edgeList, setEdge)
					else : 
						f2lPermutation += "U B' "
						self.rubiksCube.scramble("U B'")
						for edge in edgeList : 
							flag = True
							for key in self.rubiksCube.getEdges(edge) : 
								if (self.rubiksCube.getEdges(edge)[key] in cornerColors) == False : 
									flag = False
							if flag == True : 
								setEdge = edge
						if self.rubiksCube.getEdges(setEdge)["Top"] == mocm["Top"] : 
							wannaMove = findIndex(edgeList, edgePair.TR) - findIndex(edgeList, setEdge)
						else : 
							wannaMove = findIndex(edgeList, edgePair.TL) - findIndex(edgeList, setEdge)
					iterator = 0
					while iterator < abs(wannaMove) : 
						if wannaMove < 0 : 
							f2lPermutation += "U' "
							self.rubiksCube.scramble("U'")
						else : 
							f2lPermutation += "U "
							self.rubiksCube.scramble("U")
						iterator += 1
					if mocm["Back"] == Color.WHITE : 
						f2lPermutation += "L' U "
						self.rubiksCube.scramble("L' U")
					else : 
						f2lPermutation += "B U' "
						self.rubiksCube.scramble("B U'")
				else : 
					if mocm["Right"] == Color.WHITE : 
						# move the edge out of the way
						f2lPermutation += "U' B "
						self.rubiksCube.scramble("U' B")
						for edge in edgeList : 
							flag = True
							for key in self.rubiksCube.getEdges(edge) : 
								if (self.rubiksCube.getEdges(edge)[key] in cornerColors) == False : 
									flag = False
							if flag == True : 
								setEdge = edge
						if self.rubiksCube.getEdges(setEdge)["Top"] == mocm["Top"] : 
							wannaMove = findIndex(edgeList, edgePair.TL) - findIndex(edgeList, setEdge)
						else : 
							wannaMove = findIndex(edgeList, edgePair.TR) - findIndex(edgeList, setEdge)
					else : 
						f2lPermutation += "U R' "
						self.rubiksCube.scramble("U R'")
						for edge in edgeList : 
							flag = True
							for key in self.rubiksCube.getEdges(edge) : 
								if (self.rubiksCube.getEdges(edge)[key] in cornerColors) == False : 
									flag = False
							if flag == True : 
								setEdge = edge
						if self.rubiksCube.getEdges(setEdge)["Top"] == mocm["Top"] : 
							wannaMove = findIndex(edgeList, edgePair.TF) - findIndex(edgeList, setEdge)
						else : 
							wannaMove = findIndex(edgeList, edgePair.TB) - findIndex(edgeList, setEdge)
					iterator = 0
					while iterator < abs(wannaMove) : 
						if wannaMove < 0 : 
							f2lPermutation += "U' "
							self.rubiksCube.scramble("U'")
						else : 
							f2lPermutation += "U "
							self.rubiksCube.scramble("U")
						iterator += 1
					if mocm["Right"] == Color.WHITE : 
						f2lPermutation += "B' U "
						self.rubiksCube.scramble("B' U")
					else : 
						f2lPermutation += "R U' "
						self.rubiksCube.scramble("R U'")
				mostOptimalCornerStatus = f2lPairStatus.pairFormed
		
			f2lPermutation2 = ""
			if mostOptimalCornerStatus == f2lPairStatus.pairFormed : 
				# placing the edge in the desired area
				cornerColor = None
				cornerColors = []
			
				for key in self.rubiksCube.getCorner(mostOptimalCorner) : 
					cornerColors.append(self.rubiksCube.getCorner(mostOptimalCorner)[key])
			
				if Color.ORANGE in cornerColors and Color.BLUE in cornerColors : 
					cornerColor = WhiteCornerColors.OB
				elif Color.ORANGE in cornerColors and Color.GREEN in cornerColors : 
					cornerColor = WhiteCornerColors.OG
				elif Color.RED in cornerColors and Color.BLUE in cornerColors : 
					cornerColor = WhiteCornerColors.RB
				elif Color.RED in cornerColors and Color.GREEN in cornerColors : 
					cornerColor = WhiteCornerColors.RG
				upMovesNum = findIndex(cornerList, colorToColorMap[cornerColor]) - findIndex(cornerList, mostOptimalCorner)
				ij = 0
				mostOptimalCorner = colorToColorMap[cornerColor]
				
				while ij < abs(upMovesNum):
					if upMovesNum < 0 : 
						f2lPermutation2 += "U' "
						self.rubiksCube.scramble("U'")
					else : 
						f2lPermutation2 += "U "
						self.rubiksCube.scramble("U")
					ij += 1
				mocm = self.rubiksCube.getCorner(mostOptimalCorner)
				# inserting the corner into desired area
				if mostOptimalCorner == Corner.TFR : 
					if mocm["Right"] == Color.WHITE : 
						if self.rubiksCube.getEdges(edgePair.TF)["Top"] == mocm["Top"] and self.rubiksCube.getEdges(edgePair.TF)["Front"] == mocm["Front"]: 
							f2lPermutation2 += "F R' F' R "
							self.rubiksCube.scramble("F R' F' R")
						else : 
							f2lPermutation2 += "R U R' "
							self.rubiksCube.scramble("R U R' ")
					else : 
						if self.rubiksCube.getEdges(edgePair.TR)["Top"] == mocm["Top" ] and self.rubiksCube.getEdges(edgePair.TR)["Right"] == mocm["Right"] : 
							f2lPermutation2 += "R' F R F' "
							self.rubiksCube.scramble("R' F R F' ")
						else : 
							f2lPermutation2 += "F' U' F "
							self.rubiksCube.scramble("F' U' F")
				elif mostOptimalCorner == Corner.TFL : 
					if mocm["Left"] == Color.WHITE : 
									
						if self.rubiksCube.getEdges(edgePair.TF)["Top"] == mocm["Top"] and self.rubiksCube.getEdges(edgePair.TF)["Front"] == mocm["Front"]: 
							f2lPermutation2 += "F' L F L' "
							self.rubiksCube.scramble("F' L F L' ")
						else : 
							
							f2lPermutation2 += "L' U' L "
							self.rubiksCube.scramble("L' U' L")
					else : 
						if self.rubiksCube.getEdges(edgePair.TL)["Top"] == mocm["Top"]  and self.rubiksCube.getEdges(edgePair.TL)["Left"] == mocm["Left"] : 
							f2lPermutation2 += "L F' L' F "
							self.rubiksCube.scramble("L F' L' F")
						else : 
							f2lPermutation2 += "F U F' "
							self.rubiksCube.scramble("F U F' ")
				elif mostOptimalCorner == Corner.TBL : 
					if mocm["Left"] == Color.WHITE : 
						if self.rubiksCube.getEdges(edgePair.TB)["Top"] == mocm["Top"] and self.rubiksCube.getEdges(edgePair.TB)["Back"] == mocm["Back"] : 
							f2lPermutation2 += "U' B' U B "
							self.rubiksCube.scramble("U' B' U B ")
						else : 

							f2lPermutation2 += "L U L' "
							self.rubiksCube.scramble("L U L'")
					else : 
						if self.rubiksCube.getEdges(edgePair.TL)["Top"] == mocm["Top"] and self.rubiksCube.getEdges(edgePair.TL)["Left"] == mocm["Left"] : 
							f2lPermutation2 += "U L U' L' "
							self.rubiksCube.scramble("U L U' L' ")
						else : 
							f2lPermutation2 += "B' U' B "
							self.rubiksCube.scramble("B' U' B")
				else : 
					
					if mocm["Right"] == Color.WHITE : 
						if self.rubiksCube.getEdges(edgePair.TB)["Top"] == mocm["Top"] and self.rubiksCube.getEdges(edgePair.TB)["Back"] == mocm["Back"]  : 
							f2lPermutation2 += "U B U' B' "
							self.rubiksCube.scramble("U B U' B'")
						else : 
							f2lPermutation2 += "R' U' R "
							self.rubiksCube.scramble("R' U' R")
					else : 
						if self.rubiksCube.getEdges(edgePair.TR)["Top"] == mocm["Top"] and self.rubiksCube.getEdges(edgePair.TR)["Right"] == mocm["Right"] : 
							f2lPermutation2 += "U' R' U R "
							self.rubiksCube.scramble("U' R' U R")
						else : 
							f2lPermutation2 += "B U B' "
							self.rubiksCube.scramble("B U B'")
			final += topF2lPermutation5 + topF2lPermutation + f2lPermutation0 + f2lPermutation  + f2lPermutation2 + "\n"
			pairDone += 1

		return final
	def removeCounter(self, solution) : 
		changes = -1
		solutionList = solution.split()
		while changes != 0 :
			
			changes = 0
			solutionList = solution.split()
			solution = ""
			flag = False
			i = 0
			while i < len(solutionList) - 1: 
				if (solutionList[i] != solutionList[i + 1] + "'" and solutionList[i] + "'" != solutionList[i + 1]) and flag == False : 
					solution += solutionList[i] + " "
				elif flag == True : 
					flag = False
				elif solutionList[i] != solutionList[i + 1] + "'" or solutionList[i] + "'" != solutionList[i + 1]: 
					changes += 1
					flag = True
				i += 1
			if flag == False : 
				solution += solutionList[len(solutionList) - 1]
		return solution
	def condenseRepeats(self, solutionList) : 
		i = 0
		prev = solutionList[i]
		count = 0
		solution = ""
		while i < len(solutionList) : 
			if solutionList[i] == prev : 
				count += 1
			else : 
				count = count % 4
			#	print("=" * 40)
			#	print(solutionList)
			#	print(i)
			#	print(count)
			#	print(prev)
				if count != 0 : 
					if count == 1 : 
						solution += prev + " "
					elif count == 3 : 
						prev = prev + "'"
						prev = prev.replace("''", "")
						solution += prev + " "
					else : 
						prev = prev + str(count)
						prev = prev.replace("'2", "2")
						solution +=  prev + " "
			#	print(solution)
				prev = solutionList[i]
				count = 1
				#input()
			i += 1
		count = count % 4
		if count != 0 : 
			if count == 1 : 
				solution += prev + " "
			elif count == 3 : 
				prev = prev + "'"
				prev = prev.replace("''", "")
				solution += prev + " "
			else : 
				solution += prev + str(count) + " "
		return solution
	def simplifyAlgorithmSet(self, solution): 
		prev = ""
		while True : 
			solution = self.removeCounter(solution)
			solution = self.condenseRepeats(solution.split(" "))
			if solution == prev : 
				break
			prev = solution
		return solution
	def whiteCross(self, h, i):
		if i == 8:
			return [h]
		i += 1
		p = [self.whiteCross(h + "R ", i), self.whiteCross(h + "R' ", i), self.whiteCross(h + "L ", i), self.whiteCross(h + "L' ", i), self.whiteCross(h + "F ", i), self.whiteCross(h + "F' ", i), self.whiteCross(h + "B ", i), self.whiteCross(h + "B' ", i)]
		permutations = []
		for i in p : 
			for j in i : 
				permutations.append(j)
		return permutations
	def oll(self):
		ollSolution = ""
		ollStep = None
		#step 1 
		i = 0
		#print("=" * 10 + "OLL"  + "=" * 10)
		while i < 4 : 
			self.rubiksCube.scramble("U")
			ollSolution += "U "
			edgeOriented = 0
			if self.rubiksCube.top.topMiddle == Color.YELLOW :
				edgeOriented += 1
			if self.rubiksCube.top.centerLeft == Color.YELLOW :
				edgeOriented += 1
			if self.rubiksCube.top.centerRight == Color.YELLOW :
				edgeOriented += 1
			if self.rubiksCube.top.bottomMiddle == Color.YELLOW :
				edgeOriented += 1
			if edgeOriented == 0 : 
				ollStep = oll1StepStatus.Dot
				break
			elif edgeOriented == 2 and self.rubiksCube.top.bottomMiddle == Color.YELLOW and self.rubiksCube.top.centerRight == Color.YELLOW : 
				ollStep = oll1StepStatus.L
				break
			elif edgeOriented == 2 and self.rubiksCube.top.centerLeft == Color.YELLOW and self.rubiksCube.top.centerRight == Color.YELLOW : 
				ollStep = oll1StepStatus.I
				break
			
			i += 1
		if ollStep == oll1StepStatus.I : 
			ollSolution += "F R U R' U' F' "
			self.rubiksCube.scramble("F R U R' U' F'")
		elif ollStep == oll1StepStatus.L : 
			ollSolution += "B U L U' L' B' "
			self.rubiksCube.scramble("B U L U' L' B'")
		elif ollStep == oll1StepStatus.Dot : 
			ollSolution += "F R U R' U' F' B U L U' L' B' "
			self.rubiksCube.scramble("F R U R' U' F' B U L U' L' B'")
		# second step
		oll2Permutations = [
			"R U U R' U' R U' R'",
			"R U R' U R U' R' U R U U R'",
			"F R' F' L F R F' L'", 
			"R U U R R U' R R U' R R U U R",
			"R U R' U R U U R'",
			"L F R' F' L' F R F'",
			"U' L F R' F' L' F R F' L U U L L U' L L U' L L U U L ", # <== take out this permutation
		]
		i = 0
		while i < 4 : 
			#print(i)
			self.rubiksCube.scramble("U")
			ollSolution += "U "
			
			for permutation in oll2Permutations : 
				self.rubiksCube.scrambleUnharmed(permutation)
				#print(self.checkYellowSideDone())
				if self.checkYellowSideDone() == False : 
					self.rubiksCube.scrambleUnharmed(self.reversePermutations(permutation))
				else : 
					i = 5
					ollSolution += permutation
					break
				#self.rubiksCube.printF()
			i += 1
		# laset step
		i = 0
		#print("=" * 20)
		return ollSolution
	def checkYellowSideDone(self):
		for i in self.rubiksCube.top.rubicksCubeSidesArray : 
			for j in i : 
				if j != Color.YELLOW : 
					return False
		return True
	def checkYellowCornerDone(self) :
		
		if self.rubiksCube.front.topRight != self.rubiksCube.front.topLeft : 
			return False
		if self.rubiksCube.back.topRight != self.rubiksCube.back.topLeft : 
			return False
		if self.rubiksCube.left.topRight != self.rubiksCube.left.topLeft : 
			return False
		if self.rubiksCube.right.topRight != self.rubiksCube.right.topLeft : 
			return False
		return True
	def pll(self) : 
		# aligning the corners : 
		pllPermutation = " "
		pllPermutaitons1 = [
			"F R U' R' U' R U R' F' R U R' U' R' F R F'", 
			"R U R' U' R' F R R U' R' U' R U R' F'"
		]
		i = 0
		while i < 4 : 
			pllPermutation += "U "
			self.rubiksCube.scrambleUnharmed("U")
			for permutation in pllPermutaitons1 : 
				self.rubiksCube.scrambleUnharmed(permutation)
				if self.checkYellowCornerDone() : 
					pllPermutation += permutation + " "
					i = 5
					break
				else : 
					self.rubiksCube.scrambleUnharmed(self.reversePermutations(permutation))
			i += 1
		#aligning the edge : 
		pllPermutation2 = [
			"R U' R U R U R U' R' U' R R", 
			"R R U R U R' U' R' U' R' U R'", 
			""
		]
		i = 0
		while i < 4 : 
			pllPermutation += "U "
			self.rubiksCube.scrambleUnharmed("U")
			for first in pllPermutation2 : 
				flag = False
				for second in pllPermutation2 : 
					# 0 U moves
					self.rubiksCube.scramble(first + " " + second + " ")
					if self.topLayerComplete() : 
						flag = True 
						pllPermutation += first + " " + second + " "
						break
					else : 
						self.rubiksCube.scramble(self.reversePermutations(first + " " + second + " "))
					# 1 U moves
					self.rubiksCube.scramble(first + " U " + second + " ")
					if self.topLayerComplete() : 
						flag = True 
						pllPermutation += first + " U " + second + " "
						break
					else : 
						self.rubiksCube.scramble(self.reversePermutations(first + " U " + second + " "))
					# 2 U moves
					self.rubiksCube.scramble(first + " U U " + second + " ")
					if self.topLayerComplete() : 
						flag = True 
						pllPermutation += first + " U U " + second + " "
						break
					else : 
						self.rubiksCube.scramble(self.reversePermutations(first + " U U " + second + " "))
					# 3 U moves
					self.rubiksCube.scramble(first + " U U U " + second + " ")
					if self.topLayerComplete() : 
						flag = True 
						pllPermutation += first + " U U U " + second + " "
						break
					else : 
						self.rubiksCube.scramble(self.reversePermutations(first + " U U U " + second + " "))
				if flag : 
					i = 5
					break
			i += 1
		i = 0
		while i < 4 : 
			if self.rubiksCube.front.topMiddle == self.rubiksCube.front.centerMiddle : 
				break
			pllPermutation += "U "
			self.rubiksCube.scramble("U")
			i += 1
		return pllPermutation
	def topLayerComplete(self) : 
		if (self.rubiksCube.front.topLeft == self.rubiksCube.front.topMiddle and self.rubiksCube.front.topLeft == self.rubiksCube.front.topRight ) == False : 
			return False
		if (self.rubiksCube.right.topLeft == self.rubiksCube.right.topMiddle and self.rubiksCube.right.topLeft == self.rubiksCube.right.topRight ) == False : 
			return False
		if (self.rubiksCube.left.topLeft == self.rubiksCube.left.topMiddle and self.rubiksCube.left.topLeft == self.rubiksCube.left.topRight ) == False : 
			return False
		if (self.rubiksCube.back.topLeft == self.rubiksCube.back.topMiddle and self.rubiksCube.back.topLeft == self.rubiksCube.back.topRight ) == False : 
			return False
		return True 
	def solve(self):
		#condensing lsit
		solution = ""
		if self.cubePairs(self.rubiksCube) < 3 : 
			for permutation in self.moves6:
				self.rubiksCube.scramble(permutation)
				if self.cubePairs(self.rubiksCube) >= 3 : 
					solution = solution + permutation
					break
				self.rubiksCube.scramble(self.reversePermutations(permutation))
		if self.cubePairs(self.rubiksCube) != 4 : 
			for permutation in self.moves6:
				self.rubiksCube.scramble(permutation)
				if self.cubePairs(self.rubiksCube) == 4 : 
					solution = solution + permutation
					break
				self.rubiksCube.scramble(self.reversePermutations(permutation))
		i = 0
		if self.whiteCrossDoneNumber() != 1 :
			for permutation in self.moves3:
				self.rubiksCube.scramble(permutation)
				if self.whiteCrossDoneNumber() == 1 and self.cubePairs(self.rubiksCube) == 4: 
					solution = solution + permutation
					break
				self.rubiksCube.scramble(self.reversePermutations(permutation))
		if self.whiteCrossDoneNumber() != 2:
			for permutation in self.moves3:
				self.rubiksCube.scramble(permutation)
				if self.whiteCrossDoneNumber() == 2 and self.cubePairs(self.rubiksCube) == 4: 
					solution = solution + permutation
					break
				self.rubiksCube.scramble(self.reversePermutations(permutation))
		if self.whiteCrossDoneNumber() != 3:
			for permutation in self.moves3:
				self.rubiksCube.scramble(permutation)
				if self.whiteCrossDoneNumber() == 3 and self.cubePairs(self.rubiksCube) == 4: 
					solution = solution + permutation
					break
				self.rubiksCube.scramble(self.reversePermutations(permutation))
		if self.whiteCrossDoneNumber() != 4:
			for permutation in self.moves3:
				self.rubiksCube.scramble(permutation)
				if self.whiteCrossDoneNumber() == 4 and self.cubePairs(self.rubiksCube) == 4: 
					solution = solution + permutation
					break
				self.rubiksCube.scramble(self.reversePermutations(permutation))
		self.rubiksCube.solution = ""
		self.f2l()
		print("white cross")
		print(solution)
		f2ls = self.rubiksCube.solution
		print("f2l")
		print(f2ls)
		olls = self.oll()
		print("oll")
		print(olls)
		plls = self.pll()
		print("Pll")
		print(plls)
		return self.simplifyAlgorithmSet(solution + f2ls + olls + plls)
		scrambles = [
			"",
			"B2 D' R U F' D' B2 R U2 L' F' R2 B' L B2 L' D2 R2 D2 F2 R2",
             "R2 B2 U L2 F2 R2 D' B2 R2 U' F2 R F2 D2 L F L2 B' R F2 L U2",
             "D R2 U' L2 D2 R2 U' R2 D2 F2 D L' B R' D' L' U2 L2 F' U B",
             "D R2 U R2 B2 U2 F2 L2 B2 L2 B2 L2 R2 U L' U2 B' L' F2 U R' F' L F'",
             "L B R' D F' L D2 R U' R2 B2 L2 U B2 R2 D2 F2 L2 D' R2 U2 B2",
             "B2 U F2 D L2 B2 U2 B2 F2 R2 U2 L' B L B L U' R' D R D' U2 R F L",
             "B' R' U2 F2 U' L2 F2 R2 U2 B2 L2 F2 L2 R' F R B U2 F' R' F R U",
             "F2 D' L2 B2 L2 F2 R2 F2 U R2 B2 U' B' U F R F U' L F L' F' U'",
             "F L' U' L2 B' R2 U2 B' R2 F2 U2 B' L2 F2 U' R F' L' F U' B L B' R' U",
             "R' U2 F' L' B L2 U' R' F2 R2 U2 L2 B2 R2 F2 R' F2 L2 B D2 L B R' D L'",
             "F' R2 U' L' B L B' U' R' F2 L2 F2 R2 B2 U2 F2 L2 B' L2 B' U2 L F2 R U",
             "B' D' F2 U B2 R2 U2 L2 F2 L2 F2 R2 B2 U2 R F' L F' L U' R' D R D' B L' U",
             "R2 U F2 U' L2 B2 U' L2 F2 L2 F2 U' R B' L F' U' L2 F' L2 F2 L F2 R2 U2",
             "B L2 U' B2 R2 F2 U' R2 F2 L2 U L2 B' R' F' L F' R U' L U2 R2 F2 L2 U",
             "B' R F U' F' L F' R U' B' L2 U' R2 D2 F2 U2 L2 B2 R2 U2 L F' R F L'",
             "F2 L2 B2 R2 U2 F2 R2 U' R2 B2 U' F' R F' R U' R' D R D' B' R U' R' U R'",
             "B' R2 F2 L2 F2 R2 B2 L2 U2 B2 D2 R' U",
			 ]

def generate_scramble(n):
    scramble = []
    prev_move = None
    moves = ["U", "U'", "U2", "D", "D'", "D2", "L", "L'", "L2", "R", "R'", "R2", "F", "F'", "F2", "B", "B'", "B2"]
    for i in range(n):
        move = random.choice(moves)
        if prev_move is not None and move[0] == prev_move[0]:
            while move[0] == prev_move[0]:
                move = random.choice(moves)
        scramble.append(move)
        prev_move = move
    return " ".join(scramble)
class testcase : 
	def __init__(self, a, s):
		self.scramble = s
		self.time = a

"""cube = RubiksCube(True)
cube.scrambleUnharmed("F2 L2 R2 D L2 D R2 D' B2 F2 U F L' B F U F' D2 R2 D2 R2")
solver = CubeSolver(cube)
solution = solver.solve()
print(solution)
"""