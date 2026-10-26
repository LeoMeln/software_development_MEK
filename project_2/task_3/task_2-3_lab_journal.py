import textwrap

name = input("Введите ФИО исследователя: ")
date = input("Введите дату эксперимента (ДД.ММ.ГГГГ): ")
exp = input("Введите название эксперимента: ")
conclusion = input("Введите вывод по эксперименту: ")

width = 50
inner_width = width - 4
border = "+" + "-" * (width - 2) + "+"

with open("journal.txt", "w", encoding="utf-8") as f:
    f.write(f"{border}\n")
    f.write(f"| Электронный лабораторный журнал{' ' * (inner_width - len('Электронный лабораторный журнал'))} |\n")
    f.write(f"{border}\n")
    
    fields = [
        ("ФИО исследователя", name),
        ("Дата", date),
        ("Эксперимент", exp)
    ]
    
    for label, value in fields:
        line_content = f"{label:<17}: {value}"
        f.write(f"| {line_content.ljust(inner_width)} |\n")
        
    f.write(f"{border}\n")
    f.write("| Вывод:\n")
    
    wrapped_lines = textwrap.wrap(conclusion, width=inner_width)
    for line in wrapped_lines:
        f.write(f"| {line.ljust(inner_width)} |\n")
        
    f.write(f"{border}\n")

print("Журнал успешно сохранён в journal.txt")