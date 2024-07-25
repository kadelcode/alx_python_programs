def magic_calculation(a, b):
    # Importing functions add and sub
    from magic_calculation_102 import add, sub

    # If a is less than b
    if a < b:
        # Add a and b, store in c
        c = add(a, b)
        # Loop over range(4, 6)
        for i in range(4, 6):
            # Add c and i
            c = add(c, i)
        # Return c
        return c

    else:
        # Return subtracted result
        return sub(a, b)
