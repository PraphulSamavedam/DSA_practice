import heapq
import math
from typing import List


class Solution:

    def optimized_approach(self, difficulty: List[int], profit: List[int],
                            worker: List[int]) -> int:
        """
        Time Complexity: O(max(n log n, m log m))
        Space Complexity: O(m)
        """
        minDiffHeap = [(diff, proft) for diff, proft in
                       zip(difficulty, profit)]
        heapq.heapify(minDiffHeap)  # m log m

        worker.sort()  # n log n
        result = 0
        max_profit = 0
        for work in worker:
            while minDiffHeap and minDiffHeap[0][0] <= work:
                _, profit = heapq.heappop(minDiffHeap)
                max_profit = max(max_profit, profit)
            result += max_profit
        return result

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        difficulty_inps = [[2, 4, 6, 8, 10], [85, 47, 57]]
        profit_inps = [[10, 20, 30, 40, 50], [24, 66, 99]]
        worker_inps = [[4, 5, 6, 7], [40, 25, 25]]
        results = [100, 0]
        soln_results = []
        test_fail = []

        # Optimal approach
        print(f"Optimal Approach")
        for indx, _ in enumerate(difficulty_inps):
            soln_result = self.optimized_approach(
                difficulty=difficulty_inps[indx], profit=profit_inps[indx],
                worker=worker_inps[indx])
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
