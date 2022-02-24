def code_vi(text, code):
    main = [0] * len(text)
    for i in range(len(text)): 
        main[i] = [0] * 3
    
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
    
    for i in range(len(text)):
        num = 1071 + (ord(main[i][0]) - 1071) + (ord(main[i][1]) - 1071) - 1
        if num > 1103:
            main[i][2] = chr(num - 32)
        else:
            main[i][2] = chr(num)
    
    fin = ''
    for i in range(len(text)):
        fin = fin + main[i][2]
    return(fin)    
    
    
def de_code_vi(text, code):
    main = [0] * len(text)
    for i in range(len(text)): 
        main[i] = [0] * 3
    
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
    
    for i in range(len(text)):
    num = 1071 + 1 + (ord(main[i][0])) - (ord(main[i][1]))
    if num > 1103:
        main[i][2] = chr(num - 32)
        print(num)
    elif num < 1072:
        main[i][2] = chr(num + 32)
    else:
        main[i][2] = chr(num)
        print(num)
    
    fin = ''
    for i in range(len(text)):
        fin = fin + main[i][2]
    return(fin)   




print('���� �� ������ ����������� ��������� - ������� 1, ���� �� ������ ������������ ��������� - ������� 2')
c = int(input())
if c == 1:
    print('������� �����, ������� ������ �����������:')
    text = input()
    print('������� ����:')
    code = input()    
    print('��� ���� ������������� ���������:)')
    print(code_vi(text, code))
elif c == 2:
    print('������� �����, ������� ������ ������������:')
    text = input()
    print('������� ����:')
    code = input()    
    print('��� ���� �������������� ���������:)')
    print(de_code_vi(text, code))
else:
    print("����������� ����")
    
