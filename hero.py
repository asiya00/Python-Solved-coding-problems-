def hero(bullets, dragons):
    return bullets >= 2*dragons


print(hero(100, 40))


def square_sum(arr):
    return sum(i**2 for i in arr)


print(square_sum([1, 2, 16, 14]))
