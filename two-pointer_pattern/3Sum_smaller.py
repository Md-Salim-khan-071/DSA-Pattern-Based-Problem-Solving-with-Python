# question : given an array . and  a target . find triplets ( 3 numbers in the array ) whose sum is less than target . no of such triplets should be returned

def threeSumClosest(nums,target):
    nums.sort()
    n=len(nums)
    i=0
    result = 0
    while(i <= n-3):
        if (i>0 and nums[i] == nums[i-1]):
            i+=1
            continue
        j=i+1
        k=n-1
        while(j<k):
            result_sum = nums[i]+nums[j]+nums[k]
            if(result_sum==target):
                k -= 1

            elif(result_sum<target):
                result += 1
                j += 1

            else:
                k -= 1
            
        i+=1
    return result

nums = [-2,0,1,3,-1]
target = 2
result = threeSumClosest(nums,target)
print(result)