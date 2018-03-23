def bubble_sort(arr):
    """
    Implementation of bubble sort algorithm.
    """
    for i in range(len(arr)):
        sort_upto = len(arr)-i
        print("array is :", arr, "\n")
        for j in range(1,sort_upto):
                if arr[j-1] > arr[j]:
                    temp = arr[j-1]
                    arr[j-1] = arr[j]
                    arr[j] = temp
    return arr

def selection_sort(arr):
    """
    Implementation of selection sort algorithm.
    """
    for i in range(len(arr)):
        min_index = i
        print(arr,"\n")
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    return arr

def insertion_sort(arr):
    """
    Implementation of insertion sort algorithm.
    """
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr
