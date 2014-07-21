def f(x, y):
    x = x + 3
    y.append(23)
    y.append("hola")
    print(x, y)
x = 22
y = [22]
f(x, y)
print(x, y)

