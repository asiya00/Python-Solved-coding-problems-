import math

count = 0
def game(n):
    global count
    if n <= 1:
        return count
    if int(math.log(n, 2)) == math.log(n, 2):
        count += 1
        game(n//2)
    else:
        temp = math.floor(math.log(n, 2))
        temp = 2**temp
        print(temp, n)
        n = n - temp
        print(n)
        count += 1
        game(n)
    return count
    # count = 0
    # while n > 1:
    #     if int(math.log(n, 2)) == math.log(n, 2):
    #         n = n//2
    #         count += 1
    #     else:
    #         temp = math.floor(math.log(n, 2))
    #         temp = 2**temp
    #         n = n - temp
    #         count += 1
    # return count

count = game(6)
print(count)

if count % 2:
    print("Louise")
else:
    print("Richard")

