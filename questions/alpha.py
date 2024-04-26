from math import inf


def best_time_to_buy_sell(arr: list[int]):
    """Leet code 121"""
    profit = 0
    if len(arr) <= 1:
        return 0

    max_holder = [0] * len(arr)
    max_holder[-1] = -inf
    for index in range(len(arr) - 2, -1, -1):
        max_holder[index] = max(arr[index + 1], max_holder[index + 1])

    for indx, num in enumerate(arr):
        current_profit = max_holder[indx] - num
        profit = max(profit, current_profit)
    return profit


def jumpy_game(array: list) -> bool:
    possible = True
    min_steps = 0
    for index in range(len(array) - 1, -1, -1):
        if array[index] >= min_steps:
            min_steps = 0
            possible = possible & True
        else:
            possible = possible & False
        min_steps += 1
    return possible


def __find_island(grid: list[list[int]], row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return
    else:
        if grid[row][col] == 1:
            grid[row][col] = 0
            __find_island(grid, row - 1, col)
            __find_island(grid, row + 1, col)
            __find_island(grid, row, col - 1)
            __find_island(grid, row, col + 1)


def getNumberOfIslands(grid: list[list[int]]):
    islands: int = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                __find_island(grid, row, col)
                islands += 1
    return islands


def max_subarray_sum(arr: list[int]) -> int:
    if len(arr) < 1:
        return -1
    curr_sum = arr[0]
    if len(arr) == 1:
        return curr_sum
    max_sum = curr_sum

    for num in range(1,len(arr), 1):
        curr_sum = max(0, curr_sum)
        curr_sum += arr[num]
        max_sum = max(max_sum, curr_sum)
    return max_sum


def longest_subarray_with_k(arr: list[int], target: int):
    """All positive values scenario"""
    left = 0
    right = 0
    max_length = 0
    total = 0
    while right < len(arr):
        total += arr[right]
        while (total > target) & (left <= right):
            total -= arr[left]
            left += 1
        if total == target:
            max_length = max(max_length, right - left + 1)
        right += 1
    return max_length


if __name__ == '__main__':
    # array = [0, 1, 4]
    # assert jumpy_game(array) is False
    # array = [4, 3, 2, 1, 0]
    # assert jumpy_game(array) is True
    # array = [4, 1, 0, 4, 0]
    # assert jumpy_game(array) is False
    # array = [4, 2, 0, 1, 0]
    # assert jumpy_game(array) is True
    grid = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert getNumberOfIslands(grid) == 1, "Fails"

    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    assert getNumberOfIslands(grid) == 3, "Fails"

    array = [1, 2, 3, 4, 5, 6, 3]
    assert best_time_to_buy_sell(array) == 5, "Fail"

    array = [4, 3, 1, 0]
    assert best_time_to_buy_sell(array) == 0, "Fail"
    assert max_subarray_sum(array) == 8, "Fails max subarray sum"

    array = [2, 9, 3, 10]
    assert best_time_to_buy_sell(array) == 8, "Fail"
    assert max_subarray_sum(array) == 24, "Fails max subarray sum"

    array = [5, -4, 2]
    assert max_subarray_sum(array) == 5, "Fails max subarray sum"

    array = [5, -4, 8]
    assert max_subarray_sum(array) == 9, "Fails max subarray sum"

    array = [-5, -4, -8]
    assert max_subarray_sum(array) == -4, "Fails max subarray sum"

    array = [-1, -40, -80000]
    assert max_subarray_sum(array) == -1, "Fails max subarray sum"

    array = [100, 200, 300, 450]
    print(longest_subarray_with_k(array, 300))

    # print(f"Max profit: {best_time_to_buy_sell(array)}")

