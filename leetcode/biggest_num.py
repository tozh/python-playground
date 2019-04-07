def digits(a):
    result = []
    while a > 0:
        result.append(a % 10)
        a //= 10
    return result[::-1]


def cmp(a, b):
    assert isinstance(a, int)
    assert isinstance(b, int)
    digits_a = digits(a)
    digits_b = digits(b)
    if len(digits_a) > len(digits_b):
        shorter_len = len(digits_b)
        a_shorter = -1
    elif len(digits_a) < len(digits_b):
        shorter_len = len(digits_a)
        a_shorter = 1
    else:
        shorter_len = len(digits_a)
        a_shorter = 0

    for i in range(shorter_len):
        if digits_a[i] > digits_b[i]:
            return 1
        elif digits_a[i] < digits_b[i]:
            return -1

    if a_shorter == 0:
        return 0
    elif a_shorter == 1:
        return -(digits_a[0]-digits_b[shorter_len])
    else:
        return -(digits_b[0] - digits_a[shorter_len])


l = [456, 45]

print(l.sort())

