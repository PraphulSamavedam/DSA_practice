from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        summation_value, carry = 0, 1
        result = []
        for index in range(len(digits) - 1, -1, -1):
            summation_value = digits[index] + carry
            carry = summation_value % 10
            result.insert(0, carry)
            carry = summation_value // 10
        if carry != 0:
            result.insert(0, carry)
        return result


if __name__ == "__main__":
    sol = Solution()
    number_list = [1, 2, 3]
    print(sol.plusOne(number_list))

    number_list = [9, 9]
    print(sol.plusOne(number_list))

    number_list = [9]
    print(sol.plusOne(number_list))