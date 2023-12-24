import random
i = 0
score = 0
while (True):
    print("""Введите к б н для игры
        Если хотите выйти, напишите 0!""")
    a = input()
    if a == "0":
        break
    rnd = random.randint(1,3)
    if rnd == 1:
        print("к")
        i = "к"
    elif rnd == 2:
        print("б")
        i = "б"
    elif rnd == 3:
        print("н")
        i = "н"
print("Игра окончена!")
