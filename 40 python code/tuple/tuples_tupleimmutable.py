# Example tuple
my_tuple = (1, 2, 3)

# Trying to modify an element (this will raise an error)
try:
    my_tuple[0] = 10
except TypeError as e:
    print('Error:', e)