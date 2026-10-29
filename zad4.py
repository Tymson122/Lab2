gol = int(input("Liczba goli: "))
bonus = 0

if gol > 5:
    bonus += 5
if gol > 10:
    bonus += 10

punkty = gol * 10 + bonus
print("Wynik druzyny:", punkty)