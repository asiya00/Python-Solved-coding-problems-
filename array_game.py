# # Python3 Program to find minimum
# # number of operations to make all
# # array Elements equal

# # Function to find minimum number
# # of operations to make all array
# # Elements equal
# def countMinimumMoves(arr, n, k) :

#   # Check if it is possible or not
#   # That is if all the elements from
#   # index K to N are not equal
#   for i in range(k - 1, n) :
#       if (arr[i] != arr[k - 1]) :
#           return -1

#   # Find minimum number of moves
#   for i in range(k - 1, -1, -1) :
#       if (arr[i] != arr[k - 1]) :
#           return i + 1

#   # Elements are already equal
#   return 0

# # Driver Code
# if __name__ == "__main__" :

#   arr = [5, 6, 8, 8, 5]
#   K = 4

#   n = len(arr)

#   print(countMinimumMoves(arr, n, K))

# # This code is contributed by Ryuga

# Python 3 for finding minimum
# operation required

# function for finding min
# operation
def minOp(arr, n):
    sm = sum(arr)
    small = min(arr)
    minOperation = sm - (n * small)
    return minOperation


arr = [2, 2, 2]
n = len(arr)
print("Minimum Operation = ", minOp(arr, n))
