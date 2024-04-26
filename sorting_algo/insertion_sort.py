"""Implements the insertion sorting algorithm"""


def sort(numbers: list):
    """
    Space Complexity: O(1)
    Time Complexity:
        - Best Case: Already sorted list - O(N)
        - Worst Case: Reversely sorted list - O(N^2)
        - Average Case: O(N^2)
    Inplace: True
    """
    length = len(numbers)
    result = numbers.copy()

    for unsorted_index in range(1, length, 1):

        element = result[unsorted_index]
        index = unsorted_index - 1
        # print(f"Sorting {element} on {result}")
        while index >= 0 and result[index] > element:
            result[index], result[index+1] = result[index+1], result[index]
            index -= 1
    print(result)

    return result


if __name__ == "__main__":
    num_array = [1, 2, 3, 5, 6, 7, 10]

    sorted_array = sort(num_array)
    num_array.sort()
    assert sorted_array == num_array

    num_array = [7, 2, 3, 5, 6, 1, 10]
    sorted_array = sort(num_array)
    num_array.sort()
    assert sorted_array == num_array

    num_array = [10, 9, 8, 6, 4, 2, 0]
    sorted_array = sort(num_array)
    num_array.sort()
    assert sorted_array == num_array

    num_array = [4, 9, 8, 6, 4, 2, 0]
    sorted_array = sort(num_array)
    num_array.sort()
    assert sorted_array == num_array

    num_array = [-10, -9, 8, 6, 4, 2, 0]
    sorted_array = sort(num_array)
    num_array.sort()
    assert sorted_array == num_array
