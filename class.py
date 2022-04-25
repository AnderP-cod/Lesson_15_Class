

"""Використовуючи класи Написати програму - контактную книгу

    Базовий прикладных данных, які містяться про користувача:
            тел_номер #380984567831 имя #Сергей фамилия #
            Шостак
            город
            /село #Ровно
            email в формате first_last.city@city.com    #Shostak_Serhii.Rivne@Rivne.com

    Повинна вміти програма:
    - Доставить контакт користувача
    - Выдать контакт користувача
    - Вызмінювати данные користувача - Пошук користувачів
    по городу/селу
    - Пошук користувача по емейлу
    - Вывести колількість контактів
"""

print("Создаем контактную книгу")

class Newhuman:
	number = 0
	def __init__(self,surname,name,city,email):
		self.surname = surname
		self.name = name
		self.city = city
		self.email = f"{email}@email.com"
		Newhuman.number += 1
class Newbook1:
	def __init__(self,surname):
		self.surname = surname
class Newbook2:
	def __init__(self,name):
		self.name = name
class Newbook3:
	def __init__(self,city):
		self.city = city
class Newbook4:
	def __init__(self,email):
		self.email = f"{email}@email.com"


human = Newhuman(input("Напишите фамилмю "),input("Напишите имя "),input("Напишите город "),input("Напишите email "))
print("Вы создали контактную книгу")

print()

print("Что вы хотите сделать")
print("1 Посмотреть контактную книгу")
print("2 Поменять информацию контактной книги")
print("3 Посмотреть город")
print("4 Посотреть емейл")
print("5 Вывести количество контактов")

item2 = int(input("Нажмите 1 , 2 , 3 , 4 , 5"))

if item2 == 1:
	print(f"Фамилия {human.surname} ,Имя {human.name} ,Город {human.city} ,email {human.email},")
elif item2 == 2:
	print("Какую информацию хотите поменять")
	print("1 Фамилию")
	print("2 Имя")
	print("3 Город")
	print("4 Email")
	book = int(input("Нажмите 1 , 2 , 3 , 4"))
	if book == 1:
		book1 = Newbook1(input("Напишите Фамилию"))
		print(f"{book1.surname}")
	elif book == 2:
		book2 = Newbook2(input("Напишите Имя"))
		print(f"{book2.name}")
	elif book == 3:
		book3 = Newbook3(input("Напишите Город"))
		print(f"{book3.city}")
	elif book == 4:
		book4 = Newbook4(input("Напишите Email"))
		print(f"{book4.email}")
elif item2 == 3:
	print(f"Город {human.city}")
elif item2 == 4:
	print(f"email {human.email}")
elif item2 == 5:
	print(Newhuman.number)

	