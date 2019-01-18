import numpy as np
import MapCell as mapCell
def inRange(matrix, inx, iny):
	if matrix[0] > inx and inx >= 0:
		if matrix[1] > iny and iny >= 0:
			return True

def flowDirrection(next,cur):
	if next is cur: return
	if next.groundLevel > cur.groundLevel:
		cur.higherGround.append(next)
		cur.higherGround.sort(key=lambda x: x.groundLevel)
	if next.groundLevel < cur.groundLevel:
		cur.lowerGround.append(next)
		cur.lowerGround.sort(key=lambda x: x.groundLevel)

def connections(map):
	#mergeCells of same hight beide eachother
	
	print("Reducing Map")
	for (x,y),value in np.ndenumerate(map):
		if not(value.visted):
			findSameHeightAnGroup(map,x,y,value)
			value.incomingWater *= value.gridSize
		value.visted = True
		
	print("Determining water flow directions")
	for (x,y),value in np.ndenumerate(map):
		#top
		size = map.shape
		if inRange(size,x,y+1):
			flowDirrection(map[x][y+1], value)
		#right		
		if inRange(size,x+1,y):
			flowDirrection(map[x+1][y], value)
		#bottem
		if inRange(size,x,y-1):
			flowDirrection(map[x][y-1], value)		
		#left
		if inRange(size,x-1,y):
			flowDirrection(map[x-1][y], value)
			
	for (x,y),value in np.ndenumerate(map):
		value.visted=False
			
			
			
def findSameHeightAnGroup(map,x,y, currentGroup):
	size = map.shape
	if inRange(size,x,y+1) and not(map[x][y+1] is currentGroup) and (map[x][y+1].groundLevel == currentGroup.groundLevel):
				map[x][y+1] = currentGroup
				currentGroup.gridSize +=1
				findSameHeightAnGroup(map,x,y+1,currentGroup)
		#right		
	if inRange(size,x+1,y) and not(map[x+1][y] is currentGroup) and (map[x+1][y].groundLevel == currentGroup.groundLevel):
				map[x+1][y] = currentGroup
				currentGroup.gridSize +=1
				findSameHeightAnGroup(map,x+1,y,currentGroup)
	#bottem
	if inRange(size,x,y-1) and not(map[x][y-1] is currentGroup) and (map[x][y-1].groundLevel == currentGroup.groundLevel):
				map[x][y-1] = currentGroup
				currentGroup.gridSize +=1
				findSameHeightAnGroup(map,x,y-1,currentGroup)
	#left
	if inRange(size,x-1,y) and not(map[x-1][y] is currentGroup) and (map[x-1][y].groundLevel == currentGroup.groundLevel):
				map[x-1][y] = currentGroup
				currentGroup.gridSize +=1
				findSameHeightAnGroup(map,x-1,y,currentGroup)