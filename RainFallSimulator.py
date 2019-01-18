from matplotlib import pyplot as plot, colors
from matplotlib.image import imsave
import matplotlib.animation as animation
from operator import attrgetter
from PIL import Image
import numpy as np
import PreprocessFunctions as preprocess
import MapCell as mapCell
import sys


#load file tif raster areaMap
mapName=sys.argv[1]
rainFall=float(sys.argv[2])
seaLevel=float(sys.argv[3])
gammaLevel=float(sys.argv[4])
colourBarvmax=float(sys.argv[5])
frames=int(sys.argv[6])
fps=int(sys.argv[7])
im = Image.open(mapName)
fig, ax = plot.subplots()
#convert to 2D image of ground hieghts
grid = np.array(im)
#Rain over the area in meters
rainFall = np.full(grid.shape, rainFall/1000.0)
#creates an empty 'areaMap' of the area to be populated
areaMap = np.empty(grid.shape,dtype='O')
mapCell.seaLevel=seaLevel*1.0

for (x,y),value in np.ndenumerate(grid):
		areaMap[x][y] = mapCell.MapCell(value,rainFall[x][y])
print(grid.shape)
preprocess.connections(areaMap)
	
#Coloring in final graph: Green = low, Red = high 
cground = colors.LinearSegmentedColormap.from_list('my_colormap',['green','yellow','red'], 256)
cwater = colors.LinearSegmentedColormap.from_list('my_colormap',[[0,1,1,0],[0,1,1,1],'blue'])
# tell imshow about color areaMap so that only set colors are used
vectGroundFunc = np.vectorize(attrgetter('groundLevel'))
groundMap = plot.imshow(vectGroundFunc(areaMap), cmap=cground,origin='lower')

vectWaterFunc = np.vectorize(attrgetter('waterLevel'))
vectIncWaterFunc = np.vectorize(attrgetter('incomingWater'))
waterMap = plot.imshow(vectWaterFunc(areaMap),  cmap=cwater,origin='lower',norm=colors.PowerNorm(gamma=gammaLevel*1.0, vmax=colourBarvmax/1000.0), animated=True)

colourbar = fig.colorbar(waterMap, ax=ax, extend='max')

#show areaMap and update in loop

print("Starting simluation")
print("Total Water = " + str(np.sum(vectWaterFunc(areaMap))+np.sum(rainFall)))
	
def runSimulation(self):
	
	for (x,y),movingWater in np.ndenumerate(areaMap):
		if not(movingWater.visted):
			movingWater.waterFlow()
			
	#print("Moving Water Total: "+str(np.sum(vectIncWaterFunc(areaMap))))
	
	for (x,y),updatingWaterLevels in np.ndenumerate(areaMap):
		if updatingWaterLevels.visted:
			updatingWaterLevels.updateWaterLevel()
	for (x,y),equalise in np.ndenumerate(areaMap):
		equalise.equaliseWaterLevels()
	
	waterMap.set_data(vectWaterFunc(areaMap))
	colourbar.update_normal(waterMap)
	
	print("Cycle completed")

simulation = animation.FuncAnimation(fig,runSimulation,frames=frames)
#plot.show()
simulation.save('simulation.gif',fps=fps)


#while True:
#	runSimulation()
#	plot.pause(0.5)
	