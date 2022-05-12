a = []
y = []
candidates = [
    {"name": "Vasya", "scores": {"math": 66, "russian_language": 52, "computer_science": 35}, "extra_scores": 12},
    {"name": "Vova", "scores": {"math": 90, "russian_language": 53, "computer_science": 30}, "extra_scores": 1},
    {"name": "Vanya", "scores": {"math": 69, "russian_language": 50, "computer_science": 30}, "extra_scores": 1},
    {"name": "Vano", "scores": {"math": 60, "russian_language": 59, "computer_science": 39}, "extra_scores": 5},
    {"name": "Vanka", "scores": {"math": 69, "russian_language": 50, "computer_science": 31}, "extra_scores": 1},
    {"name": "Vlad", "scores": {"math": 60, "russian_language": 50, "computer_science": 30}, "extra_scores": 5},
    {"name": "Vadim", "scores": {"math": 61, "russian_language": 50, "computer_science": 30}, "extra_scores": 5},
    {"name": "Vika", "scores": {"math": 60, "russian_language": 58, "computer_science": 40}, "extra_scores": 5},
    {"name": "Vovan", "scores": {"math": 59, "russian_language": 58, "computer_science": 41}, "extra_scores": 5},
    {"name": "Vasya", "scores": {"math": 66, "russian_language": 52, "computer_science": 35}, "extra_scores": 12},
    {"name": "Vova", "scores": {"math": 90, "russian_language": 53, "computer_science": 30}, "extra_scores": 1},
    {"name": "Vanya", "scores": {"math": 69, "russian_language": 50, "computer_science": 33}, "extra_scores": 1},
    {"name": "Vano", "scores": {"math": 60, "russian_language": 59, "computer_science": 39}, "extra_scores": 5},
    {"name": "Vanka", "scores": {"math": 69, "russian_language": 50, "computer_science": 33}, "extra_scores": 1},
    {"name": "Vlad", "scores": {"math": 60, "russian_language": 50, "computer_science": 30}, "extra_scores": 5},
    {"name": "Vadim", "scores": {"math": 61, "russian_language": 50, "computer_science": 30}, "extra_scores": 5},
    {"name": "Vika", "scores": {"math": 60, "russian_language": 58, "computer_science": 40}, "extra_scores": 5},
    {"name": "Vovan", "scores": {"math": 59, "russian_language": 58, "computer_science": 41}, "extra_scores": 5},
    {"name": "Vasya", "scores": {"math": 66, "russian_language": 52, "computer_science": 35}, "extra_scores": 12},
    {"name": "Vova", "scores": {"math": 90, "russian_language": 53, "computer_science": 30}, "extra_scores": 1},
    {"name": "Vanya", "scores": {"math": 69, "russian_language": 50, "computer_science": 33}, "extra_scores": 1},
    {"name": "Vano", "scores": {"math": 60, "russian_language": 59, "computer_science": 39}, "extra_scores": 5},
    {"name": "Vanka", "scores": {"math": 69, "russian_language": 50, "computer_science": 33}, "extra_scores": 1},
    {"name": "Vlad", "scores": {"math": 60, "russian_language": 50, "computer_science": 30}, "extra_scores": 5},
    {"name": "Vadim", "scores": {"math": 61, "russian_language": 50, "computer_science": 30}, "extra_scores": 5},
    {"name": "Vika", "scores": {"math": 60, "russian_language": 58, "computer_science": 40}, "extra_scores": 5},
    {"name": "Vovan", "scores": {"math": 59, "russian_language": 58, "computer_science": 41}, "extra_scores": 5}

]

for i in candidates:
    b = []
    d, h = 0, 0
    b.append(i["name"])
    for n in i["scores"]:
        c = i["scores"][n]
        h += c
    d = h - i["scores"]["russian_language"]
    h += i['extra_scores']
    b.append(h)
    b.append(d)
    a.append(b)
    if len(a) > 1:
        for k in range(len(a)-1, 0, -1):
            if a[k][1] > a[k-1][1] or (a[k][1] == a[k-1][1] and a[k][2] > a[k-1][2]):
                a[k], a[k - 1] = a[k - 1], a[k]
    if len(a) > 3 and (a[2][1] > a[3][1] or (a[2][1] == a[3][1] and a[2][2] > a[3][2])):
        a = a[:3]
    elif len(a) > 3:
        for i in range(2, len(a)-1):
            if a[i][1] > a[i+1][1] or (a[i][1] == a[i+1][1] and a[i][2] > a[i+1][2]):
                a = a[:i+1]
if len(a) > 3:
    for k in range(len(a) - 1, 0, -1):
        s = 1
        if a[k][1] == a[k - 1][1] and a[k][2] == a[k - 1][2]:
            s += 1
        else:
            break
        y = a[len(a)-s:]
print(a)

def find_top_20(x):
    a = []
    y = []
    for i in candidates:
        b = []
        q, d, h = 0, 0, 0
        b.append(i["name"])
        for n in i["scores"]:
            c = i["scores"][n]
            h += c
        d = h - i["scores"]["russian_language"]
        h += i['extra_scores']
        q = i["scores"]["computer_science"]
        b.append(h)
        b.append(d)
        b.append(q)
        a.append(b)
        if len(a) > 1:
            for k in range(len(a) - 1, 0, -1):
                if a[k][1] > a[k - 1][1] or (a[k][1] == a[k - 1][1] and a[k][2] > a[k - 1][2]):
                    a[k], a[k - 1] = a[k - 1], a[k]
        if len(a) > 20 and (a[19][1] > a[20][1] or (a[19][1] == a[20][1] and a[19][2] > a[20][2])):
            a = a[:20]
        elif len(a) > 20:
            for i in range(19, len(a) - 1):
                if a[i][1] > a[i + 1][1] or (a[i][1] == a[i + 1][1] and a[i][2] > a[i + 1][2]):
                    a = a[:i + 1]
    if len(a) > 20:
        w = []
        s = 1
        for k in range(len(a) - 1, 0, -1):
            if a[k][1] == a[k - 1][1] and a[k][2] == a[k - 1][2]:
                s += 1
            else:
                break
            y = a[len(a) - s:]
        for k in range(len(y) - 1, 0, -1):
            if y[k][3] > y[k - 1][3]:
                y[k], y[k - 1] = y[k - 1], y[k]
        z = []
        z.append(y[0])
        for j in y:
            if z[0][3] == j[3]:
                z.append(j[0])
        z.remove(z[0])
        for f in y:
            w.append(f[0])
        u = []
        for m in a:
            u.append(m[0])
        return u, ",но эти кандидаты имеют одинаковое кол-во балов", w, "из них по информатике эти набрали больше", z
    else:
        u = []
        for m in a:
            u.append(m[0])

        return u

x = find_top_20(candidates)

print(x)

