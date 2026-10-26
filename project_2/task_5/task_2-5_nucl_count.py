dna_seq = input("Введите последовательность ДНК: ")
upper_seq = dna_seq.upper()

print(f"\nПоследовательность в верхнем регистре: {upper_seq}")
count_a = upper_seq.count('A')
count_t = upper_seq.count('T')
count_g = upper_seq.count('G')
count_c = upper_seq.count('C')

length = len(upper_seq)

if length > 0:
    perc_a = (count_a / length) * 100
    perc_t = (count_t / length) * 100
    perc_g = (count_g / length) * 100
    perc_c = (count_c / length) * 100
else:
    perc_a = perc_t = perc_g = perc_c = 0.0

print("\nПодсчёт нуклеотидов:")
print(f"A: {count_a}")
print(f"T: {count_t}")
print(f"G: {count_g}")
print(f"C: {count_c}")

print(f"\nПроцентное содержание:")
print(f"A: {perc_a:.2f}%")
print(f"T: {perc_t:.2f}%")
print(f"G: {perc_g:.2f}%")
print(f"C: {perc_c:.2f}%")

print(f"\nОбщая длина: {length} нуклеотидов")