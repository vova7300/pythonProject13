


students_avg_scores = {'Max': 4.962, 'Eric': 4.964, 'Peter': 4.923,
                       'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973,
                       'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937
                       }


def make_report_about_top3(x):
    b = []
    c = []
    for key in students_avg_scores:
        c.append(key)
        c.append(students_avg_scores[key])
        b.append(c)
        c = []
        if len(b) > 1:
            for k in range(len(b) - 1, 0, -1):
                if b[k][1] >= b[k - 1][1]:
                    b[k], b[k - 1] = b[k - 1], b[k]
            if len(b) > 3 and b[2][1] > b[3][1]:
                b = b[:3]

    f = open("file.csv", "w+")
    for k in b:
        for i in k:
            i = str(i)
            f.write(i)
            f.write(" ")
        f.write(";\n")
    return f

print(make_report_about_top3(students_avg_scores))
