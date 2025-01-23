records = []
lowest = float('inf')
second_lowest = float('inf')
second_lowest_students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])
for record in records:
    if record[1] < lowest:
        second_lowest = lowest
        lowest = record[1]
    elif record[1] < second_lowest and record[1] != lowest:
        second_lowest = record[1]
    
for record in records:
    if record[1] == second_lowest:
        second_lowest_students.append(record[0])
second_lowest_students.sort()
for name in second_lowest_students:
    print(name)
    
# A better solution
   
# if __name__ == "__main__":
#     records = []

#     # Collect input
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append((name, score))

#     # Find the two lowest unique scores
#     scores = sorted({score for _, score in records})
#     if len(scores) < 2:
#         print("No second lowest score available")
#         exit()
    
#     second_lowest = scores[1]

#     # Get all names with the second lowest score
#     second_lowest_students = sorted([name for name, score in records if score == second_lowest])

#     # Print names in alphabetical order
#     print("\n".join(second_lowest_students))
