X=int(input('^ '))
if X==1:
    print("Написать программу поиска самого длинного слова в строке, \nразделенной пробелами.")
    slo=str((input('Введите слова: ')).strip()).split(" ")
    l1=len(slo)
    slov2=len(slo[0])
    for i in range(l1):
        if slov2<=len(slo[i]):
            slov2=len(slo[i])
            ma=slo[i]
    print("Самое длинное слово: ",ma,len(ma),'= букв')
elif X==2:
    print("Написать программу поиска самого длинного слова в строке, \nразделенной точкой запятой.")
    slo=str((input('Введите слова: ')).strip()).split(';')
    l1=len(slo)
    slov2=len(slo[0])
    for i in range(l1):
        if slov2<=len(slo[i]):
            slov2=len(slo[i])
            ma=slo[i]
    print("Самое длинное слово: ",ma,len(ma),'= букв')
elif X==3:
    print('Написать программу самого короткого слова который выделяется \nзнаком который пользователь вводит в интерактивном режиме')
    znak=input('Введите знак: ')
    slo=str((input('Введите слова: ')).strip()).split(znak)
    l1=len(slo)

    slov2=len(slo[0])
    for i in range(l1):
        if slov2>=len(slo[i]):
            slov2=len(slo[i])
            mi=slo[i]
    print("Самое короткое слово: ",mi,len(mi),'= букв')
elif X==4:
    print('Написать программу которое находит введенное слово в строке \nкоторое также вводится пользователем в интерактивном режиме ')
    slo=str((input('Введите слова: ')).strip()).split(' ')
    slovoo=str(input("Введите слово которое хотите найти: "))
    l1=len(slo)
    for i in range(l1):
        if slo[i]==slovoo:
            print('Это ',i+1,"- тое слово")
            break
    else:
        print("Такоего слово нет в предложении!")
elif X==5:
    print('Посчитать количество слов в предложении которое вводит пользователь')
    slo=str((input('Введите слова: ')).strip()).split(' ')
    l1=len(slo)
    print('В предлодении ',l1,' слов')
