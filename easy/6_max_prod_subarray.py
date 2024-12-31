# Subarrays are contiguous not discrete i,e elements must be asjacent to each other

class MaxProdSubarray():
    def __init__(self,arr):
        self.arr = arr


    def brute_force(self):
        '''
        Run a loop to find the start of the subarrays.
        Run another nested loop
        Multiply each element and store the maximum value of all the subarray.
        
        Time Complexity:  O(N*N), Because we are traversing the whole array again and again for every integer.
        Space Complexity: O(1), Since, we are not using any extra space.

        '''
        max_prod = float('-inf')
        i_start = 0
        j_end = 0
        for i in range(len(self.arr)):
            prod = 1
            for j in range(i, len(self.arr)):
                prod *= self.arr[j]
                # max_prod = max(max_prod, prod)
                if prod > max_prod:
                    max_prod = prod
                    i_start = i
                    j_end = j
        return max_prod, [i_start, j_end]
    
    def observation(self):
        '''
        We will first declare 2 variables i.e. ‘pre’(stores the product of the prefix subarray) and ‘suff’
        (stores the product of the suffix subarray). They both will be initialized with 1(as we want to store
          the product).
        Now, we will use a loop(say i) that will run from 0 to n-1.
        We have to check 2 cases to handle the presence of 0:
        If pre = 0: This means the previous element was 0. So, we will consider the current element as a part of
          the new subarray. So, we will set ‘pre’ to 1.
        If suff = 0: This means the previous element was 0 in the suffix. So, we will consider the current 
        element as a part of the new suffix subarray. So, we will set ‘suff’ to 1.
        Next, we will multiply the elements from the starting index with ‘pre’ and the elements from the end
          with ‘suff’. To incorporate both cases inside a single loop, we will do the following:
        We will multiply arr[i] with ‘pre’ i.e. pre *= arr[i].
        We will multiply arr[n-i-1] with ‘suff’ i.e. suff *= arr[n-i-1].
        After each iteration, we will consider the maximum among the previous answer, ‘pre’ and ‘suff’ i.e. 
        max(previous_answer, pre, suff).
        Finally, we will return the maximum product.

        Time Complexity: O(N), N = size of the given array.
        Reason: We are using a single loop that runs for N times.
        Space Complexity: O(1) as No extra data structures are used for computation.
        '''
        n = len(self.arr)

        pref, suff = 1,1
        max_prod = float('-inf')
        for i in range(n):
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1
            pref *= self.arr[i]
            suff *= self.arr[n-i-1]
            max_prod = max(max_prod, pref, suff)

        return max_prod
    

if __name__ == "__main__":
    nums = [1, 2, -4, 0, -3, -5, -6, -7]
    max_prod_subarray = MaxProdSubarray(nums)
    # max_prod, index = max_prod_subarray.brute_force()
    # print(f"Maximum product subarray is {max_prod} and its indices are {index[0]} to {index[1]}")
    max_prod = max_prod_subarray.observation()
    print(f"Maximum product subarray is {max_prod}")
