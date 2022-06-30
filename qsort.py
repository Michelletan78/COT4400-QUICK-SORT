# COT 4400:Design and Analysis of Algorithms  Course project 1
# # This function takes last element as pivot
# the pivot element at its correct position in sorted
# left array, elements all smaller  than pivot
# right array  all elements greater than pivot

import random


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above


arr = [10, 80, 3, 19, 14, 7, 5, 12]
print("Array of orignal sequences is: ", arr)
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:", arr)
