from typing import List


class Solution:

    def brute_approach(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Initial solution that I thought
        Time complexity: O(n * (max(bloomDay) - min(bloomDay) )
        Space complexity: O(1)
        """
        if m * k > len(bloomDay):
            return -1

        min_value = min(bloomDay)
        max_value = max(bloomDay)

        for x in range(min_value, max_value+1):
            bouquets = 0
            series = 0
            for bloom in bloomDay:
                if bloom <= x:
                    series += 1
                    if series >= k:
                        bouquets += 1
                        series = 0
                else:
                    series = 0
            if bouquets >= m:
                return x

    def base_approach(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Initial approach based on the binary search
        """
        if m * k > len(bloomDay):
            return -1
        # Possible to create the m bouquets of size k each have
        # to find the min number of days.

        min_val = min(bloomDay)
        max_val = max(bloomDay)

        if min_val == max_val:
            return min_val

        def get_bouquet_cnt(lst, val, bqt_sz):
            cnt = 0
            continuous = 0
            for indx, value in enumerate(lst):
                if value <= val:
                    continuous += 1
                else:
                    continuous = 0
                if continuous == bqt_sz:
                    cnt += 1
                    continuous = 0
            return cnt

        # Binary search to get to know the day we can make return the result
        def binary_search(min_value, max_value, lst, bqt_cnt, bqt_sz):
            mid_val = (min_value + max_value) // 2
            bouquet_cnt = get_bouquet_cnt(lst, mid_val, bqt_sz)
            if bouquet_cnt == bqt_cnt and \
                    get_bouquet_cnt(lst, mid_val - 1, bqt_sz) < bqt_cnt:
                return mid_val
            elif bouquet_cnt < bqt_cnt:
                min_value = mid_val + 1
            else:
                max_value = mid_val - 1
            return binary_search(min_value, max_value, lst, bqt_cnt, bqt_sz)

        return binary_search(min_value=min_val, max_value=max_val,
                             lst=bloomDay, bqt_cnt=m, bqt_sz=k)

    def better_approach(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Binary search based approach with lowered boilerplate.

        Time Complexity: O(n * log (max(bloomDay))
        Space Complexity: O(1)
        """
        min_val = 1
        max_val = max(bloomDay)
        ans = -1
        while min_val <= max_val:
            mid_val = min_val + (max_val - min_val) // 2
            bouquets = 0
            cntg = 0
            for value in bloomDay:
                if value <= mid_val:
                    cntg += 1
                    if cntg == k:
                        bouquets += 1
                        cntg = 0
                else:
                    cntg = 0

            if bouquets >= m:
                ans = mid_val
                max_val = mid_val - 1
            else:  # bouquets < k
                min_val = mid_val + 1
        return ans

    def testCases(self):
        """ This method has all the test cases along with desired answers"""
        bloomDay_inps = [[1, 10, 3, 10, 2], [1, 10, 3, 10, 2],
                         [7, 7, 7, 7, 12, 7, 7],
                         [1000000000, 1000000000]]
        m_inps = [3, 3, 2, 1]
        k_inps = [1, 2, 3, 1]
        results = [3, -1, 12, 1000000000]
        soln_results = []
        test_fail = []

        # Base approach
        print(f"Brute Force Approach")
        for indx, _ in enumerate(bloomDay_inps):
            soln_result = self.brute_approach(bloomDay=bloomDay_inps[indx],
                                              m=m_inps[indx], k=k_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        self.print_results(results, soln_results, test_fail)
        test_fail.clear()
        soln_results.clear()

        # Base approach
        print(f"Base binary Approach")
        for indx, _ in enumerate(bloomDay_inps):
            soln_result = self.base_approach(bloomDay=bloomDay_inps[indx],
                                             m=m_inps[indx], k=k_inps[indx])
            test_fail.append(soln_result == results[indx])
            soln_results.append(soln_result)
        self.print_results(results, soln_results, test_fail)
        test_fail.clear()
        soln_results.clear()

        # Optimal approach
        print(f"Better binary Approach")
        for indx, _ in enumerate(bloomDay_inps):
            soln_result = self.better_approach(bloomDay=bloomDay_inps[indx],
                                               m=m_inps[indx],
                                               k=k_inps[indx])
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
