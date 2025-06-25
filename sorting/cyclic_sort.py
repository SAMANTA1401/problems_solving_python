def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    return arr


if __name__ == "__main__":
    arr = [4,45,7,23,4,73,7,4,3,1]
    print("x")
    print(cyclic_sort(arr))
     # O(n)