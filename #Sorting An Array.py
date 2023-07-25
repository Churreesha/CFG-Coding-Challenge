#Sorting An Array
#Bubble Sort Method
# Define a function to sort an array using bubble sort
def bubble_sort(array):
    # Get the length of the array
    n = len(array)
    # Loop through the array n - 1 times
    for i in range(n - 1):
        # Loop through the array from 0 to n - i - 1
        for j in range(n - i - 1):
            # If the current element is greater than the next element, swap them
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    # Return the sorted array
    return array

# Test the function with an example
array = [1, 4, 5, 66, 3, 84, 11, 198]
sorted_array = bubble_sort(array)
print(sorted_array) 