# Given an array of integers, return indices of the two numbers such that they add up to a specific target


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # creates a new dictionary
        d = dict()
        for i in range(len(nums)):
            key = target - nums[i]
            # if the difference is in the dictionary
            if key in d:
                return [d[key] , i]
            # if the difference is NOT in the dictionary
            # put a new entry in the dictionary, key=number, value=position
            else:
                d[nums[i]] = i
                
        return 
        

nums = [3, 2, 4]
target = 7

a = Solution()
print "The indices of two numbers adding up to", target, "is", a.twoSum(nums, target)


