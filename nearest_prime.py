def isPrime(n):
    if(n == 1 or n == 0):
        return False
    for i in range(2, int(n**(0.5))+1):
        if(n % i == 0):
            return False
    return True


def nearest_prime(n):
    di = {}
    left = 0
    right = 0
    count = 0
    num = n - 1
    while count < 5 and left < 3:
        if isPrime(num):
            di[num] = n - num
            left += 1
            count += 1
        num = num - 1
        if num == 0:
            break

    num2 = n + 1
    while count < 5 or right < 2:
        if isPrime(num2):
            di[num2] = abs(n - num2)
            right += 1
            count += 1
        num2 = num2 + 1
    temp = 0
    maximum = 0
    for key, value in di.items():
        if maximum < value:
            maximum = value
            if temp != key:
                temp = key

    return temp


print(nearest_prime(62))
