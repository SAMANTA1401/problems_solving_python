def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1 
            print("3",arr)

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1  
            print("1",arr)

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            print("2",arr)
        
    return arr 


if __name__ == "__main__":

    arr = [4,45,7,23,4,73,7,4,3,1]
    print(merge_sort(arr))
    # O(n*logn)