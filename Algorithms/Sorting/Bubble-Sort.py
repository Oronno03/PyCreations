def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    print("Unsorted Array:")
    print(data)
    bubble_sort(data)
    print("Sorted Array:")
    print(data)
