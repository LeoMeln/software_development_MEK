total_capsules = int(input("Введите общее количество произведенных капсул: "))
pack_size = int(input("Введите количество капсул в одной упаковке: "))

full_packs = total_capsules // pack_size
remainder = total_capsules % pack_size

print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток капсул:\t\t{remainder}")