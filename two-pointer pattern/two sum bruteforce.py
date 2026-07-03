def two_sum_bruteforce(nums, target):
    n = len(nums)  #this give the length of array so that we can use as index value . if we directly "for i in nums"  then  i becomes elemenst of nums and not indexes

    for i in range(n):   # range starts from and stops one before the last . since n = 4 , i -> 0,1,2,3 
        for j in range(n):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]

nums = [2, 7, 11, 15]
target = 9

print(two_sum_bruteforce(nums, target))