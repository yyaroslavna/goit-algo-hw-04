import random
import timeit


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def timsort(arr):
    return sorted(arr)


random.seed(42)

data = {
    "Випадкові": random.sample(range(100000), 4000),
    "Відсортовані": list(range(4000)),
    "Зворотні": list(range(4000, 0, -1)),
    "Майже відсортовані": list(range(4000))
}


for _ in range(20):
    i = random.randint(0, 3999)
    j = random.randint(0, 3999)

    data["Майже відсортовані"][i], data["Майже відсортовані"][j] = (
        data["Майже відсортовані"][j],
        data["Майже відсортовані"][i]
    )


algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Timsort": timsort
}


print(f"{'Набір даних':<25} {'Insertion Sort':<20} {'Merge Sort':<20} {'Timsort':<20}")
print("-" * 85)

for data_name, numbers in data.items():
    results = []
    for algorithm in algorithms.values():
        times = timeit.repeat(
            lambda: algorithm(numbers.copy()),
            repeat=3,
            number=1
        )
        results.append(min(times))

    print(
        f"{data_name:<25} "
        f"{results[0]:<20.6f} "
        f"{results[1]:<20.6f} "
        f"{results[2]:<20.6f}"
    )
