def selection_sort(arr):
    for i in range(len(arr) - 1):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]


if __name__ == "__main__":
    data = [64, 25, -12, 22, 11]
    print("Unsorted Array:")
    print(data)
    selection_sort(data)
    print("Sorted Array:")
    print(data)
