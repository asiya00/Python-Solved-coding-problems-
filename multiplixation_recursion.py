def multiply(a, b):
    if b == 0:    # base condn
        return 0
    if b == 1:    # base condn
        return a
    return a + multiply(a, b - 1)  # induction and hypothesis
print(multiply(0, 1))
