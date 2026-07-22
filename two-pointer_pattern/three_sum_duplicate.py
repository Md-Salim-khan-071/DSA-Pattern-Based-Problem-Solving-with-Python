def threeSum(nums):
    nums.sort()
    n=len(nums)
    answer = []
    i=0
    
    while(i <= n-3):
        if (i>0 and nums[i] == nums[i-1]):
            i+=1
            continue
        j=i+1
        k=n-1
        while(j<k):
            if (  (nums[j] + nums[k]) > -nums[i] ):
                k -= 1
            elif ( (nums[j] + nums[k]) < -nums[i] ):
                j += 1
            else :
                answer.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while(j<n and  nums[j] == nums[j-1]):
                    j+=1
                while(k>=0 and k<n-1 and nums[k]==nums[k+1]):
                    k-=1
        i+=1
    return answer

nums = [-1,0,1,2,-1,-4]
result = threeSum(nums)
print(result)
                 