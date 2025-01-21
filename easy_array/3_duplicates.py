class Duplicate():
    def __init__(self, nums):
        self.nums = nums
        

    def brute_force(self):
        '''
        we can easily find any duplicate in the array just by using two nested loops. 
        The first loop will pick integers one by one from the array and the second nested loop will 
        check if there exists any duplicate or not.

        Time Complexity:  O(N*N), Because we are traversing the whole array again and again for every integer.
        Space Complexity: O(1), Since, we are not using any extra space.

        '''
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] == self.nums[j]:
                    return nums[j]
        return False
    
    def adjacent(self):
        '''
        We can also solve this problem by sorting the array. After that, we can easily find the duplicate in the array.

        Time Complexity: O(N * logN), Because we are sorting the array.
        Space Complexity: O(1), Since, we are not using any extra space.

        '''
        nums = sorted(self.nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
        return False
    
    def hash_set(self):
        '''
        we can use any data structure like HashSet, HashTable, or ArrayList as almost all data structures 
        have a predefined function that checks if there already exists a given integer or not.

        Time Complexity:  O(N*logN), Sorting takes N*logN. Times where N is the length of the array
        Space Complexity: O(1), Since we are not using any extra space. If we are not counting extra space taken by sorting.
        '''
        hash_set = set()
        for num in self.nums:
            if num in hash_set:
                return num
            hash_set.add(num)


if __name__ == '__main__':
    nums = [1, 2, 3, 1] 
    duplicate = Duplicate(nums)
    print(f'duplicate element is {duplicate.brute_force()}')  # Output: 1
    print(f'duplicate element is {duplicate.adjacent()}')  # Output: 1
    print(f'duplicate element is {duplicate.hash_set()}')  # Output: 1
 