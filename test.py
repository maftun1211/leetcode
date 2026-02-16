# def hammingWeight( n: int) -> int:
#     return bin(n).count('1')

# def romanToInt(s: str) -> int:
#     d1={
#         'I':1,
#         'IV':4,
#         'V':5,
#         'IX':9,
#         'X':10,
#         'XL':40,
#         'L':50,
#         'XC':90,
#         'C':100,
#         'CD':400,
#         'D':500,
#         'CM':900,
#         'M':1000
#     }
#     t=0
#     for c in s:
#         if c in d1:
#             t+=d1[c]
#     return t
# print(romanToInt("IVX"))
from typing import List
def removeDuplicates( nums: List[int]) -> int:
    if not nums:
        return 0
    k=1
    for i in range(1,len(nums)):
        if nums[i]!= nums[k-1]:
            nums[k]=nums[i]
            k+=1
    return k



