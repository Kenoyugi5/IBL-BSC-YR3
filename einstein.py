
# `constant = pow(300000000, 2)` is calculating the square of the speed of light in meters per second
# (300,000,000 m/s) and assigning it to the variable `constant`.
constant = pow(300000000, 2)
speed = constant
mass = input("Enter Mass in Kilograms: ")
# `energy = int(mass)*speed` is calculating the energy in joules by multiplying the mass entered by
# the user (converted to an integer using `int()`) with the square of the speed of light (assigned to
# the variable `speed`). This calculation is based on Einstein's famous equation E=mc^2, where E
# represents energy, m represents mass, and c represents the speed of light.
energy = int(mass)*speed
print("Energy in Joules= {}" .format(energy))