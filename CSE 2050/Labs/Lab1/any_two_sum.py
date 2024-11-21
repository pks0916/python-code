def any_two_sum(numbers, total):
    """checks if any two number in the list add up to the total"""
    seen_nums = []
    for num in numbers:
        num_works = total - num
        if num_works in seen_nums:
            return True
        seen_nums.append(num)
    return False