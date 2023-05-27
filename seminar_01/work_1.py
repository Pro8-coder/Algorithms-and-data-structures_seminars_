"""
Есть массив чисел lst и число n. Надо найти индексы 2х чисел в массиве, сумма
которых даёт число n. Гарантируется что в массиве существует ровно одна пара
чисел соответствующих условию.
"""


def find_sum_indexes(nums, target):
    hash_table = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[nums[i]] = i


lst = [2, 7, 11, 15]
n = 9
indexes = find_sum_indexes(lst, n)
print(indexes)
