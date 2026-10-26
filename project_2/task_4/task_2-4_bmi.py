weight = float(input("Введите ваш вес (кг): "))
height_cm = float(input("Введите ваш рост (см): "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

if bmi < 18.5:
    category = "Недостаточная масса тела"
elif bmi < 25.0:
    category = "Норма"
elif bmi < 30.0:
    category = "Избыточная масса тела"
else:
    category = "Ожирение"

print("\n--- Отчет о состоянии здоровья ---")
print(f"Рост:\t\t{height_cm:.1f} см")
print(f"Вес:\t\t{weight:.1f} кг")
print(f"Индекс массы тела:\t{bmi:.2f}")
print(f"Статус:\t\t{category}")