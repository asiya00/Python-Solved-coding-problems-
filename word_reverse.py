def word_reverse(s):
    i = len(s)-1
    start = end = i+1
    while i >= 0:
        if s[i] == ' ':
            start = i+1
            while start != end:
                print(s[start], end="")
                start += 1
            print(" ", end="")
            end = i
        i -= 1
    start = 0
    while start != end:
        print(s[start], end="")
        start += 1


word_reverse("Asiya Pathan")
