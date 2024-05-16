with open("ilk_fayl.txt", "w") as f:
    f.write("Nonvenomous snakes either swallow prey alive or kill by constriction.")

with open("ilk_fayl.txt", "r") as f:
    first_line = f.readline().upper()

with open("ikinci_fayl.txt", "w") as f:
    f.write(first_line)
