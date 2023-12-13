"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


length = float(input("Foundation length (m): "))
width = float(input("Foundation width (m): "))
height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
cost_concrete = float(input("Cost of concrete ($/m^3): "))
cost_bricks = float(input("Cost of bricks ($/m^2): "))

concrete_volume_foundation = length * \
    width * height

wall_area = 2 * (length * wall_height + width * wall_height)
bricks_area = wall_area
bricks_needed = bricks_area

concrete_cost = concrete_volume_foundation * cost_concrete
bricks_cost = bricks_needed * cost_bricks
total_cost = concrete_cost + bricks_cost

print("Concrete needed for foundation (m^3): {:.2f}".format(
    concrete_volume_foundation))
print("Cost of concrete: ${:,.2f}".format(concrete_cost))
print("Bricks needed for walls (m^2): {:.2f}".format(bricks_needed))
print("Cost of bricks: ${:,.2f}".format(bricks_cost))
print("Total cost: ${:,.2f}".format(total_cost))
