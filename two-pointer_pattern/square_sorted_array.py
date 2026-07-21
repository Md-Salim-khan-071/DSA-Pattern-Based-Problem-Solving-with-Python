def sortedSquares(nums):
    if (len(nums) == 0):
        return 0
    
    negative = []
    positive = []
    n = len(nums)

    for i in range(n):
        if (nums[i]>=0):
            positive.append(nums[i])
        else:
            negative.append(nums[i])
    
    if(len(negative)==0):
        for i in range(len(positive)):
            positive[i] = positive[i]*positive[i] #squaring each
        return positive
    
    elif(len(positive)==0):
        for i in range(len(negative)):
            negative[i] = negative[i]*negative[i] #squaring each
        negative.reverse()
        return negative
    
    else:
        for i in range(len(negative)):
            negative[i] = negative[i]*negative[i] #squaring each
        negative.reverse()

        for i in range(len(positive)):
            positive[i] = positive[i]*positive[i] #squaring each
        
        new_array = []
        
        i=0
        j=0
        while ( i<= len(negative)-1 and j<=len(positive)-1):
            if negative[i]>=positive[j]:
                new_array.append(positive[j])
                j+=1
            else:
                new_array.append(negative[i])
                i+=1
        
        while i < len(negative):
            new_array.append(negative[i])
            i += 1

        while j < len(positive):
            new_array.append(positive[j])
            j += 1
    
    return new_array


nums = [-4,-2,0,1,2,3]
print(sortedSquares(nums))     
