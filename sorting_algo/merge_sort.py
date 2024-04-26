"""This implements the merge sort algorithm"""


def merge(left_array, right_array):
    result = []
    i, j = 0, 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1
    if i == len(left_array) and j != len(right_array):
        while j < len(right_array):
            result.append(right_array[j])
            j += 1
    elif j == len(right_array) and i != len(left_array):
        while i < len(left_array):
            result.append(left_array[i])
            i += 1
    return result

def merge_sort(numbers: list):
    return _merge_sort(numbers=numbers, start=0, end=len(numbers))


def _merge_sort(numbers: list, start: int, end: int):
    if start == end+1:
        return numbers[start:end]
    else:
        mid = start + (end - start) // 2
        sorted_left = _merge_sort(numbers, start=start, end=mid)
        sorted_right = _merge_sort(numbers, start=mid + 1, end=end)
        return merge(sorted_left, sorted_right)


if __name__ == "__main__":
    a = [1, 13, 24]
    b = [2, 8, 10]
    merged_array = merge(a, b)
    assert merged_array == [1, 2, 8, 10, 13, 24], "Merging of arrays failed"

    a = [0]
    b = [1]
    merged_array = merge(a, b)
    assert merged_array == [0, 1], "Merging of arrays fail for single element arrays"

    a = [0]
    b = [0]
    merged_array = merge(a, b)
    assert merged_array == [0, 0], "Fails for same elements single element merging"

    a = [10, 14, 566, 980]
    b = [10003, 100044]
    merged_array = merge(a, b)
    assert merged_array == [10, 14, 566, 980, 10003, 100044], "Fails to merge unequally sized arrays"

    a = [19990]
    b = []
    merged_array = merge(a, b)
    assert merged_array == [19990], "Fails to merge single elem and empty array"

    array = [x for x in range(10, 0, -1)]
    sorted_arr = merge_sort(array)
    array.sort()
    print(sorted_arr)
    assert sorted_arr == array, "Sorting failed"

