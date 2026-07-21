"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


def merge(nums1, nums2):
    m = len(nums1)
    n = len(nums2)

    i = m - 1          # Last valid element in nums1
    j = n - 1          # Last element in nums2
    k = (m + n) - 1      # Last position in nums1

    while i >= 0 and j >= 0:

        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    # Copy remaining elements from nums2
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

"""

"""

nums1 = [1,3,5]
nums2 = [2,4,6]
print(merge(nums1 , nums2))
