text = input()
code = input()


main = [0] * len(text)
for i in range(len(text)): 
    main[i] = [0] * 3

print(main)
j = 0
for i in range(len(text)):
    main[i][0] = text[i]
    if j < (len(code)):
        main[i][1] = code[j]
        j += 1
    else:
        j = 0
        main[i][1] = code[0]
        j += 1
    
print(main)



for i in range(len(text)):
    num = 1071 + (ord(main[i][0]) - 1071) + (ord(main[i][1]) - 1071) - 1
    if num > 1103:
        main[i][2] = chr(num - 32)
    else:
        main[i][2] = chr(num)


fin = ''
for i in range(len(text)):
    fin = fin + main[i][2]
print(fin)