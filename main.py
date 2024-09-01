sum = 0
i = 0
l = []
while True:
    inp = input(f'enter {i + 1} item prize or  press q or Q to quit :')

    if inp == 'q':
        break
    else:
        l.append(inp)
        sum += int(inp)
        i += 1


for j in range(0, i):
    print(j + 1, '.', l[j])
    j += 1

print('total prize of items is:', sum)
