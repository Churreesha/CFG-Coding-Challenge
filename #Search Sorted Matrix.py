#Search Sorted Matrix
# Define a function to search a number in a sorted matrix
def search_matrix(matrix, target):
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Initialize the left and right pointers for binary search
        left = 0
        right = len(matrix[i]) - 1
        # Repeat while left <= right
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            # If the middle element is equal to the target, return its location
            if matrix[i][mid] == target:
                return [i, mid]
            # If the middle element is greater than the target, move the right pointer to the left of the middle
            elif matrix[i][mid] > target:
                right = mid - 1
            # If the middle element is less than the target, move the left pointer to the right of the middle
            else:
                left = mid + 1
    # If the target is not found in any row, return -1
    return -1

# Test the function with an example
matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]
target = 44
result = search_matrix(matrix, target)
print(result) 