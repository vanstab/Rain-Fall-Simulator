seaLevel=80.0
class MapCell:
	def __init__(self,groundLevel,incomingWater):
		self.groundLevel=groundLevel
		self.waterLevel=0.0
		if self.groundLevel < seaLevel:
			self.waterLevel = seaLevel-groundLevel
		self.incomingWater=incomingWater
		self.higherGround = []
		self.lowerGround = []
		self.visted=False
		self.gridSize = 1.0
		volume = 0.0

	def updateWaterLevel(self):
		self.waterLevel += self.incomingWater/self.gridSize
		self.incomingWater=0.0
		self.visted=False
	
	def waterFlow(self):
		temp = []
		for lower in self.lowerGround:
			if (lower.waterLevel+lower.groundLevel) < (self.waterLevel+self.groundLevel):
				temp.append(lower)
		
		for lower in temp:
			lower.incomingWater += (self.waterLevel)/len(temp)
			self.incomingWater -= (self.waterLevel)/len(temp)

		self.visted=True
	def equaliseWaterLevels(self):
		for higher in self.higherGround:
			if (higher.waterLevel+higher.groundLevel) < (self.waterLevel+self.groundLevel):
				equaliseWater(self,higher)
				
				
def equaliseWater(fromCell, toCell):
	waterToDist = (fromCell.groundLevel + fromCell.waterLevel)- (toCell.groundLevel + toCell.waterLevel)
	fromCell.waterLevel-=waterToDist/fromCell.gridSize
	equalisedAmount = waterToDist/(fromCell.gridSize+toCell.gridSize)
	toCell.waterLevel+=equalisedAmount
	fromCell.waterLevel+=equalisedAmount
