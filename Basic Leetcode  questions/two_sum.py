# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[num] = i


# Driver Code
nums = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the target: "))

result = twoSum(nums, target)

print("Indices:", result)