s = "geeksforgeeks"


def check_anagram_palindrome(s):
    count = [0 for i in range(256)]

    for x in s:
        count[ord(x)] += 1

    odd_count = 0
    for x in s:
        if count[ord(x)] & 1:
            odd_count += 1
        if odd_count > 1:
            return "False"
    return "True"


print(check_anagram_palindrome(s))
