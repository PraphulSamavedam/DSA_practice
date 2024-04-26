class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while(n>0):
            bit = n % 2
            n = n // 2
            if bit == 1:
                result += 1
        return result


if __name__ == "__main__":
    sol = Solution()
    number_list = -3
    print(sol.hammingWeight(number_list))

    number_list = 16
    print(sol.hammingWeight(number_list))

    number_list = 32
    print(sol.hammingWeight(number_list))