def insertion_sort(arr):
    for i in range(len(arr)-1):
        j = i+1
        while (j>0):
            if arr[j]< arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j = j -1
            else:
                break
    return arr


if __name__ == "__main__":

    arr = [4,45,7,23,4,73,7,4,3,1]
    print(insertion_sort(arr))
     # O(n^2)