def get_negative(nums):
    negative = list(filter(lambda x: x < 0, nums))
    print(sum(negative))
    return negative


def get_positive(nums):
    positive = list(filter(lambda x: x > 0, nums))
    print(sum(positive))
    return positive


def result(negative, positive):
    if sum(positive) < abs(sum(negative)):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


nums = [int(x) for x in input().split(" ")]
result(get_negative(nums), get_positive(nums))
