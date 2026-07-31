
def maxSubarraySum(arr, k):
    n = len(arr)

    low = 0 
    high = k-1 
    sum  = 0
    i=0
    for i in  range(k):
        sum = sum + arr[i] 
        i  += 1

    result = sum 
    while( high < n ):
        result = max(result , sum)
        low += 1
        high += 1
        sum = sum - arr[low-1]
        if(high == n):
            break
        sum  = sum + arr[high]

    return result


arr =  [10,20,30,40,50,60,70]
k=3
print(maxSubarraySum(arr , k))