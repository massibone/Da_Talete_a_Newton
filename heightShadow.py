import math

# Taking inputs from the user
length_of_shadow = float(input("Enter the length of shadow in meters: "))
angle_of_elevation = float(input("Enter the angle of elevation in degrees: "))

# Converting degrees to radians
theta = math.radians(angle_of_elevation)

# Calculating height of the building
height_of_building = length_of_shadow * math.tan(theta)

# Output the result
print("The height of the building is {:.2f} meters".format(height_of_building))