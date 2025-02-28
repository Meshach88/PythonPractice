num = 45

binary_num = bin(num)[2:]
# binary_num = f"{num:b}"
# binary_num = format(num,'b')


binary_num.split('0')

print(max(map(len, binary_num.split('0'))))


