# 2. Напишите функцию, которая проверяет: является ли слово палиндромом

def palindrome(data):
    data = data.replace(' ', '').lower()
    stroka = str(data)
    if stroka == stroka[::-1]:
        return print("Палиндром")
    else:
        return print("Не палиндром")

vvod = input("Введите слово -> ")
palindrome(vvod)

