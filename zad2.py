x = int(input("Podaj liczbe x: "))
y = int(input("Podaj liczbe y: "))
z = int(input("Podaj liczbe z: "))

if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x
print("Liczby od najmniejszej: ", x, y, z)