def count_trailing_zeros(n):
    count = 0
    i = 5
    while n >= i:
        count += n // i
        i *= 5
    return count

n = int(input())
print(count_trailing_zeros(n))
