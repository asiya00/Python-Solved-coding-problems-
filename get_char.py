import string


def get_char(n):
    a = string.ascii_letters
    if n in range(65, 92):
        return a[((n - 65) % 26)]
    else:
        return a[(n - 97) % (26+(52-26)) + 26]


n = int(input())
print(get_char(n))
