def get_nums(type_nums, nums):
    if "Odd" in type_nums:
        print(sum([x for x in nums if x % 2 != 0]) * len(nums))
    elif "Even" in type_nums:
        print(sum([x for x in nums if x % 2 == 0]) * len(nums))


type_nums = input()
nums = [int(x) for x in input().split(" ")]
get_nums(type_nums, nums)
