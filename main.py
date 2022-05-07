a = []
candidates = [
    {"name": "Vasya", "scores": {"math": 66, "russian_language": 52, "computer_science": 30}, "extra_scores": 2},
    {"name": "Vova", "scores": {"math": 69, "russian_language": 50, "computer_science": 30}, "extra_scores": 1},
    {"name": "Vanya", "scores": {"math": 60, "russian_language": 53, "computer_science": 35}, "extra_scores": 0}
]

for i in candidates:
    b = []
    d, h = 0, 0
    b.append(i["name"])
    print(b)
    for n in i["scores"]:
        c = i["scores"][n]
        h += c
    d = h - i["scores"]["russian_language"]
    h += i['extra_scores']
    b.append(h)
    b.append(d)
    a.append(b)
    if len(a) == 2 and a[0][1] <= a[-1][1]:
        if a[0][1] < a[-1][1]:
            a[0], a[- 1] = a[- 1], a[0]
        else:
            if a[0][2] < a[- 1][2]:
                a[0], a[- 1] = a[- 1], a[0]
    elif len(a) > 3:








print(a)
