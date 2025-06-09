def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 15

index = binary_search(array, target)

if index != -1:
    print(f"The value {target} was found at index:  {index}")
else:
    print("The target value was not found")
