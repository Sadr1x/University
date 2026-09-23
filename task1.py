
numbers = [10, 20, 30, 40, 50]
print("Початковий список:", numbers)
#Індиксація
print("Перший елемент:", numbers[0])
print("Останній елемент:", numbers[-1])
#Зріз
print("Зріз [1:3]:", numbers[1:3])
print("Перші 2 елементи:", numbers[:2])
print("Зріз із кроком 2:", numbers[::2])
#Зміна на місці
numbers.append(60)
print("Після додавання 60:", numbers)
numbers.pop(0)
print("Після видалення першого:", numbers)
numbers[0:2] = [99, 99]
print("Після заміни перших двох:", numbers)
