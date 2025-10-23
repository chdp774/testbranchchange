values = []
flag = False

while not flag:
    val = int(input('Enter the expeses: '))
    values.append(val)
    if val == 0:
        flag = True

print('Total exp: ', sum(values))
print('Max expense: ', max(values))

