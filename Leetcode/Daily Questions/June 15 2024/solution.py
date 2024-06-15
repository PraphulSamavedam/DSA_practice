import heapq
import math
from typing import List


class Solution:

    def brute_force_approach(self, k: int, w: int, profits: List[int],
                             capital: List[int]) -> int:
        """
        Brute Force Approach
        Time Complexity: O(n * k)
        Space Complexity: O(n)
        Test cases: 32 passed out of 35
        Failed: Due to TLE
        """
        k = min(k, len(profits))

        # Even if we can do more projects,  we cannot exceed the projects
        # count.

        def getMaxProfitProjectUnderCapacity(capacity: int, profits: List[int],
                                             capital: List[int], visited: set):
            """
            Returns the best the project under the capacity which is
            not part of the visited set
            """
            max_profit = -math.inf
            n = len(profits)
            ix = None
            for indx in range(n):
                if (capital[indx] <= capacity) and (indx not in visited) and (
                        profits[indx] >= max_profit):
                    max_profit = profits[indx]
                    ix = indx
            return max_profit, ix

        visited = set()
        capacity = w
        # print(f"k == {k}")

        while k > 0:
            profit, ix = getMaxProfitProjectUnderCapacity(capacity, profits,
                                                          capital, visited)
            # print(f"Capacity: {capacity} Profit: {profit}, Index: {ix} visit: {visited}")
            if ix is not None:
                capacity += profit  # Increase capacity
                visited.add(ix)
            # print(f"New Capacity: {capacity}, Result: {result}",)
            k -= 1

        return capacity

    def optimized_approach(self, k: int, w: int, profits: List[int],
                           capital: List[int]) -> int:
        """
        Two Heap Approach
        Time Complexity: O(k * log n)
        Space Complexity: O(n)
        Test cases: 35 passed out of 35
        """
        mxProfit = []
        mnCap = [(cap, profit) for (cap, profit) in zip(capital, profits)]
        heapq.heapify(mnCap)  # MinHeap

        for i in range(k):

            while mnCap and mnCap[0][0] <= w:
                _, profit = heapq.heappop(mnCap)  # (O log n)
                heapq.heappush(mxProfit, -1 * profit)  # O(log n)
            if mxProfit:
                w += (-1 * heapq.heappop(mxProfit))
            else:
                break

        return w

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        k_inps = [2, 3, 3, 3, 1, 3, 4]
        init_capacity_inps = [
            0, 0, 5, 5, 10, 10, 10
        ]
        profit_inps = [
            [1, 2, 3], [1, 2, 3], [1, 2, 4], [500, 20, 40, 10],
            [500, 20, 40, 10], [500, 20, 40, 10], [500, 20, 40, 10]
        ]
        capital_inps = [
            [0, 1, 1], [0, 1, 2], [3, 2, 3], [25, 7, 12, 6],
            [25, 7, 12, 6], [25, 7, 12, 6], [25, 7, 12, 6]
        ]
        results = [4, 6, 12, 5, 30, 570, 580]
        soln_results = []
        test_fail = []

        # Brute Force approach
        for indx, _ in enumerate(k_inps):
            soln_result = self.brute_force_approach(k=k_inps[indx],
                                                    w=init_capacity_inps[indx],
                                                    profits=profit_inps[indx],
                                                    capital=capital_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        print(f"Brute Force Approach")
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # Optimal approach
        for indx, _ in enumerate(k_inps):
            soln_result = self.optimized_approach(k=k_inps[indx],
                                                  w=init_capacity_inps[indx],
                                                  profits=profit_inps[indx],
                                                  capital=capital_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        print(f"Optimal Approach")
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        return results, soln_result, test_fail

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
