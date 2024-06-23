from typing import List


class Solution:
    """
    This class has various solutions for LeetCode question 1248
    'Count Number of Nice Subarrays'
    """

    def brute_approach(self, nums: List[int], k: int) -> int:
        """
        Time complexity: O(n * n ) where n = len(nums) = len(grumpy)
        Space complexity: O(1)
        """

        result = 0
        pass

    def optimal_approach(self, nums: List[int], k: int) -> int:
        """
        This method uses sliding window approach
        Time complexity: O(n)
        Space complexity: O(1)
        """
        lt = 0
        result = 0
        window, max_window = 0, 0
        for rt in range(len(nums)):
            if grumpy[rt] == 0:
                result += nums[rt]
            else:
                window += nums[rt]
            if rt - lt + 1 > k:
                if grumpy[lt]:
                    window -= nums[lt]
                lt += 1
            max_window = max(max_window, window)
        return max_window + result

    def my_approach(self, customers, grumpy, minutes) -> int:
        """
        Approach: Sliding window approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = 0
        cnt = 0
        for indx in range(len(customers)):
            if grumpy[indx]:
                grumpy[indx] = customers[indx]
            else:
                result += customers[indx]
            cnt += 1

        st = 0
        ed = st + minutes - 1
        r_sum = 0

        for x in range(ed):
            r_sum += grumpy[x]
        max_unlock = r_sum

        while ed < cnt:
            r_sum += grumpy[ed]
            max_unlock = max(max_unlock, r_sum)
            r_sum -= grumpy[st]
            st += 1
            ed += 1

        return result + max_unlock

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        customers_inps = [[1, 0, 1, 2, 1, 1, 7, 5], [1],
                          [26, 1, 100, 4, 300, 22], [26, 1, 100, 4, 300, 22],
                          [20, 25, 20, 40, 75, 35, 20, 45, 25, 10, 25],
                          [10000, 10001]]
        grumpy_inps = [[1, 0, 1, 0, 1, 1, 0, 0], [0],
                       [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1],
                       [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                       [1, 1]]
        minutes_inps = [2, 1, 1, 5, 4, 2]
        results = [16, 1, 452, 453, 290, 20001]
        soln_results = []
        test_fail = []

        # Brute Force approach
        print(f"Brute Force Approach")
        for indx, _ in enumerate(customers_inps):
            soln_result = self.brute_approach(nums=customers_inps[indx],
                                              k=minutes_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # My approach
        print(f"My Approach")
        for indx, _ in enumerate(customers_inps):
            soln_result = self.my_approach(customers=customers_inps[indx],
                                           grumpy=grumpy_inps[indx],
                                           minutes=minutes_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # Optimal approach
        print(f"Optimal Approach")
        for indx, _ in enumerate(customers_inps):
            soln_result = self.optimal_approach(nums=customers_inps[indx],
                                                k=minutes_inps[indx])
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
