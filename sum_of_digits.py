def sum_of_digits(n, sum=0):
    if n < 1:
        return sum
    remainder = n % 10
    sum += remainder
    n = n//10
    return sum_of_digits(n, sum)


print(sum_of_digits(1032))
