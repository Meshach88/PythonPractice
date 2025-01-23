# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     arr1 = [ x for x in arr]
#     arr1 = sorted(arr1)
#     maxNum = max(arr1)
#     arr2 = [x for x in arr1 if x!=maxNum]
#     print(arr2[-1])

# Better solution
if __name__ == '__main__':
    n = int(input())  # Number of elements (not strictly used here)
    arr = map(int, input().split())  # Input the elements
    unique_numbers = list(set(arr))  # Remove duplicates by converting to a set
    if len(unique_numbers) < 2:  # Check if there are at least two unique numbers
        print("No second largest number")
    else:
        unique_numbers.sort(reverse=True)  # Sort in descending order
        print(unique_numbers[1])  # Second largest number

print("Hello")