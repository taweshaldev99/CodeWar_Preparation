#import array
def differenceDiagonal(arr):
    primaryDiagonal=0
    secondaryDiagonal=0

    n=len(arr)
    for i in range(n):
        primaryDiagonal +=arr[i][i]
        secondaryDiagonal +=arr[i][n-1-i]
    return abs(primaryDiagonal-secondaryDiagonal)
matrix=[
    [3,4,5],
    [6,7,8],
    [1,2,3]
]
print(differenceDiagonal(matrix))
    

