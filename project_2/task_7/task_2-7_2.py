sequences = ["ATATACGCGTA", "CTTCGGNGGA"]
for seq in sequences:
    print(f"Последовательность: {seq}")
    for nucleotide in seq:
        print(nucleotide)
    print("-" * 30)

print("Цикл выполнен")