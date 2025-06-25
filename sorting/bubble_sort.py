def bubble_sort(arr):
    swapped = False
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                swapped = True
        if swapped == False:
            break

    return arr

if __name__ == "__main__":

    arr = [4,45,7,23,4,73,7,4,3,1]
    print(bubble_sort(arr))
    # O(n^2)