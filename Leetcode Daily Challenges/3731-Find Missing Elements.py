def findMissingElements(nums):
    nums.sort()
    answer = []

    for i in range(nums[0], nums[-1] + 1):
        if i not in nums:
            answer.append(i)

    return answer


nums = [1, 4, 2, 5]
print(findMissingElements(nums))