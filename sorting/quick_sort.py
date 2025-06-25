
def sort(arr, low, high):
    if low >= high:
        return 
    
    s, e = low, high # two pointer
    mid = int(s + (e-s)/2)
    p = arr[mid]  # pivot point
    # while the start is less than or equal to the end
    while s <= e:
        # if the array is sorted, it won't swap
        # i.e the the left half is already sorted
        while arr[s] < p:
            s += 1
        # same for the other half
        while arr[e] > p:
            e -= 1

        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1

    sort(arr, low, e)
    sort(arr, s, high)


def quick_sort(nums):
        sort(nums, 0, len(nums) - 1)
        return nums

if __name__ == "__main__":
    arr = [4,45,7,23,4,73,7,4,3,1]
    print(quick_sort(arr))
    # O(n*logn)











def quick_sort(arr):
    """Quick sort is a divide-and-conquer algorithm that sorts an array by choosing a
    “pivot” element and partitioning the other elements into two sub-arrays, according
    to whether they are less than or greater than the pivot"""
    sort(arr, 0, len(arr) - 1)
    
    pass





if __name__ == "__main__":
    arr = [4,45,7,23,4,73,7,4,3,1]
    print(quick_sort(arr))
    # O(n*logn)