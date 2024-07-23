# Create a function that returns true if the first array
# can be nested inside the second and false otherwise.

# arr1 can be nested inside arr2 if:

#    1 arr1's min is greater than arr2's min.
#    2 arr1's max is less than arr2's max.

# Examples

# canNest([1, 2, 3, 4], [0, 6]) ➞ true

# canNest([3, 1], [4, 0]) ➞ true

# canNest([9, 9, 8], [8, 9]) ➞ false

# canNest([1, 2, 3, 4], [2, 3]) ➞ false


def canNest(arr1, arr2 ): 
	x = min(arr1)
	y = min(arr2)
	z = max(arr1)
	n = max(arr2)
	if(x > y and z < n):
		return True
	else:
		return False
print(canNest([1, 2, 3, 4], [0, 6]))



def canNest(arr1, arr2):
    # Get the minimum and maximum values of both arrays
    min1, max1 = min(arr1), max(arr1)
    min2, max2 = min(arr2), max(arr2)
    
    # Check the conditions for nesting
    if min1 > min2 and max1 < max2:
        return True
    else:
        return False

# Test cases
print(canNest([1, 2, 3, 4], [0, 6]))  # ➞ true
print(canNest([3, 1], [4, 0]))        # ➞ true
print(canNest([9, 9, 8], [8, 9]))     # ➞ false
print(canNest([1, 2, 3, 4], [2, 3]))  # ➞ false
