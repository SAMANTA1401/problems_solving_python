
class ThreeSum():
    def __init__(self, arr):
        self.arr = arr
        
        
    def brute_force(self):
        '''
        Time Complexity: O(N^3), N = size of the array.
        Reason: We are using 3 nested loops. And inserting triplets into the set takes 
        O(log(no. of unique triplets)) time complexity. But we are not considering the time complexity of 
        sorting as we are just sorting 3 elements every time.
        
        Space Complexity: O(2* no of triplets) time complexity
        Reason: s we are using a set data structure and a list to store the triplets.
        '''
        st = set()
        n = len(self.arr)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if self.arr[i] + self.arr[j] + self.arr[k] == 0:
                        temp = [self.arr[i], self.arr[j], self.arr[k]]
                        temp.sort()
                        st.add(tuple(temp)) # set stores only unique elements
        ans = [list(x) for x in st]
        return ans
    
    def two_loop(self):
        '''In the previous approach, we utilized 3 loops, but now our goal is to reduce it to 2 loops. 
        To achieve this, we need to find a way to calculate arr[k] since we intend to eliminate the third loop 
        (k loop). To calculate arr[k], we can derive a formula as follows: 
        arr[k] = target - (arr[i]+arr[j]+arr[k]) = 0-(arr[i]+arr[j]+arr[k]) = -(arr[i]+arr[j]+arr[k]) 
        So, we will first calculate arr[i] and arr[j] using 2 loops and for the third one i.e. arr[k] we 
        will not use another loop and instead we will look up the value 0-(arr[i]+arr[j]+arr[k]) in the set 
        data structure. Thus we can remove the third loop from the algorithm.
        For implementing the search operation of the third element,  we will store all the elements between the 
        indices i and j in a HashSet and then we will search for the third element in the HashSet.
        
        Time Complexity: O(N3 * log(no. of unique triplets)), where N = size of the array.
        eason: Here, we are mainly using 3 nested loops. And inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.

        Space Complexity: O(2 * no. of the unique triplets) as we are using a set data structure and a list to store the triplets.
        
        
        '''
        st = set()
        for i in range(len(self.arr)):
            hashset = set()
            for j in range(i+1, len(self.arr)):
                third = -(self.arr[i] + self.arr[j])
                if third in hashset:
                    temp = [self.arr[i], self.arr[j], third]
                    temp.sort()
                    st.add(tuple(temp))
                hashset.add(self.arr[j])
                
        ans = [list(x) for x in st]
        return ans
                
                
    def three_pointer(self):
        '''We will first sort the array. Then, we will fix a pointer i, and the rest 2 pointers j and k will be moving. 
            Now, we need to first understand what the HashSet and the set were doing to make our algorithm work without them. So, the set data structure was basically storing the unique triplets in sorted order and the HashSet was used to search for the third element.
            That is why, we will first sort the entire array, and then to get the unique triplets, we will simply skip the duplicate numbers while moving the pointers.
            How to skip duplicate numbers
            As the entire array is sorted, the duplicate numbers will be in consecutive places. So, while moving a pointer, we will check the current element and the adjacent element. Until they become different, we will move the pointer by 1 place. We will follow this process for all 3 pointers. Thus, we can easily skip the duplicate elements while moving the pointers.
            Now, we can also remove the HashSet as we have two moving pointers i.e. j and k that will find the appropriate value of arr[j] and arr[k]. So, we do not need that HashSet anymore for the look-up operations.
        
            Time Complexity: O(NlogN) sorting the array +O(N^2)for and while loop, where N = size of the array.
            Reason: The pointer i, is running for approximately N times. And both the pointers j and k combined can run for approximately N times including the operation of skipping duplicates. So the total time complexity will be O(N2). 

            Space Complexity: O(no. of triplets), This space is only used to store the answer. We are not using any extra space to solve this problem. So, from that perspective, space complexity can be written as O(1).
        '''
        ans = []
        arr.sort()
        for i in range(len(self.arr)):
            # skip the duplicates
            if i != 0 and arr[i] == arr[i-1]:
                continue
            # moving 2 pointers:
            j = i + 1
            k = len(self.arr) - 1
            
            while j < k:
                sum = arr[i] + arr[j] + arr[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    temp = [arr[i], arr[j], arr[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    # skip the duplicates
                    while j < k and arr[j] == arr[j-1]:
                        j += 1
                    while j < k and arr[k] == arr[k+1]:
                        k -= 1
                        
        return ans
        
        
    
    
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    n = len(arr)
    triplet = ThreeSum(arr)
    # ans = triplet.brute_force()
    # ans = triplet.two_loop()
    ans = triplet.three_pointer()
    print("Triplets with sum zero are:")  # Output: Triplets with sum zero are: [-1, -1, 2] [-1, 0, 1]  [0, -1, 1]  [2, 0, -2]  \n
    print(ans)
    for it in ans:
        print("[", end="")
        for i in it:
            print(i, end=" ")
        print("]", end=" ")
    print("\n")
