# The prime factors of 13195 are 5, 7, 13 and 29.
# 600851475143
# def check_prime(num):
#     for j in range(int(num**0.5)+1, 1, -1):
#         if num % j == 0:
#             return False
#     return True


# def prime_factors(n):
#     if check_prime(n):
#         return n
#     largest = 2
#     for i in range(3, (n//2)+1, 2):
#         if n % i == 0:
#             if check_prime(i):
#                 if largest < i:
#                     largest = i
#     return largest


# n = 600851475143
# print(prime_factors(n))

def largest_prime_factor(n):
    largest = 2
    while n % 2 == 0:
        n = n // 2

    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            largest = i
            n = n // i
    if n > 2:
        largest = n
    return largest


print(largest_prime_factor(600851475143))
