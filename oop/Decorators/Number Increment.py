def number_increment(nums):
    def increase():
        return [num + 1 for num in nums]

    return [num for num in increase()]
