# https://leetcode.com/studyplan/top-interview-150/

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.

Return k.
"""

class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:
        noDuplicatedList = [nums[0]]
        for i in range(1, len(nums), 1):
            if (nums[i] > noDuplicatedList[-1]):
                noDuplicatedList.append(nums[i])
        for i in range(len(noDuplicatedList)):
            nums[i] = noDuplicatedList[i]
        for i in range(len(noDuplicatedList), len(nums), 1):
            nums[i] = None
        return len(noDuplicatedList)

if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2, 3, 3]
    print('k: ', s.removeDuplicates(nums))
    print('nums ---->: ', nums)

