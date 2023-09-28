import numpy as np
import math
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

# Regarding the JSON output
# A break pattern is a list of subpatterns.
# A subpattern is a list of stars.
# A star is a list of 4 numbers.
# Each star is a 4-tuple list.  [x,y,z,ghost_time_offset].
# The sub patterns are used for different colors etc, one for each potential child star definition


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
    xy = xyz[:, 0]**2 + xyz[:, 1]**2
    ptsnew[:, 3] = np.sqrt(xy + xyz[:, 2]**2)
    # for elevation angle defined from Z-axis down
    ptsnew[:, 4] = np.arctan2(np.sqrt(xy), xyz[:, 2])
    ptsnew[:, 5] = np.arctan2(xyz[:, 1], xyz[:, 0])
    return ptsnew


# setup plot
a = plt.figure().add_subplot(111, projection='3d')


# Function to create slices for for example for quarter peony


def azimuth_slices(samples=500, slices=4, ghost_value=0):
    sphere = appendSpherical_np(fibonacci_sphere(samples))
    f3d_array = []
    for i in range(1, slices+1):
        angle_min = (2*(i-1)*math.pi/slices)-math.pi
        angle_max = (2*(i)*math.pi/slices)-math.pi
        part_sphere = sphere[np.argwhere(
            (sphere[:, 5] > angle_min) & (sphere[:, 5] < angle_max)), :]
        a.scatter(part_sphere[:, :, 0],
                  part_sphere[:, :, 1], part_sphere[:, :, 2])
        f3d_partial_array = np.hstack([part_sphere[:, :, 0], part_sphere[:, :, 1],
                                       part_sphere[:, :, 2], (i-1)*ghost_value*np.ones_like(part_sphere[:, :, 2])])
        f3d_array.append(f3d_partial_array.tolist())
    return(f3d_array)

# Function to create bands


def cartesian_bands(samples=500, bands=4, ghost_value=0):
    sphere = appendSpherical_np(fibonacci_sphere(samples))
    f3d_array = []
    for i in range(0, bands):
        band_size = 2/bands
        band_min = band_size*i-1
        band_max = band_size*(i+1)-1
        part_sphere = sphere[np.argwhere(
            (sphere[:, 1] > band_min) & (sphere[:, 1] < band_max)), :]
        a.scatter(part_sphere[:, :, 0],
                  part_sphere[:, :, 1], part_sphere[:, :, 2])
        f3d_partial_array = np.hstack([part_sphere[:, :, 0], part_sphere[:, :, 1],
                                       part_sphere[:, :, 2], i*ghost_value*np.ones_like(part_sphere[:, :, 2])])
        f3d_array.append(f3d_partial_array.tolist())
    return(f3d_array)

# 6 sections on a peony


def six_sections(samples=500, ghost_value=0):
    sphere = appendSpherical_np(fibonacci_sphere(samples))
    f3d_array = []
    part1 = sphere[np.argwhere((sphere[:, 4] < math.pi/4) &
                               (-math.pi < sphere[:, 5]) & (sphere[:, 5] < math.pi)), :]
    part2 = sphere[np.argwhere((math.pi/4 < sphere[:, 4]) & (sphere[:, 4] < 3*math.pi/4)
                               & (-math.pi < sphere[:, 5]) & (sphere[:, 5] < -math.pi/2)), :]
    part3 = sphere[np.argwhere((math.pi/4 < sphere[:, 4]) & (sphere[:, 4]
                                                             < 3*math.pi/4) & (-math.pi/2 < sphere[:, 5]) & (sphere[:, 5] < 0)), :]
    part4 = sphere[np.argwhere((math.pi/4 < sphere[:, 4]) & (sphere[:, 4]
                                                             < 3*math.pi/4) & (0 < sphere[:, 5]) & (sphere[:, 5] < math.pi/2)), :]
    part5 = sphere[np.argwhere((math.pi/4 < sphere[:, 4]) & (sphere[:, 4] < 3*math.pi/4)
                               & (math.pi/2 < sphere[:, 5]) & (sphere[:, 5] < math.pi)), :]
    part6 = sphere[np.argwhere((sphere[:, 4] > 3*math.pi/4) & (sphere[:, 4]
                                                               < math.pi) & (-math.pi < sphere[:, 5]) & (sphere[:, 5] < math.pi)), :]
    all_parts = [part1, part2, part3, part4, part5, part6]
    for idx, part in enumerate(all_parts):
        a.scatter(part[:, :, 0], part[:, :, 1], part[:, :, 2])
        f3d_partial_array = np.hstack(
            [part[:, :, 0], part[:, :, 1], part[:, :, 2], idx*ghost_value*np.ones_like(part[:, :, 2])])
        f3d_array.append(f3d_partial_array.tolist())
    return(f3d_array)


def parallel_rings(samples=100, rings=2, angle=20, ghost=0):
    stars_in_ring = int(np.ceil(samples))
    split_angle = (angle*math.pi/180)/2
    f3d_array = []
    for idx, r in enumerate(np.linspace(-1, 1, rings)):
        ring_array = []
        for i in range(0, stars_in_ring-1):
            x = math.sin(math.pi/2+r*split_angle) * \
                math.cos(i*(2*math.pi)/stars_in_ring)
            y = math.sin(math.pi/2+r*split_angle) * \
                math.sin(i*(2*math.pi)/stars_in_ring)
            z = math.cos(math.pi/2+r*split_angle)
            ghost_value = idx*ghost
            ring_array.append([x, y, z, ghost_value])
        ring_array = np.array(ring_array)
        a.scatter(ring_array[:, 0], ring_array[:, 1], ring_array[:, 2])
        f3d_array.append(ring_array.tolist())
    a.set_xlim([-1, 1])
    a.set_ylim([-1, 1])
    a.set_zlim([-1, 1])
    return(f3d_array)