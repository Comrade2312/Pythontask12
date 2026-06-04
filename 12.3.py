import json

english_data = """
cat - кошка
dog - собака
home - домашняя папка, дом
mouse - мышь, манипулятор мышь
to do - делать, изготавливать
to make - изготавливать
"""

with open("en-ru.txt", 'w', encoding="utf-8") as file:
    file.write(english_data)

русс_англ = {}

with open("en-ru.txt", 'r', encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if " - " in line:
            eng, rus = line.split(" - ", 1)
        elif " – " in line:
            eng, rus = line.split(" – ", 1)
        else:
            continue
        for r in rus.split(", "):
            if r not in русс_англ:
                русс_англ[r] = []
            if eng not in русс_англ[r]:
                русс_англ[r].append(eng)

with open("ru-en.txt", 'w', encoding="utf-8") as file:
    for r in sorted(русс_англ.keys()):
        file.write(f"{r} – {', '.join(sorted(русс_англ[r]))}\n")

print(open("ru-en.txt", 'r', encoding="utf-8").read())
