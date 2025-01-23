with open('example2.txt', 'w+') as writeFile:
    writeFile.write('This text was written into this file')
    writeFile.seek(0)
    print(writeFile.read())

# with open('example2.txt', 'r') as readFile:
#     print(readFile.read())


Lines = ['This is line 1\n', 'This is line 2\n', 'This is line 3\n']

with open('example3.txt','w') as file1:
    for line in Lines:
        file1.write(line)

with open('example3.txt','r') as file1:
    print(file1.read())

with open('example3.txt', 'a+') as file1:
    file1.write('An additional line \n')
    file1.seek(0)
    print(file1.read())

with open('example3.txt', 'r') as source_file:
    with open('example4.txt', 'w+') as destination_file:
        for line in source_file:
            destination_file.write(line)
        destination_file.seek(0)
        print(destination_file.read())