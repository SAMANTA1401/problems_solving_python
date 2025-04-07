class MinRotSortArr():
    def __init__(self, arr):
        self.arr = arr

    def brute_force(self):
        '''
        Time Complexity: O(N), N = size of the given array.
        Reason: We have to iterate through the entire array to check if the target is present in the array.
        Space Complexity: O(1)
        Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
        '''
        
        mini = float('inf') 
        n = len(self.arr)  # size of the array.
        for i in range(n):
            # Always keep the minimum.
            mini = min(mini, self.arr[i])
        return mini
    
    def binary_search(self):
        '''
        Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this:
        low will point to the first index and high will point to the last index.
        Calculate the ‘mid’: Now, inside a loop, we will calculate the value of ‘mid’ using the following
        formula:
        mid = (low+high) // 2 ( ‘//’ refers to integer division)
        Identify the sorted half, and after picking the leftmost element, eliminate that half.
        If arr[low] <= arr[mid]: This condition ensures that the left part is sorted. So, we will pick the
        leftmost element i.e. arr[low]. Now, we will compare it with 'ans' and update 'ans' with the smaller 
        value (i.e., min(ans, arr[low])). Now, we will eliminate this left half(i.e. low = mid+1).
        Otherwise, if the right half is sorted:  This condition ensures that the right half is sorted. So, we
        will pick the leftmost element i.e. arr[mid]. Now, we will compare it with 'ans' and update 'ans' with
        the smaller value (i.e., min(ans, arr[mid])). Now, we will eliminate this right 
        alf(i.e. high = mid-1).
        This process will be inside a loop and the loop will continue until low crosses high. Finally, 
        we will return the ‘ans’ variable that stores the minimum element

        Time Complexity: O(logN), N = size of the given array.
        Reason: We are basically using binary search to find the minimum.
        Space Complexity: O(1)
        Reason: We have not used any extra data structures, this makes space complexity, even in the worst 
        case as O(1).
        '''

        low = 0
        high = len(self.arr) - 1
        ans = float('inf') 
        # Binary search for the smallest element.
        while low <= high:
            mid = (low + high) // 2
            # If left half is sorted.
            if self.arr[low] <= self.arr[mid]:
                # Keep the minimum.
                ans = min(ans, self.arr[low])
                # Eliminate the left half.
                low = mid + 1
            # If right half is sorted.
            else:
                # Keep the minimum.
                ans = min(ans, self.arr[mid])
                # Eliminate the right half.
                high = mid - 1
                # Reduce the search space.
        return ans



if __name__ == "__main__":
    sort_arr = [0, 1, 2, 3, 4, 5, 6, 7]  
    rot_arr = [4, 5, 6, 7, 0, 1, 2, 3] # rotation at index 3
    findmin = MinRotSortArr(rot_arr)
    ans = findmin.brute_force()
    print("The minimum element is:", ans)

