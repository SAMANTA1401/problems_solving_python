hashmap = [] # dict to find index of single number in arr
def single_number(arr):
    '''find single number from the array of pair numbers'''
    for i in range(len(arr)):
        if arr[i] not in hashmap:
            hashmap.append(arr[i])
        else:
            hashmap.remove(arr[i])
    return hashmap[0]




if __name__ == "__main__":
    arr = [2,2,3,4,5,3,1,1,4,6,6]
    print(single_number(arr))
 