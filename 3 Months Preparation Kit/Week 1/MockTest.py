# Complete the 'findMedian' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.

def findMedian(arr):
    # Write your code here
    sortedArr = sorted(arr)
    print(sortedArr)
    midNum = len(sortedArr) // 2
    return sortedArr[midNum]