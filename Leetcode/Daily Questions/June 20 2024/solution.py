from typing import List


class Solution:

    def brute_approach(self, positions: List[int], m: int) -> int:
        """
        This method returns the maximum possible minimum distance between
        any two balls placed in the positions after placing m balls in the
        positions provided.

        Time complexity: O(n * max(positions) ) where n = len(positions)
        Space complexity: O(1)
        """
        positions.sort(reverse=False)
        best_max_dist = positions[-1] - positions[0]

        ans = -1
        for dist in range(1, best_max_dist + 1):
            balls = 1
            last_posn = positions[0]
            for posn in positions:
                if posn - last_posn >= dist:
                    last_posn = posn
                    balls += 1
            if balls >= m:
                ans = dist
            else:  # balls < m
                break
        return ans

    def optimal_approach(self, positions: List[int], m: int) -> int:
        """
        This method returns the maximum possible minimum distance between
        any two balls placed in the positions after placing m balls in the
        positions provided.

        Time complexity: O(n * log (max(positions) - min(positions)) )
        Space complexity: O(1)
        """
        positions.sort(reverse=False)
        lt, rt = 1, positions[-1] - positions[0]  # Min Distance, Max Distance

        ans = -1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            last_posn = positions[0]
            balls = 1
            for posn in positions:
                if posn - last_posn >= mid:
                    balls += 1
                    last_posn = posn
            if balls >= m:
                ans = mid
                lt = mid + 1
            else:
                rt = mid - 1
        return ans

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        input_inps = [[26, 1, 100, 4, 300, 22], [26, 1, 100, 4, 300, 22],
                      [1, 2, 3, 4, 7], [10000, 10001]]
        m_inps = [2, 3, 3, 2]
        results = [299, 99, 3, 1]
        soln_results = []
        test_fail = []

        # Brute Force approach
        print(f"Brute Force Approach")
        for indx, _ in enumerate(input_inps):
            soln_result = self.brute_approach(positions=input_inps[indx],
                                              m=m_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # Optimal approach
        print(f"Optimal Approach")
        for indx, _ in enumerate(input_inps):
            soln_result = self.optimal_approach(positions=input_inps[indx],
                                                m=m_inps[indx])
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
