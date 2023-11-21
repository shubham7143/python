# positional arguments args & kwargs

def team(players, *today, **squad):
    print("today's", players, end=": ")
    for i in today:
        print(i, end=" ")

    print()

    for idx, i in squad.items():  # type: ignore
        print(idx, "=>", i)


squad = {"pace bowlers": ["bhuvi", "bumrah", "shami"], "spin bowlers": ["kuldeep", "yuzi"],
         "all rounders": ["hardik", "jadeja", "jadhav", "shankar"],
         "batsmen": ["rohit", "dhawan", "rahul", "kohli"], "keepers": ["pant", "dk"]}

playing11 = ["rohit", "dhawan", "kohli", "rahul", "pant", "hardik",
             "jadeja", "bhuvi", "kuldeep", "bumrah", "yuzi"]

team(11, *playing11, **squad)
