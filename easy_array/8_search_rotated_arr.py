

class SearchRotSortArr():
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
        
    def brute_force(self):
        '''Time Complexity: O(N), N = size of the given array.
            Reason: We have to iterate through the entire array to check if the target is present in the array.

            Space Complexity: O(1)
            Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
        
        '''
        for i in range(len(self.arr)):
            if self.arr[i] == self.k:
                return i
        return -1
    
    def binary_search(self):
        '''
        Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index, and high will point to the last index.
        Calculate the ‘mid’: Now, inside a loop, we will calculate the value of ‘mid’ using the following formula:
        mid = (low+high) // 2 ( ‘//’ refers to integer division)
        Check if arr[mid] == target: If it is, return the index mid.
        Identify the sorted half, check where the target is located, and then eliminate one half accordingly:
        If arr[low] <= arr[mid]: This condition ensures that the left part is sorted.
        If arr[low] <= target && target <= arr[mid]: It signifies that the target is in this sorted half. So, we will eliminate the right half (high = mid-1).
        Otherwise, the target does not exist in the sorted half. So, we will eliminate this left half by doing low = mid+1.
        Otherwise, if the right half is sorted:
        If arr[mid] <= target && target <= arr[high]: It signifies that the target is in this sorted right half. So, we will eliminate the left half (low = mid+1).
        Otherwise, the target does not exist in this sorted half. So, we will eliminate this right half by doing high = mid-1.
        Once, the ‘mid’ points to the target, the index will be returned.
        This process will be inside a loop and the loop will continue until low crosses high. If no index is found, we will return -1.
        
        Time Complexity: O(logN), N = size of the given array.
            Reason: We are using binary search to search the target.

            Space Complexity: O(1)
            Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
        '''
        low = 0
        high = len(self.arr)-1
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.arr[mid] == self.k:
                return mid
            # If left part is sorted.
            if self.arr[low] <= self.arr[mid]:
                if self.arr[low] <= self.k and self.k <= self.arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # If right part is sorted.
            else:
                if self.arr[mid] <= self.k and self.k <= self.arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    # return -1
            
        return -1
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    search = SearchRotSortArr(arr, k)
    # ans = search.brute_force()
    ans = search.binary_search()
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)