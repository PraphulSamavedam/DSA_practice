class Solution:
    def getSqrdDigitsSum(self, n: int) -> int:
        string_format = str(n)
        result = 0
        for digit in string_format:
            result += (int(digit) * int(digit))
        return result

    def isHappy(self, n: int) -> bool:
        track = dict()
        num = self.getSqrdDigitsSum(n)
        while num not in track:
            track[num] = True
            num = self.getSqrdDigitsSum(num)
        if num == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    number = 1111111
    sol = Solution()
    print(sol.isHappy(number))
