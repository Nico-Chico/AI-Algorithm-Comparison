import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Reading data
# Open solutions file and reading limits and mode
fp = open('solutions.txt', 'r')
minXlim = int(fp.readline())
maxXlim = int(fp.readline())
minYlim = int(fp.readline())
maxYlim = int(fp.readline())
mode = fp.readline()
minZlim = 12
maxZlim = 12
### Manual axes
minXlim = -14
maxXlim = 14
minYlim = -14
maxYlim = 14
minZlim = -8
maxZlim = 8


# # Read 
# particles = 4; ## Amount of particles
# timeSteps = 10;
# colors = ['b', 'r', 'g', 'y']
# colors = np.random.rand(particles)
# data = np.random.uniform(-10, 10, size=(particles, timeSteps, 3)) # (particle, timestep, coordinates)
# print("Generated data in use")
# print(data)
# print("End of data")

###
line = fp.readline()
while line != "END\n":
    s = line.split(') ')
    ID = int(s[0])
    s2 = s[1].split()
    t = int(s2[0])
    coords = [float(s2[1]), float(s2[2]), float(s2[3])]
    print(ID, t, coords)
    data[id, t, coords]
    line = fp.readline()





# #Set plot in interactive mode
# plt.ion()


# #Setting figure and axis
# fig = plt.figure(figsize=(20,16))
# ax = fig.gca(projection='3d')

# ax.set_xlim([minXlim,maxXlim])
# ax.set_ylim([minYlim,maxYlim])
# ax.set_zlim([minZlim,maxZlim])

# #Open the plot
# plt.show()


# # ### MODE PSO - Plotting 3D Matrix Data

# # Function
# X = np.arange(minXlim, maxXlim, 0.25)
# Y = np.arange(minYlim, maxYlim, 0.25)
# X, Y = np.meshgrid(X, Y)
# Z = np.sin(np.sqrt(X**2 + Y**2))

# # Plot the surface.
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True, alpha=0.2)


# # Plotting
# for t in list(range(timeSteps)):
#     x = data[:,t,0]
#     y = data[:,t,1]
#     z = data[:,t,2]
#     scat = ax.scatter(x, y, z, s=80, c=colors) #Update the plot becouse we are in interactive mode
#     plt.pause(1)
#     scat.remove()

# plt.show(block = True) # To keep the plot until you close it.

