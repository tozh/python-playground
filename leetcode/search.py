combo = [0, 0, 0]
nums = [1, 3, 5]

def search_combo(nums, target):

    combo = []
    if nums is []:
        return combo
    min = nums[0]
    max = nums[0]
    no_nagtive = True
    no_positive = True
    all_zero = True
    has_zero = False
    for num in nums:
        min = num if num < min else min
        max = num if num > max else max
        if num > 0:
            no_positive = False
            all_zero = False
        if num < 0:
            no_nagtive = False
            all_zero = False
        if num == 0:
            has_zero = True
    if no_nagtive and not all_zero:

        return combo

