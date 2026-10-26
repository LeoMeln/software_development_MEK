donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
patient = input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()
valid_groups = {"I", "II", "III", "IV"}

if donor not in valid_groups or patient not in valid_groups:
    print("Ошибка: указана несуществующая группа крови.")
else:

    if donor == "I" or donor == patient:
        print(f"Переливание крови от донора ({donor}) пациенту ({patient}) ВОЗМОЖНО.")
    else:
        print(f"Переливание крови от донора ({donor}) пациенту ({patient}) ПРОТИВОПОКАЗАНО.")