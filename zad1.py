l_punktow = int(input("Podaj liczbe punktow: "))
if l_punktow > 80:
    print("Mozesz zaliczyć egzamin w terminie 0")
elif l_punktow >= 50:
    print("Możesz poprawic wynik")
elif l_punktow < 50:
    print("Musisz poprawic wynik")