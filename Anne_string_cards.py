# Anne has many red cards and black cards. He likes to play with cards and now he will place them in a horizontal line.
# Initially, there are no cards placed.
# Anne will perform the below operations any number of times until it exceeds N cards.
# Append A black cards at the back of the cards already placed. Then append B red cards 
# at the back.
# Now, the task is to find the total number of black cards among the first N cards placed 
# in the given order.

# Input Format

# The First line contains three integers N, A and B
# 1<=N<=10^18
# A,B>=0
# At least one of A and B are non zero

# N = 9
# b = 3
# r = 4

# bbbrrrr

n, b, r = map(int, input().split())
a = b
d = n//(b+r)  # 1
e = n % (b+r)  # 2 st[:2] bbbrrr
if e > b:
    f = e - b
    e = e - f
print(a*d+e)
