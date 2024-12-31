# Subarrays are contiguous not discrete i,e elements must be asjacent to each other

class MaxSubArray:
    def __init__(self, arr):
        self.arr = arr

    def brute_force(self):
        '''
        First, we will run a loop(say i) that will select every possible starting index of the subarray. 
        The possible starting indices can vary from index 0 to index n-1(n = array size).
        Inside the loop, we will run another loop(say j) that will signify the ending index as well as the
        current element of the subarray. For every subarray starting from index i, the possible ending 
        index can vary from index i to n-1(n = size of the array).
        Inside loop j, we will add the current element to the sum of the previous subarray i.e. 
        sum = sum + arr[j]. Among all the sums the maximum one will be the answer.

        Time Complexity: O(N^2), where N = size of the array.
        Reason: We are using 2 nested loops, each running approximately N times.
        Space Complexity: O(1) as we are not using any extra space.
        '''
        max_sum = float('-inf')
        i_start = 0
        j_end = 0
        for i in range(len(self.arr)): # for starting index 
            current_sum = 0
            for j in range(i, len(self.arr)): # for ending index
                current_sum += self.arr[j]
                # max_sum = max(max_sum, current_sum)
                if current_sum > max_sum:
                    max_sum = current_sum
                    i_start = i
                    j_end = j
        return max_sum , [i_start, j_end]
    
    def kadane(self):
        '''
        We will run a loop(say i) to iterate the given array.
        Now, while iterating we will add the elements to the sum variable and consider the maximum one.
        If at any point the sum becomes negative we will set the sum to 0 as we are not going to consider it as a part of our answer.
        
        Time Complexity: O(N), where N = size of the array.
        Reason: We are using a single loop running N times.
        Space Complexity: O(1) as we are not using any extra space.
        '''
        max_sum = float('-inf')
        current_sum = 0
        for num in self.arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    

if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    max_sub_array = MaxSubArray(arr)
    # mx_sum, index = max_sub_array.brute_force()
    # print(f'max sum of subarray :{ mx_sum} and array index {index[0]} to {index[1]}' )
    mx_sum = max_sub_array.kadane()
    print(f'max sum of subarray :{ mx_sum}' )
    
