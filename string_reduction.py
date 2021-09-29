def minDeletions(X, i, j):
 
    # base condition
    if i >= j:
        return 0
 
    # if the last character of the string is the same as the first character
    if X[i] == X[j]:
        return minDeletions(X, i + 1, j - 1)
 
    # otherwise, if the last character of the string is different from the
    # first character
 
    # 1. Remove the last character and recur for the remaining substring
    # 2. Remove the first character and recur for the remaining substring
 
    # return 1 (for remove operation) + minimum of the two values
 
    return 1 + min(minDeletions(X, i, j - 1), minDeletions(X, i + 1, j))
 
 
if __name__ == '__main__':
 
    X = "bbeadcebfp"
    n = len(X)
 
    print("The minimum number of deletions required is", minDeletions(X, 0, n - 1))