def threeSumClosest(nums,target):
    nums.sort()
    n=len(nums)
    i=0
    max_diff = float('inf')
    answer = 0
    while(i <= n-3):
        if (i>0 and nums[i] == nums[i-1]):
            i+=1
            continue
        j=i+1
        k=n-1
        while(j<k):
            result_sum = nums[i]+nums[j]+nums[k]
            if(result_sum==target):
                return result_sum

            elif(result_sum<target):
                diff = abs(result_sum-target)
                if(max_diff > diff):
                    max_diff = diff
                    answer = result_sum
                j += 1


            else:
                diff = abs(result_sum-target)
                if(max_diff > diff):
                    max_diff = diff
                    answer = result_sum
                k -= 1
            
        i+=1
    return answer

nums = [-1,2,5,-4]
target = 1
result = threeSumClosest(nums,target)
print(result)