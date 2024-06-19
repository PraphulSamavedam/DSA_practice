from typing import List


class Solution:

    def brute_force_approach(self, nums: List[int], n: int) -> int:
        """
        Brute Force Approach
        Time Complexity: O(n * len(nums))
        Space Complexity: O(n)
        Failed: Due to Memory Limit
        Will fail for the last test case of this file.
        """

        def fill_boolean(boolean: List[bool], n: int, num: int):
            for idx in range(n, -1, -1):
                # print(f"x: {boolean[idx]}, ix:{idx}, num: {num}")
                if boolean[idx] and idx + num <= n:
                    boolean[idx + num] = True
            return boolean

        boolean = [False for _ in range(n + 1)]
        boolean[0] = True

        for num in nums:
            boolean = fill_boolean(boolean, n, num)
        result = 0
        while not all(boolean):
            for ix in range(n):
                if not boolean[ix]:
                    num = ix
                    result += 1
                    break
            # print(f"Pre fill: {boolean}")
            boolean = fill_boolean(boolean, n, num)
            # print(f"Post fill boolean: {boolean}")
        return result

    def optimized_approach(self, nums: List[int], n: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        rng = [0, 0]
        patches = 0
        for ix, num in enumerate(nums):
            if num > rng[1] + 1:
                # Add the patching
                while num > rng[1] + 1:
                    patch = rng[1] + 1
                    rng[1] += patch
                    patches += 1

                    # Return if we have reached required target
                    if rng[1] >= n:
                        return patches

                # print(f"Post Patching: {rng}")
            rng[1] += num
            # print(f"Adding the number as patch: {rng}")
            if rng[1] >= n:
                return patches

        # Add additional patches post exhausting all the options provided
        while rng[1] < n:
            patch = rng[1] + 1
            rng[1] += patch
            patches += 1
        return patches

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        n_inps = [6, 20, 5, 20, 52
                  , 2147483647
                  ]
        nums_inps = [
            [1, 3], [1, 5, 10], [1, 2, 2],
            [1, 2, 2, 6, 34, 38, 41, 44, 47, 47, 56, 59, 62, 73, 77, 83, 87,
             89, 94], [1, 2, 2, 6, 34, 38]
            , [1, 2, 31, 33]
        ]
        results = [1, 2, 0, 1, 2
                   , 28
                   ]
        soln_results = []
        test_fail = []

        # Brute Force approach
        for indx, _ in enumerate(n_inps):
            soln_result = self.brute_force_approach(nums=nums_inps[indx],
                                                    n=n_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        print(f"Brute Force Approach")
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # Optimal approach
        for indx, _ in enumerate(nums_inps):
            soln_result = self.optimized_approach(nums=nums_inps[indx],
                                                  n=n_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        print(f"Optimal Approach")
        return results, soln_result, test_fail

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
