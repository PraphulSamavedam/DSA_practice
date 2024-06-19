import math


class Solution:

    def linear_approach(self, n: int) -> bool:
        """
        Returns True only if the number can be decomposed as sum of squares
        of two whole numbers.


        Approach: HashSet based
        Time Complexity: O(sqrt(n))
        Space Complexity: O(sqrt(n))
        """
        limit = int(math.sqrt(n)) + 1
        memory = set()
        for x in range(limit):
            if (n - (x*x) in memory) or (n == (2*x*x)):
                return True
            memory.add(x*x)
        return False

    def optimized_approach(self, n: int) -> bool:
        """
        Returns True only if the number can be decomposed as sum of squares
        of two whole numbers based on two pointer approach

        Approach: HashSet based
        Time Complexity: O(sqrt(n))
        Space Complexity: O(1)
        """
        lt = 0
        rt = int(math.sqrt(n)) + 1

        while lt <= rt:
            val = (lt*lt) + (rt*rt)
            if val == n:
                return True
            elif val < n:
                lt += 1
            else:
                rt -= 1

        return False

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        n_inps = [1, 5, 29, 64, 13, 2, 3, 17, 9, 102657424, 102746825,
                  104344825, 2147483647, 268435481]
        results = [True, True, True, True, True, True, False, True, True,
                   True, True, True, False, True]
        soln_results = []
        test_fail = []

        # Brute Force approach
        for indx, _ in enumerate(n_inps):
            soln_result = self.linear_approach(n=n_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        print(f"Brute Force Approach")
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # Optimal approach
        for indx, _ in enumerate(n_inps):
            soln_result = self.optimized_approach(n=n_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        print(f"Optimal Approach")
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
