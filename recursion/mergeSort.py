def merge(arr, start, mid, end, temp):
    left = mid - start + 1
    right = end - mid

    for i in range(left):
        temp[i] = arr[i + start]

    for i in range(right):
        temp[i + left] = arr[i + mid + 1]

    l, r, a = 0, left, start

    # merge the arrays
    while l < left and r < (left + right):
        if temp[l] < temp[r]:
            arr[a] = temp[l]
            l += 1
        else:
            arr[a] = temp[r]
            r += 1
        a += 1

    # copy the remaining elements from both sides
    while l < left:
        arr[a] = temp[l]
        l += 1
        a += 1

    while r < (right + left):
        arr[a] = temp[r]
        r += 1
        a += 1


def merge_sort(arr, start, end, temp):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid, temp)
    merge_sort(arr, mid + 1, end, temp)
    merge(arr, start, mid, end, temp)


# Example usage
arr = [6, 3, 5, 1, 4, 8, 2, 7]
N = len(arr)
temp = [0] * N
print("Initial array:", arr)
merge_sort(arr, 0, N - 1, temp)
print("Sorted array:", arr)