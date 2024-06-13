from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(1) (Ignoring sort space)
        Approach: Greedy Approach (Fill the smaller seats quickly in a greedy fashion)
        """
        seats.sort()
        students.sort()
        result = 0
        for indx in range(len(seats)):
            result += abs(students[indx] - seats[indx])
        return result

    def test(self):
        expected, results, success = self.testCases()
        self.print_results(expected, results, success)

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        seat_inps = [
            [3, 1, 5], [4, 1, 5, 9], [2, 2, 6, 6], [2, 2, 3], [14, 10, 20]
        ]
        student_inps = [
            [2, 7, 4], [1, 3, 2, 6], [1, 3, 2, 6], [3, 2, 2], [10, 24, 15]
        ]
        results = [4, 7, 4, 0, 5]
        soln_results = []
        test_fail = []
        for indx, seat in enumerate(seat_inps):
            soln_result = self.minMovesToSeat(seat, student_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        return results, soln_result, test_fail

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
