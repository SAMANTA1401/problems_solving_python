def binary_search(arr,target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + (right-left))//2

        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            left = mid +1 
        else:
            right = mid -1

    return -1

if __name__ == "__main__":
    arr = [34,46,57,32,786,56]
    target = 786
    print(binary_search(arr,target))