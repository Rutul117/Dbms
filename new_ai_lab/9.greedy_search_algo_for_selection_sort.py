def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)

    selection_sort(arr)

    print("Sorted array:", arr)
