This simulates where rain water goes after it has fallen. Using the PIL library to convert a raster image map into a matrix; it runs a series of functions to simulate where the water would go. Before the simulation begins it reduces the raster map by grouping consecutive sections of areas of the same height.
Currently this does not take into account the saturation level of the ground or how much water it can absorb. 

RainFallSimulator arguments:
1. Raster map name*
2. Rain fall in mm
3. Sea level or min water level in map in meters
4. Gamma level used on the colour bar scale for the power normalisation used
5. Max value of the scale in mm
6. Frames (steps) the simulation will take + 1, min value is zero
7. FPS (frames per second)

Currently it saves the simulation as a simulation.gif file. If FFmpeg is installed it will us that as the encoder instead of pillow.

* I have only tested it with TIF format however most likely if PIL can process it, it will work fine.
