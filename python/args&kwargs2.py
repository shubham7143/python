def team(players, *today, **squad):
    print("today's", players, end=": ")
    for i in today:
        print(i, end=" ")

    print()

    for idx, i in squad.items():  # type: ignore
        print(idx, "=>", i)


squad = {'bat': ["rohit", "dhawan", "Kohli", "Rahul"], "Bowl": ["Jassi", "Bhuvi", "chahal",
                                                                "kuldeep", "shami"], 'all': ["jadeja", "hardik", "kedar", "yuvi"], 'wk': ["dk", "dhoni"]}
playing11 = ["rohit", "dhawan", "kohli", "rahul", "yuvi",
             "dhoni", "hardik", "bhuvi", "bumrah", "kuldeep", "chahal"]
# print(playing11)
# print(*playing11)
# print()
# print(squad)
# print(*squad)
# print(*squad.items())

team(11, *playing11, **squad)
