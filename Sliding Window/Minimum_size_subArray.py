def minSubArrayLen(target, nums):
    n = len(nums)

    low=0
    high=0
    sum=0
    answer = max

    while(high < n):

        sum = sum + nums[high]

        while ( sum >= target ):  #this loop will run  untill the sum is greater than target . 
            len = (high - low) + 1
            answer = min(answer , len)
            sum = sum -  nums[low]
            low += 1
        # suppose [1,2,3,8,9] and target=15 . now starting from  first , to be sum equal to zero we need all elements . later we remove the first element , still the the sum  is greater than target . remove second still greater . remove third  still greater . but if we remove fourth(8) sum is  lesser than target , hence  loop is stopped answer is 2 . 

        high += 1

    return answer 