'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


# Write your code here
def get_max_profit(coin_list, K):
    coin_list._merge_sort(,,
    if K == 0:
        return 0
    else:
        banned_coin = coin_list[0]
        sum, count = banned_coin, 1
        for coin in coin_list[1:]:
            if count>= int(K):
                break
            elif coin < banned_coin:
                banned_coin = coin
                count += 1
                sum += coin
        return sum

if __name__ == "__main__":
    Testcases = int(input())
    for test_case in range(Testcases):
        (N, K) = tuple(map(int, str(input()).split(" ")))
        coin_list = list(map(int, str(input()).split(" ")))
        print(get_max_profit(coin_list, K))