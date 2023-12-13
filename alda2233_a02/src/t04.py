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


flyers = int(input("Number of flyers: "))
people = int(input("Number of delivery people: "))

flyers_per_person = flyers // people
left_over = flyers % people

print("Flyers per delivery person:", flyers_per_person)
print("Flyers left over:", left_over)
