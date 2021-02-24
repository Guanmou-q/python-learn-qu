number = 1
while number < 100:
    with open('1-99.txt', 'a+') as fp:
        fp.write(str(number) + '\n')
    number = int(number) + 1
