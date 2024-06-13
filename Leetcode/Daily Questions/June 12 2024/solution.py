from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Time Complexity: O(n)
        Space Complexity: O(1)
        Approach: CountSort
        Notes:Multiple pass
        """
        cnt_0, cnt_1 = 0, 0
        cnt = 0
        # Get the count of the specific values in the list
        for num in nums:
            if num == 0:
                cnt_0 += 1
            elif num == 1:
                cnt_1 += 1
            cnt += 1

        # Fill back the numbers of the list
        for indx in range(cnt):
            if cnt_0 > 0:
                nums[indx] = 0
                cnt_0 -= 1
            elif cnt_1 > 0:
                nums[indx] = 1
                cnt_1 -= 1
            else:
                nums[indx] = 2

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        numbers = [
            [0, 2, 1],
            [2, 1, 1, 0, 0, 1, 2, 1, 1, 0],
            [0, 2, 2, 1, 0, 1, 1, 2, 0],
            [1, 0],
            [0, 1, 1],
            [0, 2, 1, 1, 0, 2, 1, 1, 2],
            [0, 2],
            [0, 1, 2],
            [2, 0, 2, 0]
        ]
        results = [
            [0, 1, 2],
            [0, 0, 0, 1, 1, 1, 1, 1, 2, 2],
            [0, 0, 0, 1, 1, 1, 2, 2, 2],
            [0, 1],
            [0, 1, 1],
            [0, 0, 1, 1, 1, 1, 2, 2, 2],
            [0, 2],
            [0, 1, 2],
            [0, 0, 2, 2]
        ]
        soln_results = []
        test_fail = []
        for indx, num in enumerate(numbers):
            self.sortColors(num)
            test_fail.append(num == results[indx])
            soln_results.append(num)
        return results, soln_results, test_fail

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

    def test(self):
        expected, results, success = self.testCases()
        self.print_results(expected, results, success)

if __name__ == "__main__":
    soln = Solution()
    soln.test()
