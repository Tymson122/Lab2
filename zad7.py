haslo = "pk47!jy0893"
for i in haslo:
    if i == "!":
        if len(haslo) == 11:
            print("Haslo jest poprawne")
            break
        else:
            print("Haslo jest nie poprawne")
            break