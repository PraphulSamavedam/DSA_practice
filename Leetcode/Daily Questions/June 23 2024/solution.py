import heapq
from collections import deque
from typing import List


class Solution:
    """
    This class has various solutions for LeetCode question
    Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    """

    def brute_approach(self, nums: List[int], limit: int) -> int:
        """
        Brute Force Approach
        Time Complexity: O(n*n)
        Space Complexity: O(1)
        """
        result = 0
        for st in range(len(nums)):
            flag = True
            max_val = nums[st]
            min_val = nums[st]
            for ed in range(st + 1, len(nums)):
                if abs(nums[ed] - min_val) > limit or abs(
                        nums[ed] - max_val) > limit:
                    flag = False
                if flag:
                    # print(f"Valid: {nums[st:ed + 1]}")
                    result = max(result, ed - st + 1)
                    max_val = max(max_val, nums[ed])
                    min_val = min(min_val, nums[ed])
                else:
                    break
        return result

    def two_heap_approach(self, nums: List[int], limit: int) -> int:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        Approach: Two Heap based approach
        """
        result = 0
        lt = 0
        min_heap = []
        max_heap = []

        for rt in range(len(nums)):
            heapq.heappush(min_heap, (nums[rt], rt))
            heapq.heappush(max_heap, (-nums[rt], rt))

            while (-max_heap[0][0] - min_heap[0][0]) > limit:

                lt = min(max_heap[0][1], min_heap[0][1]) + 1

                while max_heap[0][1] < lt:
                    heapq.heappop(max_heap)

                while min_heap[0][1] < lt:
                    heapq.heappop(min_heap)

            result = max(result, rt - lt + 1)

        return result

    def two_queue_approach(self, nums: List[int], limit: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        Approach: Two Dequeue based approach
        """
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # Maintain the max_deque in decreasing order
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            # Maintain the min_deque in increasing order
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            # Check if the current window exceeds the limit
            while max_deque[0] - min_deque[0] > limit:
                # Remove the elements that are out of the current window
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

    def optimal_approach(self, nums: List[int], limit: int) -> int:
        """
        This method uses
        Time complexity: O(n)
        Space complexity: O(n)
        """
        return self.two_queue_approach(nums, limit)

    def my_approach(self, nums: List[int], limit: int) -> int:
        """
        Optimal Approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = 0
        lt = 0
        max_val = nums[0]
        min_val = nums[0]

        for rt in range(len(nums)):
            # print(f"Processing rt, num, min, max: {rt, nums[rt], min_val, max_val}")
            if abs(nums[rt] - min_val) <= limit and abs(
                    nums[rt] - max_val) <= limit:
                # print(f"Within limit lt, rt : {lt, rt, nums[lt:rt+1]}")
                result = max(result, rt - lt + 1)
                min_val = min(min_val, nums[rt])
                max_val = max(max_val, nums[rt])
                # print(f"Within limit min_val, max_val {min_val, max_val}")
            else:
                # # Either nums[lt] - min_val > limit or nums[lt] - max_val > limit
                # print(f"Outbounds {lt, rt, nums[rt], min_val, max_val}")
                # Move the lt pointer
                # Using the rt as min and max_val
                lt = rt
                min_val = nums[rt]
                max_val = nums[rt]
                while lt > 0 and abs(nums[lt] - min_val) <= limit and abs(
                        nums[lt] - max_val) <= limit:
                    min_val = min(min_val, nums[lt])
                    max_val = max(max_val, nums[lt])
                    lt -= 1
                lt += 1
                result = max(result, rt - lt + 1)

        return result

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        nums_inps = [[8, 2, 4, 7], [10, 1, 2, 4, 7, 2],
                     [4, 2, 2, 2, 4, 4, 2, 2],
                     [34, 24, 70, 27, 40, 26, 32, 47, 11, 36, 12, 97, 58, 12,
                      84, 74, 83, 44,
                      30, 50, 40, 6, 42, 24, 41, 75, 39, 32, 43, 13, 70, 79,
                      75, 77, 12, 32, 29, 3, 32, 52, 10, 35, 71, 10, 94, 10, 3,
                      82, 2, 38, 97, 46, 64, 61, 20, 13, 65, 100, 42, 10, 66,
                      86, 23, 23, 100, 20, 19, 41, 40, 14, 91, 66, 78, 38, 17,
                      27, 19, 70, 93, 5, 100, 41, 80, 87, 71, 96, 89, 27, 23,
                      39, 56, 69],
                     [1, 5, 6, 7, 8, 10, 6, 5, 6],
                     ]
        limit_inps = [4, 5, 0, 72, 4]
        results = [2, 4, 3, 15, 5]
        soln_results = []
        test_fail = []

        # Brute Force approach
        print(f"Brute Force Approach")
        for indx, _ in enumerate(nums_inps):
            soln_result = self.brute_approach(nums=nums_inps[indx],
                                              limit=limit_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # My approach
        print(f"My Approach")
        for indx, _ in enumerate(nums_inps):
            soln_result = self.my_approach(nums=nums_inps[indx],
                                           limit=limit_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        print(f"Two Heaps Approach")
        for indx, _ in enumerate(nums_inps):
            soln_result = self.two_heap_approach(nums=nums_inps[indx],
                                                 limit=limit_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        self.print_results(results, soln_results, test_fail)
        soln_results.clear()
        test_fail.clear()

        # Optimal approach
        print(f"Optimal Approach: Two deque approach")
        for indx, _ in enumerate(nums_inps):
            soln_result = self.optimal_approach(nums=nums_inps[indx],
                                                limit=limit_inps[indx])
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
