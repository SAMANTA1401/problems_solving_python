

class MissingNumber:
    def __init__(self, arr):
        self.arr = arr
        
    def brute_force(self):
        '''We will run a loop(say i) from 1 to N.
            For each integer, i, we will try to find it in the given array using linear search.
            For that, we will run another loop to iterate over the array and consider a flag variable to indicate if the element exists in the array.
            Flag = 1 means the element is present and flag = 0 means the element is missing.
            Initially, the flag value will be set to 0. While iterating the array, if we find the element, we will set the flag to 1 and 
            break out from the loop.
            Now, for any number i, if we cannot find it, the flag will remain 0 even after iterating the whole array and we will return 
            the number.

            Time Complexity: O(N^2), where N = size of the array+1.
            Reason: In the worst case i.e. if the missing number is N itself, the outer loop will run for N times, and for every single
            number the inner loop will also run for approximately N times. So, the total time complexity will be O(N2).

            Space Complexity: O(1)  as we are not using any extra space.
        '''
        # Outer loop that runs from 1 to N:
        for i in range(1, len(self.arr) + 2):
        # flag variable to check if an element exists
            flag = 0
            
            # Search the element using linear search:
            for j in range(len(self.arr)):
                if self.arr[j] == i:
                    # i is present in the array:
                    flag = 1
                    break
            # check if the element is missing (i.e., flag == 0):
            if flag == 0:
                return i

        # The following line will never execute.
        # It is just to avoid warnings.
        return -1
    
    
    def hashing(self):
        '''The range of the number is 1 to N. So, we need a hash array of size N+1 (as we want to store the 
        frequency of N as well).
            Now, for each element in the given array, we will store the frequency in the hash array.
            After that, for each number between 1 to N, we will check the frequencies. And for any number, 
            if the frequency is 0, we will return it.
            
            Time Complexity: O(N) + O(N) ~ O(2*N),  where N = size of the array+1.
            Reason: For storing the frequencies in the hash array, the program takes O(N) time complexity and for 
            checking the frequencies in the second step again O(N) is required. So, the total time complexity is 
            O(N) + O(N).

            Space Complexity: O(N), where N = size of the array+1. Here we are using an extra hash array of size N+1.
        '''
        hash = [0] * (len(self.arr) + 2)  # [0, 0, 0, 0, 0, 0] hash array present no of elements + missing elements 
        # storing the frequencies:          [0, 1, 2, 3, 4, 5]
        for i in range(len(self.arr)):  #   [0, 1, 1, 0, 1, 1]
            hash[self.arr[i]] += 1 # if present value will be replaced 0 to 1
        # checking the frequencies for numbers 1 to N:
        for i in range(1,len(self.arr)+2):
            if hash[i] == 0:
                return i
            
        return -1
    
    def summation(self):
        '''We will first calculate the summation of first N natural numbers(i.e. 1 to N) using the specified formula.
            Then we will add all the array elements using a loop.
            Finally, we will consider the difference between the summation of the first N natural numbers and the sum of the array elements.
            
            Time Complexity: O(N), where N = size of array+1.
            Reason: Here, we need only 1 loop to get the sum of the array elements. The loop runs for approx. N times. So, the time complexity is O(N).

            Space Complexity: O(1) as we are not using any extra space.
        '''
        # summation of first N elements
        summation = ((len(self.arr) + 1) * (len(self.arr)+2)) // 2
        # summation of all array elements
        s2 = sum(self.arr) # one loop O(n)
        missing_number = summation - s2
        return missing_number
        
    def xor(self): # binary operation 1 xor 1 = 0 ; 0 xor 0 = 1; 1 xor 0 = 1 ; 0 xor 1 = 1
        '''Assume the given array is: {1, 2, 4, 5} and N = 5.
            XOR of (1 to 5) i.e. xor1 = (1^2^3^4^5)
            XOR of array elements i.e. xor2 = (1^2^4^5)
            XOR of xor1 and xor2 = (1^2^3^4^5) ^ (1^2^4^5)
                        = (1^1)^(2^2)^(3)^(4^4)^(5^5)
                        = 0^0^3^0^0 = 0^3 = 3.
            The missing number is 3.
            
            Time Complexity: O(N), where N = size of array+1.
            Reason: Here, we need only 1 loop to calculate the XOR. The loop runs for approx. N times. So, the time complexity is O(N).

            Space Complexity: O(1) as we are not using any extra space.
        '''
        xor1 = 0
        xor2 = 0
        
        for i in range(len(self.arr)):
            xor2 =  xor2 ^ self.arr[i] # 4 arr elements 3 times xor (i=0 to 3)
            xor1 = xor1 ^ (i + 1) # 5 elements 4 times xor including missing number (1 to 4)
        
        xor1 = xor1 ^ (len(self.arr) + 1) # 5 elements 4 times xor including missing number (1 to 5)
        
        missing_number = xor1 ^ xor2
        return missing_number

if __name__ == '__main__':
    a = [1, 2, 4, 5]
    missing_number = MissingNumber(a)
    print(missing_number.xor())  # Expected output: 3
    print(missing_number.summation())
    print(missing_number.hashing())  # Expected output: 3
    print(missing_number.brute_force())  # Expected output: 3
