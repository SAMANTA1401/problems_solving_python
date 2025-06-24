from functools import reduce

def output_prod(arr):
    for i in range(len(arr)):
        if i==0:
            prod = reduce(lambda a,b : a*b, arr[i+1:])
            
        elif i == len(arr)-1:
            prod = reduce(lambda a,b : a*b, arr[:i])

        else:
            prod = reduce(lambda a,b : a*b, arr[i+1:])*reduce(lambda a,b : a*b, arr[:i])

        if arr[i] == prod:
            return arr[i]
        
    return False

if __name__ == "__main__":
    arr = [2,3,24,4]
    print(output_prod(arr))
    