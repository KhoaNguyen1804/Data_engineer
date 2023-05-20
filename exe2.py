def two_sum(nums, target):
    num_map = {} 

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]

        num_map[num] = i

    return []  

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
target = 13

indices = two_sum(nums, target)
if indices:
    print(f"The indices are: {indices}")
else:
    print("No solution found.")
