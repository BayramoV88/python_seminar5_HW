# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст:\n")
print(f"Исходный текст: {text}")
new_text = "абв"
lst = [i for i in text.split() if new_text not in i]
print(f'Результат: {" ".join(lst)}')