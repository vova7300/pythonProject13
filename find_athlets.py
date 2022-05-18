know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]
x = know_english
y = sportsmen
z = more_than_20_years
def find_athlets(x,y,z):
    a = []
    for k in x:
        if k in y and k in z:
            a.append(k)
    return a

print(find_athlets(x,y,z))
