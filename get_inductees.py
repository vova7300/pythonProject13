names = ['ver', 'tyj', 'tre', 'daff', 'udes', 'has', 'vew',
         'har', 'fil', 'fds', 'red', 'tgv', 'qwer', 'das', 'sad', 'rop'
         ]
print(len(names))
birthday_years = [1998, None, 2000, 1997, 2001, 2003, 2006, 2007,
                  1996, 1995, 1994, 1000, 2009, 2005, 2003, 2004
                  ]
print(len(birthday_years))
genders = ['Male', 'Male', None, 'Female', 'Male', 'Female', None, 'Male', 'Female', 'Male',
           'Male', 'Male', None, 'Male', 'Male', None
           ]
print(len(genders))
x = names
y = birthday_years
z = genders

def get_inductees(x, y, z):
        a = []
        b = []
        for k in range(len(x)):
                if z[k] == 'Male' and y[k] != None and 30 >= 2021 - y[k] >= 18:
                        a.append(x[k])
                elif (z[k] == 'Male' and y[k] == None) or (z[k] == None and 30 >= 2021 - y[k] >= 18):
                         b.append(x[k])
        return 'военнообязанные', a, 'этих не удалось установить',b

print(get_inductees(names, birthday_years, genders))

