from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Time Complexity: O(n log n) # For sorting the keys
        Space Complexity: O(n) # For hash map
        Approach: Hash map solution
        """
        result = []
        mapping = dict()
        for num in arr1:
            mapping[num] = mapping.get(num, 0) + 1
        for num in arr2:
            for cnt in range(mapping[num]):
                result.append(num)
            del mapping[num] # To get rid of already counted
        keys = sorted(mapping.keys())
        for num in keys:
            for cnt in range(mapping[num]):
                result.append(num)
        return result

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        arr1_inps = [
            [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
            [28, 6, 22, 8, 44, 17],
            [2, 3, 136, 12, 100],
            [2, 1, 1, 0, 0, 1, 2, 1, 1, 0],
        ]
        arr2_inps = [
            [2, 1, 4, 3, 9, 6],
            [22, 28, 8, 6],
            [2, 3, 12],
            [1, 2, 0],
        ]
        results = [
            [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
            [22, 28, 8, 6, 17, 44],
            [2, 3, 12, 100, 136],
            [1, 1, 1, 1, 1, 2, 2, 0, 0, 0]
        ]
        soln_results = []
        test_fail = []
        print("Hashmap based approach")
        for indx, arr1 in enumerate(arr1_inps):
            res = self.relativeSortArray(arr1, arr2_inps[indx])
            test_fail.append(res == results[indx])
            soln_results.append(res)
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
