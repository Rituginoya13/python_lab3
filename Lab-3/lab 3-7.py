def insertion_sort(arr):
 for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
 return arr
elements = [12, 11, 13, 5, 6]
sorted_elements = insertion_sort(elements)
print("Sorted Elements:", sorted_elements)
