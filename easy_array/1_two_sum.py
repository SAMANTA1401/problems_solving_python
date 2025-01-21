class TwoSums:
    def __init__(self, nums, target ):
        self.nums = nums
        self.target = target
    
    def brute_force(self):
        '''
        First, we will use a loop(say i) to select the indices of the array one by one.
        For every index i, we will traverse through the remaining array using another loop(say j) 
        to find the other number such that the sum is equal to the target (i.e. arr[i] + arr[j] = target).

        Time complexity : O(n^2) where n = number of elements
        Space complexity : O(1) as we are not using any extra space
        '''
        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j]
                
    def hashing(self):
        '''
        We will select the element of the array one by one using a loop(say i).
        Then we will check if the other required element(i.e. target-arr[i]) exists in the hashMap.
        If that element exists, then we will return “YES” for the first variant or we will return the 
        current index i.e. i, and the index of the element found using map i.e. mp[target-arr[i]].
        If that element does not exist, then we will just store the current element in the hashMap along 
        with its index. Because in the future, the current element might be a part of our answer.

        Time complexity : O(n) where n = number of elements
        Note: In the worst case(which rarely happens), the unordered_map takes O(N) to find an element. 
        In that case, the time complexity will be O(N^2). If we use map instead of unordered_map, the time 
        complexity will be O(N* logN) as the map data structure takes logN time to find an element.
        Space complexity : O(n) as we are using extra space for the hashMap
        '''
        hashMap = {} # Dictionary
        for i in range(len(self.nums)):
            if self.target - self.nums[i] in hashMap:
                return [hashMap[self.target - self.nums[i]], i]
            hashMap[self.nums[i]] = i



    def two_pointer(self):
        '''
        We will first sort the array using the sort function.
        Then we will use two pointers, one at the beginning and one at the end of the array.
        We will keep on incrementing the left pointer and decrementing the right pointer until we find the
        required pair.

        Time complexity : O(nlogn) + O(n) where n = number of elements (sorting + loop) 
        Space complexity : O(n) as we are not using any extra space for soted array elements
        if we store sorted array elements in same variable then no extra space is needed then space complexity
        will be O(1)
        '''
        nums_sort = sorted(self.nums)
        left = 0
        right = len(nums_sort) - 1
        while left < right: # upto pointer crossing
            if nums_sort[left] + nums_sort[right] == self.target:
                return [nums.index(nums_sort[left]), nums.index(nums_sort[right])]
            elif nums_sort[left] + nums_sort[right] < self.target:
                left += 1
            else:
                right -= 1
        


if __name__ == "__main__":
    nums = [2,11,7,15]
    target = 9
    two_sums = TwoSums(nums, target)
    # result = two_sums.brute_force()
    # result = two_sums.hashing()
    result = two_sums.two_pointer()
    print(f"Indices of two numbers that sum up to {target} are: {result}")