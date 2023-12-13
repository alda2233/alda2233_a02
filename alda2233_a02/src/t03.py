"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-10-06"
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


date = int(input("Enter a date in the format YYYYMMDD: "))
year = date // 10000
month = (date % 10000) // 100
day = date % 100

print(f"The reformatted date: {year}/{month:02d}/{day:02d}")
