import time


import patterns

# Regarding the JSON output
# A break pattern is a list of subpatterns.
# A subpattern is a list of stars.
# A star is a list of 4 numbers.
# Each star is a 4-tuple list.  [x,y,z,ghost_time_offset].
# The sub patterns are used for different colors etc, one for each potential child star definition



# The UI.


def user_input():
    shape_wanted = int(input(
        "Select shape (1 = Azimuth Slices(like an orange), 2 = cartesian bands, 3 = 6 sections (like on a dice)), 4 = Parallel Rings): "))

    if shape_wanted == 1:
        stars_wanted = int(input("How many stars do you want?(4in/100mm normal = 120, 4in/100mm dense = 240, 5in/125mm normal = 140, 5in/125mm dense = 280, 6in/150mm normal = 160, 6in/150mm dense = 320), 7in/175mm normal = 180, 7in/175mm dense = 360: "))
        slices_wanted = int(
            input("How many azimuth slices do you want?(Quarter peony = 4): "))
        ghost_wanted = float(input(
            "What ghost offset do you want? (normal shell = 0, (try 0.2 for ghost)): "))
        print("Copy this JSON list of lists into the custom JSON field in F3D: ")
        print(patterns.azimuth_slices(stars_wanted, slices_wanted, ghost_wanted))
    elif shape_wanted == 2:
        stars_wanted = int(input("How many stars do you want?(4in/100mm normal = 120, 4in/100mm dense = 240, 5in/125mm normal = 140, 5in/125mm dense = 280, 6in/150mm normal = 160, 6in/150mm dense = 320), 7in/175mm normal = 180, 7in/175mm dense = 360: "))
        bands_wanted = int(input("How many bands do you want?: "))
        ghost_wanted = float(input(
            "What ghost offset do you want? (normal shell = 0, (try 0.2 for ghost)): "))
        print("Copy this JSON list of lists into the custom JSON field in F3D: ")
        print(patterns.cartesian_bands(stars_wanted, bands_wanted, ghost_wanted))
    elif shape_wanted == 3:
        stars_wanted = int(input("How many stars do you want?(4in/100mm normal = 120, 4in/100mm dense = 240, 5in/125mm normal = 140, 5in/125mm dense = 280, 6in/150mm normal = 160, 6in/150mm dense = 320), 7in/175mm normal = 180, 7in/175mm dense = 360: "))
        ghost_wanted = float(input(
            "What ghost offset do you want? (normal shell = 0, (try 0.2 for ghost)): "))
        print("Copy this JSON list of lists into the custom JSON field in F3D: ")
        print(patterns.six_sections(stars_wanted, ghost_wanted))
    elif shape_wanted == 4:
        stars_wanted = int(input("How many stars do you want per ring?(4in/100mm normal = 60, 4in/100mm dense = 120, 5in/125mm normal = 70, 5in/125mm dense = 140, 6in/150mm normal = 80, 6in/150mm dense = 160), 7in/175mm normal = 90, 7in/175mm dense = 180: "))
        rings_wanted = int(input("How many rings do you want?"))
        angle_wanted = int(
            input("What angle do you want between the end rings?"))
        ghost_wanted = float(input(
            "What ghost offset do you want? (normal shell = 0, (try 0.2 for ghost)): "))
        print("Copy this JSON list of lists into the custom JSON field in F3D: ")
        print(patterns.parallel_rings(stars_wanted, rings_wanted, angle_wanted, ghost_wanted))
    else:
        print("Not supported input, you must select input by writing tha corresponding number.")
        time.sleep(1)
        user_input()


# azimuth_slices()
# cartesian_bands()
# six_sections()
# parallel_rings()
user_input()

plt.show()
