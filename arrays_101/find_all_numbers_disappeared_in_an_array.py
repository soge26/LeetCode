class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return list(set(i for i in range(1, len(nums)+1)) - set(nums))


nums = [4,3,2,7,8,2,3,1]

print(Solution().findDisappearedNumbers(nums))



# interesting solution

def findDisappearedNumbers(self, list):
    i = 0
    n = len(list)

    # STEP 1 - Cyclic sort list
    while (i < n):
        if (list[i] != i + 1):
            correct_pos = list[i] - 1

            if (list[i] == list[correct_pos]):
                i += 1
            else:
                list[i], list[correct_pos] = list[correct_pos], list[i]
        else:
            i += 1

    # STEP 2 - Elements != index+1 are missing elements in list.
    res = []
    for j in range(0, n):
        if list[j] != j + 1:
            res.append(j + 1)
    return res