from typing import List


class Solution:
    """
    This class has various solutions for LeetCode question 1248
    'Count Number of Nice Subarrays'
    """

    def brute_approach(self, nums: List[int], k: int) -> int:
        """
        Time complexity: O(n * n ) where n = len(nums)
        Space complexity: O(1)
        Cons: TLE
        """
        result = 0
        for st in range(len(nums)):
            for ed in range(st + k - 1, len(nums)):
                cnt = 0
                it = st
                while it <= ed:
                    if nums[it] % 2:
                        cnt += 1
                    it += 1
                if cnt == k:
                    result += 1
        return result

    def optimal_approach(self, nums: List[int], k: int) -> int:
        """
        This method uses sliding window approach with three pointers
        Time complexity: O(n)
        Space complexity: O(1)
        """
        l, m = 0, 0
        odd = 0
        result = 0
        for r in range(len(nums)):
            odd += nums[r] % 2

            while odd > k:
                if nums[l] % 2:
                    odd -= 1
                l += 1
                m = l

            if odd == k:
                while not nums[m] % 2:
                    m += 1
                result += (m - l) + 1
        return result

    def my_approach(self, nums: List[int], k: int) -> int:
        """
        Approach: Sliding window approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        lt = 0
        rt = 0
        odd = 0
        support = 1
        result = 0

        while rt < len(nums):
            odd += nums[rt] % 2

            if odd == k:
                # There are k odd numbers in window

                # Is lt pointing to odd or even ?
                if nums[lt] % 2 == 0:
                    support = 1
                    while nums[lt] % 2 == 0:
                        support += 1
                        lt += 1
                    # Now lt should point to odd number
                # else: # lt point towards odd number
                result += support
            elif odd > k:
                # We ensured that lt points to odd number when odd == k
                lt += 1
                odd -= 1

                # Update support
                support = 1
                while nums[lt] % 2 == 0:
                    support += 1
                    lt += 1
                result += support
            rt += 1
        return result

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        nums_inps = [[1, 1, 2, 1, 1], [2, 4, 6], [2, 4, 6],
                     [2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
                     [2, 23, 92, 3, 4, 1, 20, 1, 4129, 8192, 7861, 2342]]
        k_inps = [3, 1, 5, 2, 2, 3]
        results = [2, 0, 0, 16, 16, 14]
        soln_results = []
        test_fail = []

        # Brute Force approach
        print(f"Brute Force Approach")
        for indx, _ in enumerate(nums_inps):
            soln_result = self.brute_approach(nums=nums_inps[indx],
                                              k=k_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # My approach
        print(f"My Approach")
        for indx, _ in enumerate(nums_inps):
            soln_result = self.my_approach(nums=nums_inps[indx],
                                           k=k_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # Optimal approach
        print(f"Optimal Approach")
        for indx, _ in enumerate(nums_inps):
            soln_result = self.optimal_approach(nums=nums_inps[indx],
                                                k=k_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        return results, soln_results, test_fail

    def test(self):
        expected, results, success = self.testCases()
        self.print_results(expected, results, success)

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
