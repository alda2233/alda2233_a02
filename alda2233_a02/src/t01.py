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


TAX_RATE = 18.5 / 100  # Tax rate as a constant
total_sales = float(input("Enter the total sales: $"))
annual_tax = total_sales * TAX_RATE
# Print the projected tax report
print("\nProjected Tax Report")
print("--------------------------")
print(f"Total sales:   $ {total_sales:,.2f}")
print(f"Annual tax:    % {TAX_RATE * 100:.2f}")
print("--------------------------")
print(f"Tax:           $ {annual_tax:,.2f}")
