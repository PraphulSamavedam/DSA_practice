import math
from typing import List
from copy import deepcopy


class Solution:
    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        nums_inp = [
            [2, 1, 2], [2, 3, 1], [2, 2, 6, 6],
            [3, 56, 5, 10, 15, 15, 15],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [2, 3, 4, 5, 6, 7, 1, 1, 1]
        ]
        results = [1, 0, 2, 3, 78, 15]
        soln_results = []
        test_fail = []

        # Brute Force approach
        for indx, num in enumerate(nums_inp.copy()):
            soln_result = self.brute_force(num)
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        print(f"Brute Force Approach")
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # Sort based approach
        for indx, num in enumerate(deepcopy(nums_inp)):
            soln_result = self.sort_approach(num)
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        print(f"Sort based approach")
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # # Linear approach
        for indx, num in enumerate(deepcopy(nums_inp)):
            soln_result = self.linear_approach(num)
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        print(f"Linear solution approach")
        self.print_results(results, soln_results, test_fail)

        return results, soln_result, test_fail

    def brute_force(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n**2)
        Space Complexity: O(n)
        """
        dct = dict()
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
        kSet = set(dct.keys())
        ordKSet = sorted(dct.keys())
        result = 0
        for key in ordKSet:
            cnt = dct[key]
            if cnt == 1:
                continue
            mov = 0
            while cnt > 1:
                while (key + mov) in kSet:
                    mov += 1
                kSet.add(key + mov)
                result += mov
                cnt -= 1
        return result

    def sort_approach(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        n = len(nums)
        if n <= 1:
            return 0

        nums.sort()
        result = 0
        for idx in range(1, len(nums)):
            if nums[idx] <= nums[idx - 1]:
                result += (nums[idx - 1] - nums[idx] + 1)
                nums[idx] = nums[idx - 1] + 1
        return result

    def linear_approach(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n + max(nums))
        Space Complexity: O(n)
        Approach: Hashmap based
        """
        dct = dict()
        n = 0
        max_ = -math.inf
        min_ = math.inf
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
            n += 1
            max_ = max(max_, num)
            min_ = min(min_, num)

        # print(f"n: {n}, min: {min_}, max: {max_}, nums: {nums}")
        # print(f"dct: {dct}")
        result = 0
        carry = 0
        for i in range(min_, max_ + n + 1):
            if i in dct:
                carry = dct[i] - 1
                if carry > 0:
                    dct[i + 1] = dct.get(i + 1, 0) + carry
                    result += carry
            elif carry > 0 :
                carry -= 1
                result += carry
        return result

    def test(self):
        expected, results, success = self.testCases()
        # self.print_results(expected, results, success)

    def print_results(self, expected_results, solution_results, fail_pass):
        if all(fail_pass):
            print(f"All test cases passed")
            return None
        for indx, boolean in enumerate(fail_pass):
            if boolean:
                print(f"Success {indx + 1} test case.")
            else:
                print(f"Failed for {indx + 1} test case")
                print(f"Expected: {expected_results[indx]}")
                print(f"Your Res: {solution_results[indx]}")


if __name__ == "__main__":
    soln = Solution()
    soln.test()
