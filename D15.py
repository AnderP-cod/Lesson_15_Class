

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
print("Что вы хотите сделать")
print("1 Создать контактную книгу")

a = int(input("Нажмите 1 "))

if a == 1:
    print("Создаем контактную книгу")
    surname = str(input("Напишите Фамилию "))
    name = str(input("Напишите свое имя "))
    city = str(input("Напишите где вы живете "))
    email = str(input("Напишите свой email "))
    print("Мы создали контактную книгу")

print(" Посмотреть контактную книгу")

print("Что вы хотите сделать")
print("1 Посмотреть контакты")
print("2 Выбрать контакт")
print("3 Поменять данные")
print("4 Посмотреть город")
print("5 Посотреть емейл")
print("6 Вывести количество контактов")

choice = int(input("Выберите из списка 1 2 3 4 5 6"))

class Yura():
    surname_2 = "Москоленко"
    name_2 = "Юра"
    city_2 = "Киев"
    email_2 = "Yura2006@gmail.com"
class Alice():
    surname_3 = "Рыбкина"
    name_3 = "Алиса"
    city_3 = "Львов"
    email_3 = "Alice2000@gmail.com"

if choice == 1:
    print(surname)
    print(name)
    print(city)
    print(email)

elif choice == 2:
    print("Выберите анкету")
    print("1 ваша анкета")
    print("2 анкета Юра")
    print("3 анкета Алисы")
    b = int(input("1 , 2, 3 "))
    if b == 1:
        print(surname)
        print(name)
        print(city)
        print(email)
    elif b == 2:
        print(Yura.surname_2)
        print(Yura.name_2)
        print(Yura.city_2)
        print(Yura.email_2)
    elif b == 3:
        print(Alice.surname_3)
        print(Alice.name_3)
        print(Alice.city_3)
        print(Alice.email_3)

elif choice == 3:
    print("Какие данные вы хотите поменять")
    print("1 Фамилия")
    print("2 Имя")
    print("3 Город/село")
    print("4 email")

    c = int(input("1 , 2, 3, 4 "))

    if c == 1:
        surname = surname = str(input("Введите новую Фамилию"))
        print("Новая Фомилия",surname)
    elif c == 2:
        name = name = str(input("Введите новое Имя"))
        print("Новое Имя",name)
    elif c == 3:
        city = city = str(input("Введите новое Место прожывание"))
        print("Новое Место проживание",city)
    elif c == 4:
        email = email = str(input("Введите новый email"))
        print("Новый email",email)

elif choice == 4:
    print(city)

elif choice == 5:
    print(email)

elif choice == 6:
    print(surname)
    print(name)
    print(city)
    print(email)
    print()
    print(Yura.surname_2)
    print(Yura.name_2)
    print(Yura.city_2)
    print(Yura.email_2)
    print()
    print(Alice.surname_3)
    print(Alice.name_3)
    print(Alice.city_3)
    print(Alice.email_3)

    print(3)








