def max_con_one(arr):
    max_count = 0
    count = 0
    for i in range(len(arr)):
        if arr[i]==1:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    return max_count


if __name__ == "__main__":
    arr = [1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,1,1]
    print(max_con_one(arr))
 
        
        



