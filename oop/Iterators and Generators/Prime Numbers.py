def is_prime(nums):
    for num in nums:
        divedable = 0
        for n in range(1,num+1):
            if num % n == 0:
                divedable += 1
        if divedable == 2:
            yield num


def get_primes(nums):
    return is_prime(nums)
