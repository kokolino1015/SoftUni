def recursive_power(num, nums, res=1):
    res *= num
    if nums == 1:
        return res
    return recursive_power(num, nums-1, res=res)

