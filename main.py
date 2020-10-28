
mylist = ['5', '6', '0', '4', '2']

userChoice = 0
while userChoice <= 5:
	print('Меню:')
	print('1. Вывести на экран все значения')
	print('2. Добавить значение')
	print('3. Удалить значение')
	print('4. Найти значение')
	print('5. Отсортировать значения')
	print('6. Выйти')
	guess = int(input('Введите опцию: '))
	if guess == 1:
		print(mylist)
		continue
	elif guess == 2:
		print(mylist)
		x = input('Введите название чтобы добаить значение: ')
		mylist.append(x)
		print('Новый список: ', mylist)
		continue
	elif guess == 3:
		print('Список: ', mylist)
		x = input('Введите название чтобы удалить значение: ')
		mylist.remove(x)
		print(mylist)
		continue
	elif guess == 5:
		mylist.sort()
		print('Сортировка по алфавиту: ', mylist)
		continue
	else:
		break