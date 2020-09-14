import math
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import numpy as np

# creating a sphere
def fibonacci_sphere(samples=100):

    points = []
    phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = math.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        z = math.sin(theta) * radius

        points.append([x, y, z])

    return np.array(points)

# adding spherical coordinates to the sphere as last 3 arguments
def appendSpherical_np(xyz):
    ptsnew = np.hstack((xyz, np.zeros(xyz.shape)))
    xy = xyz[:,0]**2 + xyz[:,1]**2
    ptsnew[:,3] = np.sqrt(xy + xyz[:,2]**2)
    ptsnew[:,4] = np.arctan2(np.sqrt(xy), xyz[:,2]) # for elevation angle defined from Z-axis down
    ptsnew[:,5] = np.arctan2(xyz[:,1], xyz[:,0])
    return ptsnew

a = plt.figure().add_subplot(111, projection='3d')

# Function to create slices for forexample quarter peony
def azimuth_slices(samples = 500, slices = 4, ghost_value = 0):
    sphere = appendSpherical_np(fibonacci_sphere(samples))
    f3d_array = []
    for i in range(1, slices+1):
        angle_min = (2*(i-1)*math.pi/slices)-math.pi
        angle_max = (2*(i)*math.pi/slices)-math.pi
        part_sphere = sphere[np.argwhere((sphere[:,5]>angle_min) & (sphere[:,5]<angle_max)),:]
        a.scatter(part_sphere[:,:,0],part_sphere[:,:,1],part_sphere[:,:,2])
        f3d_partial_array = np.hstack([part_sphere[:,:,0],part_sphere[:,:,1],part_sphere[:,:,2], ghost_value*np.ones_like(part_sphere[:,:,2])])
        f3d_array.append(f3d_partial_array.tolist())
    return(f3d_array)

stars_wanted = int(input("How many stars do you want?(4in/100mm normal = 120, 4in/100mm dense = 240, 5in/125mm normal = 140, 5in/125mm dense = 280, 6in/150mm normal = 160, 6in/150mm dense = 320): "))
slices_wanted = int(input("How many azimuth slices do you want?(Quarter peony = 4): "))
ghost_wanted = int(input("What ghost value do you want? (normal shell = 0): "))

print("Copy this JSON list of lists into the custom JSON field in F3D: ")
print(azimuth_slices(stars_wanted,slices_wanted,ghost_wanted))
plt.show()