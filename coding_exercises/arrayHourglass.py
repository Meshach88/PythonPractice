def max_hourglass_sum (arr):
    max_sum = float('-inf')
    for i in range(4):
        for j in range(4):
            current_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            max_sum = max(current_sum, max_sum)
