"""
Question:
You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

Example:
Input: n = 124
Output: 8
Explanation:
The digits of n are [1, 2, 4].
The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
The maximum product is 8.
"""


def maxProduct(n):
    digits = [int(d) for d in str(n)]

    products = []
    L = len(digits)

    max_product = 0
    for i in range(L):
        
        j = i+1  
        while( j < L):
            current_product = digits[i]*digits[j]
            if (current_product > max_product):
                max_product = current_product
            j += 1
        
    return max_product

    


n = 12345
print(maxProduct(n))