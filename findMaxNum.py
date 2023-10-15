def findMaxNum(x, y, z):
    # Check if it's possible to reach y from x in z steps
    if abs(y - x) > z:
        return -1 
    # Return the maximum of x and y
    return max(x, y) 

# Sample Input For Testing
x = 8
y = 5
z = 3

# Function Call
result = findMaxNum(x, y, z)
print(f'The maximum value obtained from x while converting x to y in at most z steps: {result}')
