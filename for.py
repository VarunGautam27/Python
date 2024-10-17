# prices = [10,20,30]
# total = 0
# for i in prices:
#     total = total + i
# print(f"total:{total}")

# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# numbers = [5, 2, 5, 2, 2]
# for i in numbers:
#     output = ''
#     for count in range(i):
#         output+='x'
#     print(output)

for i in range(9,0,-1):
    for j in range(i):
        print('x',end='')
    print()